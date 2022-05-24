import numpy as np 

x = np.array([1, 2, 3, 4])
np.save("TP3/out/test", x)


t = np.load("TP3/out/test.npy")
print(t)

