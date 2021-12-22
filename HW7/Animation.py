import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

iteration = 5
base_pairs = 9
sample_over_time = np.zeros((5, 12290))
average_sample_over_time = np.zeros((base_pairs, 12290))
list_bar = np.zeros(9)

for base in range(base_pairs):
    for iteration_num in range(iteration):
        mydata = pd.read_table(
            "/Users/student/Desktop/Imperial/year4/MEng/HW7/ds8_" + str(iteration_num + 1) + "/traj_hist.dat",
            header=None, sep='\s+', skip_blank_lines=True)

        for i in mydata.index:
            if mydata[0][i] == '#t':
                sample_over_time[iteration_num][i] = mydata[1][i + base + 1]

    average_sample_over_time[base][:] = np.mean(sample_over_time, axis=0)
    print(len(np.mean(sample_over_time, axis=0)))
    list_bar[base] = average_sample_over_time[base][10000]

plt.bar(range(base_pairs), list_bar[:])
plt.show()

plt.bar(range(base_pairs), average_sample_over_time[0:9, 12000])
plt.show()

plt.plot(average_sample_over_time[5][:])
plt.plot(average_sample_over_time[0][:])
plt.show()

fig, ax = plt.subplots()

# Cropping the timesteps where it is zero
average_sample_over_time_new = average_sample_over_time[0:9,900:-1]

def buildmebarchart(val=int):
    # ax.clear()
    ax.bar(range(base_pairs), average_sample_over_time_new[0:9, val*10], color='blue')
    # ax.text(1, 20, 'Time step: '+str(val*10+100))
    print(val)


anim = ani.FuncAnimation(fig, buildmebarchart, interval=50, frames=1000)
plt.show()

anim.save('linechart.mp4')