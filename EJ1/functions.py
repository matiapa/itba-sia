import numpy as np
from types import MethodType
from math import exp

xi1 = np.array([4.4793, -4.0765, -4.0765], dtype=float)
xi2 = np.array([-4.1793, -4.9218, 1.7664], dtype=float)
xi3 = np.array([-3.9429, -0.7689, 4.8830], dtype=float)
xi = np.array([xi1, xi2, xi3], dtype=object)

zeta = np.array([0., 1., 1.])

def g(x):
    return exp(x) / (1 + exp(x))

def F(x, xi):
    return g(x[1] * g(x[3] * xi[0] + x[4] * xi[1] + x[5] * xi[2] - x[9])
             + x[2] * g(x[6] * xi[0] + x[7] * xi[1] + x[8] * xi[2] - x[10])
             - x[0])

def E(x):
    return sum((np.float_power((zeta[i] - F(x, xi[i])), 2)) for i in range(3))