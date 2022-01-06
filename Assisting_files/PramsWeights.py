import pandas as pd
import numpy as np
import itertools
import re

params = {
    'base_pairs': [0, 1, 2, 3, 4, 5],
    'distance': [0, 1],
    'other': [4, 5, 6, 6]

}

params2 = {
    'base_pairs_weights': [7.5, 2500, 400, 20, 5, 4],
    'distance_weights': [1, 0],
    'other': [1, 1, 1, 1]

}

f = open("wfile.txt", "w")
counter = 0

print(list(itertools.product(*params.values())))

combos = list(itertools.product(*params.values()))

weights = np.zeros(len(combos))

for values in list(itertools.product(*params2.values())):
    print(values[0]*values[1])
    weights[counter] = values[0]*values[1]
    counter += 1

counter = 0
for i in combos:
    print(i)
    text = str(i) + " " + str(weights[counter]) + '\n'
    patn = re.sub(r"[(,)]", "", text)
    f.write(patn)
    counter += 1
f.close()


