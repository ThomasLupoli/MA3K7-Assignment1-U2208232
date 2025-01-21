import numpy as np


def creator(bracelet):
    while (bracelet[0] != bracelet[-2]) or (bracelet[1] != bracelet[-1]) or len(bracelet) < 3:
        add = np.array((bracelet[-1] + bracelet[-2]) % 10)
        bracelet = np.append(bracelet, add)
    return bracelet


counter60 = 0
counter20 = 0
counter12 = 0
counter4 = 0
counter3 = 0
counter1 = 0

for i in range(10):
    for j in range(10):
        if len(creator(np.array([i, j]))) - 2 == 60:
            counter60 += 1
        elif len(creator(np.array([i, j]))) - 2 == 20:
            counter20 += 1
        elif len(creator(np.array([i, j]))) - 2 == 12:
            counter12 += 1
        elif len(creator(np.array([i, j]))) - 2 == 4:
            counter4 += 1
        elif len(creator(np.array([i, j]))) - 2 == 3:
            counter3 += 1
        elif len(creator(np.array([i, j]))) - 2 == 1:
            counter1 += 1
        else:
            print(len(creator(np.array([i, j]))) - 2)

print("number of length 60:", counter60)
print("number of length 20:", counter20)
print("number of length 12:", counter12)
print("number of length 4:", counter4)
print("number of length 3:", counter3)
print("number of length 1:", counter1)
