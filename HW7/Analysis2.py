import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

iteration = 5
unbiased_sampling = np.zeros((5, 9))
log_unbiased_sampling = np.zeros(9)

for iteration_num in range(iteration):
    mydata = pd.read_table(
        "/Users/student/Desktop/Imperial/year4/MEng/HW7/ds8_" + str(iteration_num + 1) + "/last_hist.dat",
        header=None, sep='\s+', skip_blank_lines=True)

    for i in mydata.index:

        if i > 0:
            unbiased_sampling[iteration_num][i - 1] = mydata[2][i]
            print(unbiased_sampling[iteration_num][i - 1])


log_unbiased_sampling = np.log(np.mean(unbiased_sampling, axis=0))
print(log_unbiased_sampling)

plt.plot(-log_unbiased_sampling+log_unbiased_sampling[0])
plt.show()

print(np.mean(unbiased_sampling, axis=0))
