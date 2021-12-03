import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

## A function that gives you a list of folders in the directory you are

df = pd.DataFrame()
MD = 5
VMMC = 5
data_points = 20000
dimentions = 2
MD_array = np.zeros((data_points, dimentions))
VMMC_array = np.zeros((data_points, dimentions))
equil_time_MD = 0
equil_time_VMMC = 0

for iteration in range(MD):
    first_time = True
    mydataMD = pd.read_table("/Users/student/Desktop/Imperial/year4/MEng/HW1/num20/num20_"+str(iteration+1)+"/energy.dat", header=None, names=['time', 'potential', 'kinetic', 'total'], sep='\s+')
    for i in range(data_points):
        MD_array[i, 0] += mydataMD['time'][i]
        MD_array[i, 1] += mydataMD['potential'][i]
        if (mydataMD['potential'][i] > -0.875) and (first_time == True):
            first_time = False
            equil_time_MD = equil_time_MD + mydataMD['time'][i]

equil_time_MD = equil_time_MD/MD
print(equil_time_MD)

for iteration in range(VMMC):
    first_time = True
    mydataVMMC = pd.read_table("/Users/student/Desktop/Imperial/year4/MEng/HW1/num20/num20_"+str(iteration+6)+"/energy.dat", header=None, sep='\s+')
    for i in range(data_points):
        VMMC_array[i, 0] += mydataVMMC[0][i]
        VMMC_array[i, 1] += mydataVMMC[1][i]

        if (mydataVMMC[1][i] > -0.9) and (first_time == True):
            first_time = False
            equil_time_VMMC = equil_time_VMMC + mydataVMMC[0][i]

equil_time_VMMC = equil_time_VMMC/VMMC
print(equil_time_VMMC)

MD_array[:, :] = MD_array[:, :]/MD
VMMC_array[:, :] = VMMC_array[:, :]/VMMC
plt.plot(MD_array[:, 0], MD_array[:, 1], 'r', label='MC')
plt.plot(VMMC_array[:, 0], VMMC_array[:, 1], 'b', label='VMMC')
plt.xlabel('Timesteps')
plt.ylabel('Energy')
plt.title('Equilibration plots with 20 bases')
plt.legend()

plt.savefig('/Users/student/Desktop/Imperial/year4/MEng/HW1/num20/Plot_a_HW1')
plt.show()
