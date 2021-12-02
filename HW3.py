import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def convert(lst):
    return lst[:].split()


MD = 12  # I've only done it for 1 right now. We can average over 12 when we get one working?
repetitions = 1  # Out of 4

data_points = 1000000

counter = 0
timesteps = 4000  # Change this for yours' it will be 400 i guess

total_array = np.zeros((MD, repetitions))
average_of_rep = np.zeros(MD)
force_array = np.zeros(MD)

start_vals = np.zeros(timesteps)
end_vals = np.zeros(timesteps)
total_vals = np.zeros(timesteps)

parameters = [

    {'file_num': '3', 'legend_title': 'Real Sequence', 'colour': 'red'},
    {'file_num': '4', 'legend_title': 'Average Sequence', 'colour': 'blue'},
    {'file_num': '5', 'legend_title': 'No Stacking', 'colour': 'black'}

]

for params in parameters:
    for force in range(MD):
        for rep in range(repetitions):
            mydataMD = pd.read_table("/Users/student/Desktop/Imperial/year4/MEng/HW" + params['file_num'] + "/F_"
                                     + str(rep * 12 + force + 1) + "/trajectory.dat", header=None,
                                     names=['position_x', 'position_y', 'position_z'], sep='\s+', skip_blank_lines=True)
            for i in range(data_points):

                if mydataMD['position_x'][i] == 't':
                    print(mydataMD['position_z'][i])
                    print(mydataMD['position_z'][i+3])
                    print(mydataMD['position_z'][i+102])

                    start_vals[counter] = mydataMD['position_z'][i+3]
                    end_vals[counter] = mydataMD['position_z'][i+102]

                    total_vals[counter] = start_vals[counter] - end_vals[counter]
                    print(total_vals[counter])

                    counter += 1
                    print(counter)
                if counter == timesteps:
                    break
            print(counter)
            print(sum(total_vals)/counter)  # I hope this is giving mean? lol
            total_array[force, rep] = sum(total_vals)/counter  # Should be 12 by 4
            counter = 0
        print(counter)
        average_of_rep[force] = sum(total_array[force, :])/repetitions

        f = open("/Users/student/Desktop/Imperial/year4/MEng/HW3/F_" + str(force + 1) + "/external.conf", 'r')
        lines = f.readlines()
        already_found = False

        for line in range(len(lines)):
            if convert(lines[line][0]) == ['F']:
                line_as_list = convert(lines[line])
                print(line_as_list)
                force_array[force] = float(line_as_list[2])
                print(float(line_as_list[2]))
                already_found = True
            if already_found:
                break
            f.close()

    print(average_of_rep[0])
    # print(average_of_rep[2]) #Just to see. and there should be 12 points?

    plt.plot(average_of_rep, force_array, 'o', color=params['colour'])
    plt.plot(average_of_rep, force_array, '--', linewidth=0.5, color=params['colour'], label=params['legend_title'])

plt.xlabel('Extension per base (nm)')
plt.ylabel('Force (pN)')
plt.title('The response of ssDNA to tension\n (and the role of stacking therein)')
plt.legend()
plt.show()
