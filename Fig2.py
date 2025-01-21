import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive
from IPython.display import display


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
    return list

mods = 50
x = np.asarray(number_of_bracelets(mods))
x = np.reshape(x, [mods, mods])

#im = plt.imshow(x, cmap='terrain')
im = plt.imshow(x, cmap='Spectral')
plt.colorbar(im, label="Bracelet Lengths")
plt.title("Bracelet Lengths from starting pair (mod 50)")
plt.xlabel("Start Value 2")
plt.ylabel("Start Value 1")
plt.show()


