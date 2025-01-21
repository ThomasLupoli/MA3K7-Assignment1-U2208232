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

number = 120
mods = np.arange(number) + 1
unique_bracelets = []

for i in range(number):
    unique_bracelets.append(number_of_bracelets(i + 1))

plt.plot(mods, unique_bracelets, "ro")
plt.xlabel("Modulo")
plt.ylabel("Number of unique bracelets")
z = np.polyfit(mods, unique_bracelets, 1)
p = np.poly1d(z)
plt.plot(mods,p(mods),"b--")
plt.title("The number of bracelets for each modulo")
plt.show()
