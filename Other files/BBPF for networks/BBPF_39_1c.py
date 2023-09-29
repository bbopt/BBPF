import sys
import numpy as np
import pandapower.networks as nw
import pandapower as pp


                                                
try:                                                # We're trying the Power Flow (using Newton-Raphson convergence)
    
    x = np.loadtxt(sys.argv[1], dtype=float)        # Retrieval of suggestions of P and V of generators

    net = nw.case39()                               # Choice of network

    for i in range (len(net.gen)):                  # Integration of inputs into the network : P and V of generators
        net.gen.p_mw[i] = x[i]
        net.gen.vm_pu[i] = x[len(net.gen) + i]

    pp.runpp(net)                                   # Power Flow (Newton) : Constraints A, B and C






    #______________________OBJECTIVE_FUNCTION_f__________________________________________________________________________________________________________________________


    f=0                                            

    for i in range(len(net.poly_cost)):
                     
        if net.poly_cost.et[i] == 'gen':                                # Cost coefficients and computation of f due to generators (including slack bus)
            
            f += net.poly_cost.cp0_eur[i] + net.poly_cost.cp1_eur_per_mw[i] * net.res_gen.p_mw[net.poly_cost.element[i]] + net.poly_cost.cp2_eur_per_mw2[i] * net.res_gen.p_mw[net.poly_cost.element[i]]**2


        if net.poly_cost.et[i] == 'ext_grid':                           # Cost coefficients and computation of f due to external grids

            f += net.poly_cost.cp0_eur[i] + net.poly_cost.cp1_eur_per_mw[i] * net.res_ext_grid.p_mw[net.poly_cost.element[i]] + net.poly_cost.cp2_eur_per_mw2[i] * net.res_ext_grid.p_mw[net.poly_cost.element[i]]**2






    #_____________________CONSTRAINTS < 0___________________________________________________________________________________________________________________________________


    c_pmin_ext_grid=np.zeros(len(net.ext_grid))                                      
    c_pmax_ext_grid=np.zeros(len(net.ext_grid))
    c_qmin_ext_grid=np.zeros(len(net.ext_grid))                                      
    c_qmax_ext_grid=np.zeros(len(net.ext_grid))

    for i in range(len(net.ext_grid)):                                                                  # External Grid contraints on P and Q
        
        c_pmin_ext_grid[i]= -(net.res_ext_grid.p_mw[i] - net.ext_grid.min_p_mw[i])                                 # pimin - pi of external grids
        c_pmax_ext_grid[i]= -(net.ext_grid.max_p_mw[i] - net.res_ext_grid.p_mw[i])                                 # pi - pimax of external grids
                        
        c_qmin_ext_grid[i]= -(net.res_ext_grid.q_mvar[i] - net.ext_grid.min_q_mvar[i])                             # qimin - qi of external grids
        c_qmax_ext_grid[i]= -(net.ext_grid.max_q_mvar[i] - net.res_ext_grid.q_mvar[i])                             # qi - qimax of external grids 





                                                                            
    c_qmin_gen=np.zeros(len(net.gen))
    c_qmax_gen=np.zeros(len(net.gen))

    for i in range(len(net.gen)):                                                                       # Generator constraints on Q
        
        c_qmin_gen[i] = -(net.res_gen.q_mvar[i] - net.gen.min_q_mvar[i])                                        # qimin - qi des gen
        c_qmax_gen[i] = -(net.gen.max_q_mvar[i] - net.res_gen.q_mvar[i])                                        # qi - qimax des gen                                            






                                                                        
    c_lmax_line=np.zeros(len(net.line))
    
    for i in range(len(net.line)):                                                                      # Line constraints on L
        
        c_lmax_line[i] = -(100 - net.res_line.loading_percent[i])                                             # loading of each lines < 100%






    c_vmin=np.zeros(len(net.bus))
    c_vmax=np.zeros(len(net.bus))

    gen=[net.gen.bus[i] for i in net.gen.index]
    grid=[net.ext_grid.bus[i] for i in net.ext_grid.index]
    gens=np.concatenate((grid, gen))

    for i in range(len(net.bus)):
        
        if net.bus.name[i] not in gens:                                                                # Loads and junctions constraints on V
            
            c_vmin[i] = -(net.res_bus.vm_pu[i] - net.bus.min_vm_pu[i])                                        # vi - vimin 
            c_vmax[i] = -(net.bus.max_vm_pu[i] - net.res_bus.vm_pu[i])                                        # vimax - vi
            







    #_____________________________________OUTPUTS______________________________________________________________________________________________________________________

    constraints=[]

    constraints = np.concatenate((c_pmin_ext_grid,c_pmax_ext_grid,c_qmin_ext_grid,c_qmax_ext_grid,c_qmin_gen,c_qmax_gen,c_lmax_line,c_vmin,c_vmax))

    output = np.sum(np.maximum(constraints,0))                  # All contraints are agregated here. For each contraints, constraint = 0 if the constraint is respected.

    print(f, output)
    



                                                
except:                                  # Redirect here when the Power Flow cannot be satisfied (When no network reconfiguration is possible with the proposed inputs)
    
    print(np.inf, np.inf)                                       