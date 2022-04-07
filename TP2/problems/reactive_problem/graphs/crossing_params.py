import sys
sys.path.append("..")
sys.path.append("../..")
sys.path.append("../../..")

from main.selection.elite_selection import EliteSelection
from main.pairing.elitist_pairing import ElitistPairing
from main.mutation import NormalMutation
from main.crossing.uniform_cross import UniformCross
from main.crossing.simple_cross import MultipleCross
from main.algorithm import Algorithm
from problems.reactive_problem.individual import ReactiveIndividualFactory
from problems.reactive_problem.fitness import ReactiveFitness

import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Pool, cpu_count


N = np.arange(1, 10, 1)           # Range of number of points for multiple cross
P = np.arange(0, 1, 0.1)          # Range of probabilities for uniform cross

ITERATIONS = 100


fitness = ReactiveFitness()

def run(cross):
    algorithm = Algorithm(
        ind_factory = ReactiveIndividualFactory(), 
        pairing = ElitistPairing(), 
        cross = cross,
        mutation = NormalMutation(p=1, sigma=0.1),
        fitness = fitness,
        selection = EliteSelection(),
        init_pop_size = 10
    )
    iterator = iter(algorithm)

    max_local_fitnesses = []

    for _ in range(ITERATIONS):
        population = next(iterator)
        max_local_fitness = max([fitness.apply(_) for _ in population])
        max_local_fitnesses.append( max_local_fitness )

    return max_local_fitnesses

def multiple_graph():
    fitnesses = [run(MultipleCross(npoints=n)) for n in N]

    for i in range(len(fitnesses)):
        n_fitnesses = fitnesses[i]
        n = N[i]
        plt.plot(range(len(n_fitnesses)), n_fitnesses, label=f'n={n}')

    plt.xlabel('Generation')
    plt.ylabel('Maximum fitness')
    plt.title('Multiple cross')

    plt.legend()
    plt.grid()
    plt.show()

def uniform_graph():
    fitnesses = [run(UniformCross(p)) for p in P]

    for i in range(len(fitnesses)):
        p_fitnesses = fitnesses[i]
        p = P[i]
        plt.plot(range(len(p_fitnesses)), p_fitnesses, label=f'p={p}')

    plt.xlabel('Generation')
    plt.ylabel('Maximum fitness')
    plt.title('Uniform cross')

    plt.legend()
    plt.grid()
    plt.show()

multiple_graph()