import matplotlib.pyplot as plt
import numpy as np


filename = [["NOMAD_1c_x1.42.txt","NOMAD_55c_x1.42.txt"],["NOMAD_1c_x2.42.txt","NOMAD_55c_x2.42.txt"],["NOMAD_1c_x3.42.txt","NOMAD_55c_x3.42.txt"],["NOMAD_1c_x4.42.txt","NOMAD_55c_x4.42.txt"],["NOMAD_1c_x5.42.txt","NOMAD_55c_x5.42.txt"],["NOMAD_1c_x6.42.txt","NOMAD_55c_x6.42.txt"],["NOMAD_1c_x7.42.txt","NOMAD_55c_x7.42.txt"],["NOMAD_1c_x8.42.txt","NOMAD_55c_x8.42.txt"], ["NOMAD_1c_x9.42.txt","NOMAD_55c_x9.42.txt"], ["NOMAD_1c_x10.42.txt","NOMAD_55c_x10.42.txt"], ["NOMAD_1c_x11.42.txt","NOMAD_55c_x11.42.txt"], ["NOMAD_1c_x12.42.txt","NOMAD_55c_x12.42.txt"],["NOMAD_1c_x13.42.txt","NOMAD_55c_x13.42.txt"],["NOMAD_1c_x14.42.txt","NOMAD_55c_x14.42.txt"],["NOMAD_1c_x15.42.txt","NOMAD_55c_x15.42.txt"],["NOMAD_1c_x16.42.txt","NOMAD_55c_x16.42.txt"],["NOMAD_1c_x17.42.txt","NOMAD_55c_x17.42.txt"],["NOMAD_1c_x18.42.txt","NOMAD_55c_x18.42.txt"],["NOMAD_1c_x19.42.txt","NOMAD_55c_x19.42.txt"],["NOMAD_1c_x20.42.txt","NOMAD_55c_x20.42.txt"],["NOMAD_1c_x21.42.txt","NOMAD_55c_x21.42.txt"],["NOMAD_1c_x22.42.txt","NOMAD_55c_x22.42.txt"],["NOMAD_1c_x23.42.txt","NOMAD_55c_x23.42.txt"],["NOMAD_1c_x24.42.txt","NOMAD_55c_x24.42.txt"],["NOMAD_1c_x25.42.txt","NOMAD_55c_x25.42.txt"],["NOMAD_1c_x26.42.txt","NOMAD_55c_x26.42.txt"],["NOMAD_1c_x27.42.txt","NOMAD_55c_x27.42.txt"],["NOMAD_1c_x28.42.txt","NOMAD_55c_x28.42.txt"], ["NOMAD_1c_x29.42.txt","NOMAD_55c_x29.42.txt"], ["NOMAD_1c_x30.42.txt","NOMAD_55c_x30.42.txt"]]
#color_file = ["green","purple","orange","yellow","black","red"]
color_file = ["blue","magenta"]
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
            obj[i] = [float(l[1])/1000 for l in lines2]
            cst[i] = [float(l[2]) for l in lines2]
            time[i] = [float(l[3]) for l in lines2]

        for j in range(len(obj[i])):
            if cst[i][j] == 0.0:
                if min[i] <= (obj[i])[j]:
                    #scale_y[i].append(min[i])
                    a=2
                else:
                    scale_y[i].append((obj[i])[j])
                    scale_x[i].append(bbe[i][j])
                    min[i] = (obj[i])[j]
                #scale_x[i].append(bbe[i][j])
                points_x[i].append((bbe[i])[j])
                points_y[i].append((obj[i])[j])
            else:
                if min_h[i] <= (cst[i])[j]:
                    #scale_y[i].append(min[i])
                    a=2
                else:
                    scale_y_h[i].append((cst[i])[j])
                    scale_x_h[i].append(bbe[i][j])
                    min_h[i] = (cst[i])[j]

        scale_y[i].append(scale_y[i][-1])
        scale_x[i].append(bbe[i][j])
        scale_y_h[i].append(scale_y_h[i][-1])
        scale_x_h[i].append(bbe[i][j])
        

        # scale_x = range(len(bbe))
        
        print(len(scale_x[i]))
        print(scale_x[i])
        print(scale_y[i])
        
        
        #plt.step(scale_x[i], scale_y[i],where='post',c=color_file[i],label=curve_name[i])
        # plt.step(scale_x[i], scale_y[i],where='post',c=color_file[i],label=curve_name[i])
        #plt.scatter(points_x[i], points_y[i], c=color_file[i], marker='x')
        
        axs[ligne, col].step(scale_x[i], scale_y[i],where='post',c=color_file[i],label=curve_name[i])
        axs[ligne, col].set_xscale('log')
        #axs[ligne, col].set_yscale('log')
        
        
        #col = (col + 1) % 2
        
    if col == 4:
        ligne += 1
    col = (col + 1) % 5

plt.xlabel('Number of BlackBox evaluations', labelpad=20)
plt.ylabel('Value of objective function (* 10^3)', rotation=-90, labelpad=-150)
#plt.ticklabel_format(axis='y', style='plain')
#plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
# plt.xscale("log")
# plt.yscale("log")
#plt.ylim(-2000,-1400)
plt.legend()
fig.set_size_inches(15, 15)
plt.show()
# plt.savefig("test_subplot.png")