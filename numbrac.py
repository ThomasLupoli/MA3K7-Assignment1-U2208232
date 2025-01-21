import numpy as np
import matplotlib.pyplot as plt


def creator(bracelet, mod=10):
    while (bracelet[0] != bracelet[-2]) or (bracelet[1] != bracelet[-1]) or len(bracelet) < 3:
        add = np.array((bracelet[-1] + bracelet[-2]) % mod)
        bracelet = np.append(bracelet, add)
    return bracelet[0:-2]


def number_of_bracelets(mod):
    list = []
    count = 0
    for i in range(mod):
        for j in range(mod):
            list.append(len(creator(np.array([i, j]), mod)))
    for k in range(len(list)):
        if not(list[k] in list[0:k]):
            total = list.count(list[k])
            count += total / list[k]
    return int(count)


print(number_of_bracelets(105))
