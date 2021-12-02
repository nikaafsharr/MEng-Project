import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def convert(lst):
    return (lst[:].split())

file = 'submit_parallel.sh.e4810863.' #Change this file accordingly
#Make sure that it is adjusted for MD and VMMC
iterations = 5
fraction_time = np.zeros(iterations)
for iteration in range(iterations):
    f = open('/Users/student/Desktop/Imperial/year4/MEng/HW1/num1000/files/'+file+str(iteration+1),'r')
    #Change path of file accordingly
    lines = f.readlines()
    already_found = False
    total_time = 0
    time_taken_to_equil = 0

    for line in range(len(lines)):
        if convert(lines[line][0]) == ['>']:
            line_as_list = convert(lines[line])
            print(line_as_list)
            if line_as_list[1] == 'SimBackend':
                print(float(line_as_list[2]))
                total_time = float(line_as_list[2])
                print(float(line_as_list[4]))
                time_taken_to_equil = float(line_as_list[4])
                already_found = True
            if already_found == True:
                break
    fraction_time[iteration] = time_taken_to_equil/total_time
    print(fraction_time[iteration])
    f.close()

print(sum(fraction_time)/iterations)


# print("Read Line: %s" % (lines))

# status = True
# line_index = 0
# while status == True:
#     if mydataMD[0][line_index] == '>':
#         print(mydataMD[1][line_index])
#         status = False
#
#     if status == False:
#         break
#
#     line_index += 1