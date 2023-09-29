import pandapower.networks as nw
import pandapower as pp
import pandapower.plotting as pplt
import pandapower.toolbox as tb
import numpy as np
import pandapower.converter as pc


#net = pc.from_mpc("case9.mat", f_hz=60)
net = nw.case39()
#net = nw.case6ww()
#net = nw.mv_oberrhein()
#net = nw.iceland()
#net = nw.case89pegase()
#net = nw.case24_ieee_rts

# for i in range (len(net.ext_grid)):
#     net.ext_grid.vm_pu[i] = 1
#     net.ext_grid.va_degree[i] = 0


#z=[30.296484109293427, 32.117741500373754, 38.528330341195606, 28.37182334554266, 32.144665207650114]


# for i in range (len(net.gen)):
#     net.gen.p_mw[i] = z[i]
    

# for i in range (len(net.gen) + len(net.ext_grid)):
#     net.poly_cost.cp0_eur[i] = 0
#     net.poly_cost.cp1_eur_per_mw[i] = 1
#     net.poly_cost.cp2_eur_per_mw2[i] = 0.01

# for i in range (len(net.ext_grid)):
#     net.poly_cost.cp0_eur[0] = 0
#     net.poly_cost.cp1_eur_per_mw[0] = 0
#     net.poly_cost.cp2_eur_per_mw2[0] = 0
    



#print('\n\n', '-----------------------------------NETWORK--------------------------------- :', '\n\n',net)

print('\n\n', '-----------------------------------BUS--------------------------------- :', '\n\n', net.bus)

print('\n\n\n\n', '--------------------------------------LOAD -------------------------------- :', '\n\n', net.load)

print('\n\n\n\n', '--------------------------------------GEN-------------------------------- :', '\n\n', net.gen)

print('\n\n\n\n', '---------------------------------------EXT_GRID --------------------------------- :', '\n\n', net.ext_grid)

print('\n\n\n\n', '--------------------------------------LINE -------------------------------- :', '\n\n', net.line)

#print('\n\n\n\n', '-------------------------------------------SGEN ---------------------------------- :', '\n\n', net.sgen)

print('\n\n\n\n', '---------------------------------------POLY_COST --------------------------------- :', '\n\n', net.poly_cost)

print('\n\n\n\n', '---------------------------------------SHUNT --------------------------------- :', '\n\n', net.shunt)

print('\n\n\n\n', '---------------------------------------TRAFO --------------------------------- :', '\n\n', net.trafo)







#pp.runopp(net, verbose=False, suppress_warnings=True, init= 'flat', delta = 0.0001, OPF_VIOLATION = 0.0000000000001)

pp.runopp(net,verbose=True)

print('\n\n', '-----------------------------------NETWORK--------------------------------- :', '\n\n',net)

#pp.runpm_ac_opf(net)

#tb.lf_info(net)

#pp.runopp(net, run_control=True)

#pp.control.run_control(net)






print('\n\n\n\n\n\n', '______________________________________________RESULTATS_______________________________________________','\n\n\n\n\n\n')




print('\n\n', '-----------------------------------BUS--------------------------------- :', '\n\n', net.res_bus)

print('\n\n\n\n', '--------------------------------------LOAD -------------------------------- :', '\n\n', net.res_load)

print('\n\n\n\n', '--------------------------------------GEN-------------------------------- :', '\n\n', net.res_gen)

print('\n\n\n\n', '---------------------------------------EXT_GRID --------------------------------- :', '\n\n', net.res_ext_grid)

print('\n\n\n\n', '--------------------------------------LINE -------------------------------- :', '\n\n', net.res_line)

#print('\n\n\n\n', '-------------------------------------------SGEN ---------------------------------- :', '\n\n', net.res_sgen)


print('\n\n\n\n', '---------------------------------------SHUNT --------------------------------- :', '\n\n', net.res_shunt)

print('\n\n\n\n', '---------------------------------------TRAFO --------------------------------- :', '\n\n', net.res_trafo)

print('\n\n\n\n', '-------------------------------------------COST ---------------------------------- :', '\n\n', net.res_cost)




# f=0

# a=0
# b=1
# c=0.01

# for i in range(len(net.gen)):
#     f += a + b * net.res_gen.p_mw[i] + c * net.res_gen.p_mw[i]**2

# for i in range(len(net.ext_grid)):
#     f += a + b * net.res_ext_grid.p_mw[i] + c * net.res_ext_grid.p_mw[i]**2




# f=0

# for i in range(len(net.poly_cost)):
#     if net.poly_cost.et[i] == 'gen':
#         f += net.poly_cost.cp0_eur[i] + net.poly_cost.cp1_eur_per_mw[i] * net.res_gen.p_mw[net.poly_cost.element[i]] + net.poly_cost.cp2_eur_per_mw2[i] * net.res_gen.p_mw[net.poly_cost.element[i]]**2

# for i in range(len(net.poly_cost)):
#     if net.poly_cost.et[i] == 'ext_grid':
#         f += net.poly_cost.cp0_eur[i] + net.poly_cost.cp1_eur_per_mw[i] * net.res_ext_grid.p_mw[net.poly_cost.element[i]] + net.poly_cost.cp2_eur_per_mw2[i] * net.res_ext_grid.p_mw[net.poly_cost.element[i]]**2


f=0                                            

for i in range(len(net.poly_cost)):
                    
    if net.poly_cost.et[i] == 'gen':                                # Cost coefficients and computation of f due to generators (including slack bus)
        
        f += net.poly_cost.cp0_eur[i] + net.poly_cost.cp1_eur_per_mw[i] * net.res_gen.p_mw[net.poly_cost.element[i]] + net.poly_cost.cp2_eur_per_mw2[i] * net.res_gen.p_mw[net.poly_cost.element[i]]**2


    if net.poly_cost.et[i] == 'ext_grid':                           # Cost coefficients and computation of f due to external grids

        f += net.poly_cost.cp0_eur[i] + net.poly_cost.cp1_eur_per_mw[i] * net.res_ext_grid.p_mw[net.poly_cost.element[i]] + net.poly_cost.cp2_eur_per_mw2[i] * net.res_ext_grid.p_mw[net.poly_cost.element[i]]**2




puissances=[]
voltages=[]

for i in range(len(net.gen)):
    puissances+=[round(net.res_gen.p_mw[i],4)]
    voltages+=[round(net.res_gen.vm_pu[i],4)]
    
output = (' '.join(str(elem) for elem in puissances))
output2 = (' '.join(str(elem) for elem in voltages))


print('\n\n\n\n\n\n', '________________OUTPUTS_OPF_PYPOWER________________','\n\n')

print('Active power results : ', output ,'\n')

print('Magnitude voltage results : ', output2 ,'\n\n')
    
#print('Fonction objectif f : ', f, '\n\n\n\n\n\n')










#------------------CONTRAINTES > 0---------------------------------------------------------------------------------------

                                                                #Contraintes 4,5 des generateurs
c4g=np.zeros(len(net.gen))
c5g=np.zeros(len(net.gen))

for i in range(len(net.gen)):
    c4g[i]= -(net.res_gen.p_mw[i] - net.gen.min_p_mw[i])                                         # pimin - pi des gen
    c5g[i]= -(net.gen.max_p_mw[i] - net.res_gen.p_mw[i])                                         # pi - pimax des gen                  
                    




                                                                #Contraintes 4,5 des charges
                                                                #Inutile car les donnees des charges sont fixees et invariantes
c4l=np.zeros(len(net.load))
c5l=np.zeros(len(net.load))
#for i in range(len(net.load)):
    #c4l[i] = -(net.res_load.p_mw[i] - net.load.min_p_mw[i])                                     # pimin - pi des load
    #c5l[i] = -(net.load.max_p_mw[i] - net.res_load.p_mw[i])                                     # pi - pimax des load








                                                                #Contraintes 6,7 des generateurs
c6g=np.zeros(len(net.gen))
c7g=np.zeros(len(net.gen))
for i in range(len(net.gen)):
    c6g[i] = -(net.res_gen.q_mvar[i] - net.gen.min_q_mvar[i])                                     # qimin - qi des gen
    c7g[i] = -(net.gen.max_q_mvar[i] - net.res_gen.q_mvar[i])                                     # qi - qimax des gen                                            





                                                                #Contraintes 6,7 des charges
                                                                #Inutile car les donnees des charges sont fixees et invariantes
c6l=np.zeros(len(net.load))
c7l=np.zeros(len(net.load))
#for i in range(len(net.load)):
    #c6l[i] = -(net.res_load.q_mvar[i] - net.load.min_q_mvar[i])                                  # qimin - qi des load
    #c7l[i] = -(net.load.max_q_mvar[i] - net.res_load.q_mvar[i])                                  # qi - qimax des load   








                                                                #Contraintes 8
c8=np.zeros(len(net.line))
for i in range(len(net.line)):
    c8[i] = -(100 - net.res_line.loading_percent[i])                                            # puissance de chaques lignes < 100%







                                                                #Contraintes 9
c9i=np.zeros(len(net.bus))
c9s=np.zeros(len(net.bus))
for i in range(len(net.bus)):
    c9i[i] = -(net.res_bus.vm_pu[i] - net.bus.min_vm_pu[i])                                      # vi - vimin 
    c9s[i] = -(net.bus.max_vm_pu[i] - net.res_bus.vm_pu[i])                                      # vimax - vi 






#-------------------------------------OUTPUTS------------------------------------------------------------------------

contraintes=[]

contraintes = np.concatenate((c4g, c5g, c4l, c5l, c6g, c7g, c6l, c7l, c8, c9i, c9s))

contrainte = np.sum(np.maximum(contraintes,0))


#print(f, contrainte)
print('Objective function f :', f, '\n\n') 
#print('Violation contraintes h :' ,contrainte, '\n\n\n\n\n\n')






                                                            
#                                                                         #Affichage des contraintes violees
                                                            
print('\n\n', '----------------------------- CONTRAINTES VIOLEES ------------------------------- :')


if not np.array_equal(np.maximum(c4g,0), np.zeros(len(c4g))):
    print('\n\n', 'pmin - p_gen :')
    print(np.maximum(c4g,0))
    
if not np.array_equal(np.maximum(c5g,0), np.zeros(len(c5g))):
    print('\n\n', 'p_gen - pmax :')
    print(np.maximum(c5g,0))
    
    
if not np.array_equal(np.maximum(c4l,0), np.zeros(len(c4l))):
    print('\n\n', 'pmin - p_load :')
    print(np.maximum(c4l,0))
    
if not np.array_equal(np.maximum(c5l,0), np.zeros(len(c5l))):
    print('\n\n', 'p_load - pmax :')
    print(np.maximum(c5l,0))
    
    
if not np.array_equal(np.maximum(c6g,0), np.zeros(len(c6g))):
    print('\n\n', 'qmin - q_gen :')
    print(np.maximum(c6g,0))
    
if not np.array_equal(np.maximum(c7g,0), np.zeros(len(c7g))):
    print('\n\n', 'q_gen - qmax :')
    print(np.maximum(c7g,0))
    
    
if not np.array_equal(np.maximum(c6l,0), np.zeros(len(c6l))):
    print('\n\n', 'qmin - q_load :')
    print(np.maximum(c6l,0))
    
if not np.array_equal(np.maximum(c7l,0), np.zeros(len(c7l))):
    print('\n\n', 'q_load - qmax :')
    print(np.maximum(c7l,0))


if not np.array_equal(np.maximum(c8,0), np.zeros(len(c8))):
    print('\n\n', 'line_loading_percent :')
    print(np.maximum(c8,0))
    
    
if not np.array_equal(np.maximum(c9i,0), np.zeros(len(c9i))):
    print('\n\n', 'vmin - v :')
    print(np.maximum(c9i,0))
    
if not np.array_equal(np.maximum(c9s,0), np.zeros(len(c9s))):
    print('\n\n', 'v - vmax :')
    print(np.maximum(c9s,0))