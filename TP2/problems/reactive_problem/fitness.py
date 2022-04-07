from math import exp
import sys
sys.path.append("..")
sys.path.append("../..")
from main.fitness import Fitness
from problems.reactive_problem.individual import ReactiveIndividual

inputs = {
    "xi": [[4.4793, -4.0765, -4.0765], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.8830]],
    "dseta": [0, 1, 1],
}

def g(x):
    return exp(x)/(1+exp(x))


def y(j, w, w_0, xi):
    x = sum((w[j-1][k-1]*xi[k-1]) for k in range(1, 4)) - w_0[j-1]
    return g(x)


def F(W, w, w_0, xi):
    x = sum((W[j]*y(j, w, w_0, xi)) for j in range(1, 3)) - W[0]
    return g(x)

def E(W, w, w_0):
    xi = inputs["xi"]
    dseta = inputs["dseta"]
    return sum(((dseta[u-1]-F(W, w, w_0, xi[u-1]))**2) for u in range(1, 4))

# TODO: discutir en filminas
class ReactiveFitness(Fitness):
    def apply(self, i: ReactiveIndividual):
        return 3-E(i.W, i.w, i.w_0)

    def error(self, i: ReactiveIndividual):
        return E(i.W, i.w, i.w_0)