import pandas as pd
import numpy as np

weight_sum = 0
fraction = np.zeros(9)

mydata = pd.read_table("/Users/student/Desktop/Imperial/year4/MEng/HW7/ds8_1/wfile.txt",
                       header=None, names=['Pairs_formed', 'Weight'], sep='\s+', skip_blank_lines=True)

weight_sum = mydata['Weight'].sum()

for i in mydata.index:
    fraction[i] = mydata['Weight'][i]/weight_sum
    print(fraction[i])