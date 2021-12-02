import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.DataFrame()
MD = 15
VMMC = 15
data_points = 20000
dimentions = 2
MD_array = np.zeros((data_points, dimentions))
VMMC_array = np.zeros((data_points, dimentions))

for iteration in range(MD):
    mydataMD = pd.read_table("/Users/student/Desktop/Imperial/year4/MEng/HW2/num20_"+str(iteration+1)+"/energy.dat", header=None, names=['time', 'potential', 'kinetic', 'total'], sep='\s+')
    for i in range(data_points):
        MD_array[i, 0] += mydataMD['time'][i]
        MD_array[i, 1] += mydataMD['potential'][i]

for iteration in range(VMMC):
    mydataVMMC = pd.read_table("/Users/student/Desktop/Imperial/year4/MEng/HW2/num20_"+str(iteration+6)+"/energy.dat", header=None, sep='\s+')
    for i in range(data_points):
        VMMC_array[i, 0] += mydataVMMC[0][i]
        VMMC_array[i, 1] += mydataVMMC[1][i]

MD_array[:, :] = MD_array[:, :]/MD
VMMC_array[:, :] = VMMC_array[:, :]/VMMC
plt.plot(MD_array[:, 0], MD_array[:, 1], 'r', label='MC')
plt.plot(VMMC_array[:, 0], VMMC_array[:, 1], 'b', label='VMMC')
plt.xlabel('Timesteps')
plt.ylabel('Energy')
plt.title('Equilibration plots with 20 bases')
plt.legend()

plt.savefig('/Users/student/Desktop/Imperial/year4/MEng/HW2/Plot_a_HW1')
plt.show()
