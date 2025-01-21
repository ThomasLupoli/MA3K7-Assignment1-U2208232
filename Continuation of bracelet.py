import numpy as np

bracelet = np.array([1, 5, 6, 1, 7, 8, 5])

while(bracelet[0] != bracelet[len(bracelet) - 2]) or (bracelet[1] != bracelet[len(bracelet) - 1]):
    n = int(len(bracelet))
    if bracelet[n - 1] + bracelet[n - 2] < 10:
        add = np.array([bracelet[n - 1] + bracelet[n - 2]])
    else:
        add = np.array([bracelet[n - 1] + bracelet[n - 2] - 10])
    bracelet = np.append(bracelet, add)
print(bracelet)
print(len(bracelet) - 2)