import matplotlib.pyplot as plt
import numpy as np


filename = [["NOMAD_1c_x1.42.txt","NOMAD_55c_x1.42.txt"],["NOMAD_1c_x2.42.txt","NOMAD_55c_x2.42.txt"],["NOMAD_1c_x3.42.txt","NOMAD_55c_x3.42.txt"],["NOMAD_1c_x4.42.txt","NOMAD_55c_x4.42.txt"],["NOMAD_1c_x5.42.txt","NOMAD_55c_x5.42.txt"],["NOMAD_1c_x6.42.txt","NOMAD_55c_x6.42.txt"],["NOMAD_1c_x7.42.txt","NOMAD_55c_x7.42.txt"],["NOMAD_1c_x8.42.txt","NOMAD_55c_x8.42.txt"], ["NOMAD_1c_x9.42.txt","NOMAD_55c_x9.42.txt"], ["NOMAD_1c_x10.42.txt","NOMAD_55c_x10.42.txt"], ["NOMAD_1c_x11.42.txt","NOMAD_55c_x11.42.txt"], ["NOMAD_1c_x12.42.txt","NOMAD_55c_x12.42.txt"],["NOMAD_1c_x13.42.txt","NOMAD_55c_x13.42.txt"],["NOMAD_1c_x14.42.txt","NOMAD_55c_x14.42.txt"],["NOMAD_1c_x15.42.txt","NOMAD_55c_x15.42.txt"],["NOMAD_1c_x16.42.txt","NOMAD_55c_x16.42.txt"],["NOMAD_1c_x17.42.txt","NOMAD_55c_x17.42.txt"],["NOMAD_1c_x18.42.txt","NOMAD_55c_x18.42.txt"],["NOMAD_1c_x19.42.txt","NOMAD_55c_x19.42.txt"],["NOMAD_1c_x20.42.txt","NOMAD_55c_x20.42.txt"], ["NOMAD_1c_x21.42.txt","NOMAD_55c_x21.42.txt"],["NOMAD_1c_x22.42.txt","NOMAD_55c_x22.42.txt"],["NOMAD_1c_x23.42.txt","NOMAD_55c_x23.42.txt"],["NOMAD_1c_x24.42.txt","NOMAD_55c_x24.42.txt"],["NOMAD_1c_x25.42.txt","NOMAD_55c_x25.42.txt"],["NOMAD_1c_x26.42.txt","NOMAD_55c_x26.42.txt"],["NOMAD_1c_x27.42.txt","NOMAD_55c_x27.42.txt"],["NOMAD_1c_x28.42.txt","NOMAD_55c_x28.42.txt"], ["NOMAD_1c_x29.42.txt","NOMAD_55c_x29.42.txt"], ["NOMAD_1c_x30.42.txt","NOMAD_55c_x30.42.txt"]]
#color_file = ["green","purple","orange","yellow","black","red"]
color_file = ["green","purple"]
curve_name = ["One Constraint","All Constraints"]

fig, axs = plt.subplots(6, 5)
ligne = 0
col = 0
for k,files in enumerate(filename):

    min = [np.inf for i in range(len(files))]
    min_h = [np.inf for i in range(len(files))]
    scale_x = [[] for i in range(len(files))]
    scale_y = [[] for i in range(len(files))]
    scale_x_h = [[] for i in range(len(files))]
    scale_y_h = [[] for i in range(len(files))]
    points_x = [[] for i in range(len(files))]
    points_y = [[] for i in range(len(files))]
    bbe = [[] for i in range(len(files))]
    obj = [[] for i in range(len(files))]
    cst = [[] for i in range(len(files))]
    time = [[] for i in range(len(files))]


    for i,file in enumerate(files):
        with open(file, "r") as f:
            lines = f.read().splitlines()
            lines2 = [l.split() for l in lines]
            bbe[i] = [int(l[0]) for l in lines2]
            obj[i] = [float(l[1]) for l in lines2]
            cst[i] = [float(l[2]) for l in lines2]
            time[i] = [float(l[3]) for l in lines2]

        for j in range(len(obj[i])):
            if min_h[i] > cst[i][j]:
                scale_y_h[i].append((cst[i])[j])
                scale_x_h[i].append(bbe[i][j])
                min_h[i] = (cst[i])[j]
            if min_h[i] == 0:
                break


        scale_y_h[i].append(min_h[i])
        scale_x_h[i].append(bbe[i][-1])
        

        print(scale_x_h[i])
        print(scale_y_h[i])
        
        
        axs[ligne, col].step(scale_x_h[i], scale_y_h[i],where='post',c=color_file[i],label=curve_name[i])
        axs[ligne, col].set_xscale('log')
        axs[ligne, col].set_yscale('log')
        
        #col = (col + 1) % 2
        
        if col == 0 and ligne ==0:
            plt.xlabel('Number of BlackBox evaluations')
            plt.ylabel('Value of constraint violations')
            plt.legend()
        
    if col == 4:
        ligne += 1
    col = (col + 1) % 5


plt.xlabel('Number of BlackBox evaluations', labelpad=20)
plt.ylabel('Value of constraint violations', rotation=-90, labelpad=-150)
# plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.xscale("log")
plt.yscale("log")
#plt.ylim(-2000,-1400)
plt.legend()
fig.set_size_inches(29, 21)
plt.show()
# plt.savefig("test_subplot.png")