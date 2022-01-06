import pandas as pd
import numpy as np

base_pair_weights = [7.5, 2500, 400, 20, 5, 4]
distance_weights = [1, 0]

weight = np.zeros((len(base_pair_weights)) * (len(distance_weights)))

f = open("wfile.txt", "w")

counter = 0
for i in range(len(base_pair_weights)):
    for j in range(len(distance_weights)):
        weight[counter] = base_pair_weights[i] * distance_weights[j]
        print(str(i) + " " + str(j) + " " + str(weight[counter]) + "\n")
        f.write(str(i) + " " + str(j) + " " + str(weight[counter]) + "\n")
        counter += 1

f.close()
