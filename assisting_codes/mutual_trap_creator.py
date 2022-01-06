import pandas as pd
import numpy as np

list1_start = 10
list1_end = 33
list2_start = 36
list2_end = 59

for i in range(abs(list1_start - list1_end) + 1):
    print(str(i + list1_start) + "-" + str(list2_end - i))

f = open("/Users/student/Desktop/Imperial/year4/MEng/main/handhold1/external.conf", "w")
for i in range(abs(list1_start - list1_end) + 1):
    text = "{\ntype = mutual_trap\nparticle = " + str(list2_end - i) + \
           "\nref_particle = " + str(i + list1_start) + "\nstiff = 1\nr0 = 1.2\n}\n" + \
           "{\ntype = mutual_trap\nparticle = " + str(i + list1_start) + \
           "\nref_particle = " + str(list2_end - i) + "\nstiff = 1\nr0 = 1.2\n}\n"
    f.write(text)

f.close()

f = open("/Users/student/Desktop/Imperial/year4/MEng/main/handhold1/op.txt", "w")
text1 = "{\n\torder_parameter = bond\n\tname = all_native_bonds"
f.write(text1)
for i in range(abs(list1_start - list1_end) + 1):
    text2 = "\n\tpair" + str(i+1) + \
           " = " + str(i + list1_start) + ", " + str(list2_end - i)
    f.write(text2)

text3 = "\n}"
f.write(text3)
f.close()

