import csv
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

columns = defaultdict(list) # each value in each column is appended to a list

arr = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
with open('mse.txt') as f:
    reader = csv.reader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        r = row[0]
        print(r)
        count = -1
        temp = ''
        for i in range(len(r)):
            if r[i] == ' ' or r[i] == '' or r[i] == '\n':
                count += 1
                arr[count].append(float(temp))
                temp = ''
            else:
                temp += r[i]

l = len(arr)
while [0] in arr:
    arr.remove([0])

for i in range (len(arr)):
    l = len(arr[i])
    arr[i] = sum(arr[i])/l

num_gen = []
for i in range(len(arr)):
    num_gen.append(i+1)
fig, ax = plt.subplots()
ax.plot(num_gen, arr)
plt.show()

print(arr)
