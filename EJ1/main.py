from functions import E
import numpy as np
from datetime import datetime
from scipy.optimize import minimize
from autograd.misc.optimizers import adam
import numdifftools as nd


def start_timer():
    return datetime.now()

def end_timer(time):
    return datetime.now() - time

def print_arg(x):
    print('Valor del argumento')
    print('W: [ {0:2.5f} , {1:2.5f} , {2:2.5f} ]'.format(x[0], x[1], x[2]))
    print('w: [ {0:2.5f} , {1:2.5f} , {2:2.5f} ] , [ {3:2.5f} , {4:2.5f} , {5:2.5f} ]'.format(x[3], x[4], x[5], x[6], x[7], x[8]))
    print('w_0: [ {0:2.5f} , {1:2.5f} ]'.format(x[9], x[10]))

x = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

time = start_timer()
sgd = minimize(E, x, method="L-BFGS-B")
print("Gradiente descendente")
print_arg(sgd.x)
print("Error: ", sgd.fun)
print('Time: ', end_timer(time), '\n')

time = start_timer()
cg = minimize(E, x, method="CG")
print('Gradientes conjugados')
print_arg(cg.x)
print("Error: ", cg.fun)
print('Time: ', end_timer(time))

adam_m = adam(nd.Gradient(E), x)