import pandapower.networks as nw
import pandapower as pp
import pandapower.plotting as pplt
import pandapower.toolbox as tb
import numpy as np
import seaborn




net = nw.case14()



# colors = seaborn.color_palette()
# bc = plot.create_bus_collection(net, buses=net.bus.index, color=colors[0], size=80, zorder=1)
# lc = plot.create_line_collection(net, lines=net.line.index, color='grey', zorder=2)

# long_lines = net.line.loc[net.line.length_km > 2.].index
# lcl = plot.create_line_collection(net, lines=long_lines, color=colors[2], zorder=2)
# plot.draw_collections([lc, bc, lcl])
# plt.show()

pp.runpp(net)
#print('\n\n', '-----------------------------------NETWORK--------------------------------- :', '\n\n',net)
pplt.simple_plot(net, line_color= 'brown',plot_loads= True, plot_gens=True, gen_size=2)



gen=[net.gen.bus[i] for i in net.gen.index]
grid=[net.ext_grid.bus[i] for i in net.ext_grid.index]
gens=np.concatenate((grid, gen))

for i in range(len(net.bus)):
    if net.bus.name[i] not in gens:
        
        if net.bus.name[i] not in [net.load.bus[i] for i in net.load.index]:
            print(net.bus.name[i])
            
print(gens)
print(3 in [net.gen.bus[i] for i in net.gen.index])