from functions import E
import numpy as np
from datetime import datetime
from scipy.optimize import minimize

def start_timer():
    return datetime.now()

def end_timer(time):
    return datetime.now() - time

x = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

time = start_timer()
cg = minimize(E, x, method="CG")
print('Gradientes conjugados', cg)
print('Time: ', end_timer(time))

time = start_timer()
sgd = minimize(E, x, method="L-BFGS-B")
print("Gradiente descendente", sgd)
print('Time: ', end_timer(time))