import sys
import numpy as np
import pandapower.networks as nw
import pandapower as pp


arg1 = sys.argv[1] 

if arg1 == "-h":
    print("\n_____________________________________________________________________________________________________________________________________________\n")
    print("BBPF, Blackbox Power Flow")
    print("BBPF is a blackbox optimization problem instance for the Power Flow problem. \n\n")
    
    print("For a network with n generators, 0 slack bus and 1 external grid :")
    print("  Input  :  Pg1, Pg2, ..., Pgn, |vg1|, |vg2|, ..., |vgn|")
    print("                    Pg1, Pg2, ..., Pgn are generator active powers")
    print("                    |vg1|, |vg2|, ..., |vgn| are generator magnitude voltages\n")
    
    print("  Output :  f, CSTR   OR   f, CSTR1, CSTR2, ..., CSTRk")
    print("                    f > 0 is the operating costs of power system due to generators")
    print("                    f = np.inf if an error occurs in the BBPF such as no convergence during the Power Flow analysis")
    print("                    CSTR is the value of the aggregated constraint violation of all contraints")
    print("                    CSTR1, CSTR2, ..., CSTRk are the constraint violation of all contraints")
    print("                    CSTR = 0 if the constraint i is respected")
    print("                    CSTR > 0 if the constraint i is violated (higher value of constraint violation means more important constraint violations) \n\n\n")

    print("Run a BBPF instance : BBPF.py nb_buses nb_cstr x.txt")
    print("  nb_buses : Number of buses: integer in {14, 39, 118}")
    print("             Import the cooresponding network available on Pandapower\n")

    print("  nb_cstr  : Number of output constraints: String in {-one or -all}")
    print("             -one : all constraints are agregated    : output = f, CSTR ")
    print("             -all : all constraint value are output  : output = f, CSTR1, CSTR2, ..., CSTRk \n")
        
    print("  x.txt    : Input vector in a txt file  : Point at which the simulator is evaluated")
    print("             Please use Help(2) to have input bounds for a specific network")
    print("             For a network with n generators, 0 slack bus and 1 external grid :")
    print("             input : x = Pg1, Pg2, ..., Pgn, |vg1|, |vg2|, ..., |vgn| \n\n\n")
    
    print(" Help (1) : BBPF.py -h")
    print(" Install  : BBPF.py -i")
    print(" Version  : BBPF.py -v")
    print(" Help (2) : BBPF.py nb_buses -h")
    print(" Run      : BBPF.py nb_buses nb_cstr x.txt")
    print("\n_____________________________________________________________________________________________________________________________________________\n")
    exit()


elif arg1 == "-v":
    print("\n_____________________________________________________________________________________________________________________________________________\n")
    print("Version: 1.0, October 2023")
    print("  Contributor: S. Salim (FS)")
    print("  Please report bugs to stephanejeff.salim@gmail.com")
    print("\n_____________________________________________________________________________________________________________________________________________\n")
    exit()

elif arg1 == "-i":
    print("\n_____________________________________________________________________________________________________________________________________________\n")
    print("Please install Python libraries numpy, pandapower and numba with these instructions :")
    print("  pip install numpy      (to perform mathematical operations on arrays)")
    print("  pip install pandapower (to load existing networks and run a Power Flow)")
    print("  pip install numba      (to accelerate the Power Flow computation)")
    print("\n_____________________________________________________________________________________________________________________________________________\n")
    exit()

elif arg1 == "14":
    arg2 = sys.argv[2]
    if arg2 == "-h":
        print("\n_____________________________________________________________________________________________________________________________________________\n")
        print("Network of 14 buses including 5 generators (0 slack bus, 1 external grid and 4 standard generators), 11 loads, 15 lines and 5 transformers.")
        print("Number of all constraints (-all option): 55\n\n")
        print("Basic parameters in NOMAD: ")
        print("  DIMENSION      : 8")
        print("  BB_OUTPUT_TYPE : OBJ PB")
        print("  LOWER_BOUND    :( 0.0 0.0 0.0 0.0 0.94 0.94 0.94 0.94 )")
        print("  UPPER_BOUND    :( 140.0 100.0 100.0 100.0 1.06 1.06 1.06 1.06 )")
        print("\n_____________________________________________________________________________________________________________________________________________\n")
        exit()

    else:
        net = nw.case14()
        
        if arg2 == "-one":
            allcstr = 1
        elif arg2 == "-all":
            allcstr = 55
        else:
            print("Error of the number of constraints (only -one or -all are allowed)")
            exit()
            
        arg3 = sys.argv[3]
        if len(np.loadtxt(arg3, dtype=float)) == 8 :
            x = np.loadtxt(arg3, dtype=float)
        else:
            print("Error with the initial vector size (the size must be 8 for the network of 14 buses)")
            exit()



elif arg1 == "39":
    arg2 = sys.argv[2]
    if arg2 == "-h":
        print("\n_____________________________________________________________________________________________________________________________________________\n")
        print("Network of 39 buses including 10 generators (0 slack bus, 1 external grid and 9 standard generators), 21 loads, 35 lines and 11 transformers.")
        print("Number of all constraints (-all option): 135\n\n")
        print("Basic parameters in NOMAD: ")
        print("  DIMENSION      : 18")
        print("  BB_OUTPUT_TYPE : OBJ PB")
        print("  LOWER_BOUND    :( 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 )")
        print("  UPPER_BOUND    :( 1040.0 725.0 652.0 508.0 687.0 580.0 564.0 865.0 1100.0 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 )")
        print("\n_____________________________________________________________________________________________________________________________________________\n")
        exit()

    else:
        net = nw.case39()
        
        if arg2 == "-one":
            allcstr = 1
        elif arg2 == "-all":
            allcstr = 135
        else:
            print("Error of the number of constraints (only -one or -all are allowed)")
            exit()
            
        arg3 = sys.argv[3]
        if len(np.loadtxt(arg3, dtype=float)) == 18 :
            x = np.loadtxt(arg3, dtype=float)
        else:
            print("Error with the initial vector size (the size must be 18 for the network of 39 buses)")
            exit()



elif arg1 == "118":
    arg2 = sys.argv[2]
    if arg2 == "-h":
        print("\n_____________________________________________________________________________________________________________________________________________\n")
        print("Network of 118 buses including 54 generators (0 slack bus, 1 external grid and 53 standard generators), 99 loads, 15 lines and 13 transformers.")
        print("Number of all constraints (-all option): 519\n\n")
        print("Basic parameters in NOMAD: ")
        print("  DIMENSION      : 106")
        print("  BB_OUTPUT_TYPE : OBJ PB")
        print("  LOWER_BOUND    :( 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 0.94 )")
        print("  UPPER_BOUND    :( 100.0 100.0 100.0 100.0 550.0 185.0 100.0 100.0 100.0 100.0 320.0 414.0 100.0 107.0 100.0 100.0 100.0 100.0 100.0 119.0 304.0 148.0 100.0 100.0 255.0 260.0 100.0 491.0 492.0 100.0 100.0 100.0 100.0 100.0 100.0 577.0 100.0 104.0 707.0 100.0 100.0 100.0 100.0 352.0 140.0 100.0 100.0 100.0 100.0 136.0 100.0 100.0 100.0 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 1.06 )")
        print("\n_____________________________________________________________________________________________________________________________________________\n")
        exit()

    else:
        net = nw.case118()
        
        if arg2 == "-one":
            allcstr = 1
        elif arg2 == "-all":
            allcstr = 519
        else:
            print("Error of the number of constraints (only -one or -all are allowed)")
            exit()
            
        arg3 = sys.argv[3]
        if len(np.loadtxt(arg3, dtype=float)) == 106 :
            x = np.loadtxt(arg3, dtype=float)  
        else:
            print("Error with the initial vector size (the size must be 106 for the network of 118 buses)")
            exit()

else:
    print("Error with the number of buses (only 14, 39 or 118 are allowed)")
    exit()
    



                                               
try:                                                # We're trying the Power Flow (using Newton-Raphson convergence)

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
            

    # print(b[62])





    #_____________________________________OUTPUTS______________________________________________________________________________________________________________________

    constraints=[]

    
    constraints = np.concatenate((c_pmin_ext_grid,c_pmax_ext_grid,c_qmin_ext_grid,c_qmax_ext_grid,c_qmin_gen,c_qmax_gen,c_lmax_line,c_vmin,c_vmax))
    
    all_constraints = np.maximum(constraints,0)         # All contraints are separated. For each contraints, constraint = 0 if the constraint is respected.
    
    if allcstr != 1:
        output = (' '.join(str(elem) for elem in all_constraints))
    else:
        output = np.sum(np.maximum(constraints,0))

    print(f, output)


                                                
except:                                  # Redirect here when the Power Flow cannot be satisfied (When no network reconfiguration is possible with the proposed inputs)
    output = np.inf*np.ones((1,allcstr+1))
    output = (' '.join(str(elem) for elem in output))
    print(output[1:-1])
    #print(output)