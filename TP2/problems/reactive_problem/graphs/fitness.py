import sys
sys.path.append("..")
sys.path.append("../..")
sys.path.append("../../..")

from main.selection.elite_selection import EliteSelection
from main.pairing.elitist_pairing import ElitistPairing
from main.mutation import NormalMutation
from main.crossing.simple_cross import SimpleCross
from main.algorithm import Algorithm
from problems.reactive_problem.individual import ReactiveIndividualFactory
from problems.reactive_problem.fitness import ReactiveFitness

import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool


P = [(_ + 1) / 10 for _ in range(10)]           # Range for mutation probability
S = [(_ + 1) / 100 for _ in range(10)]          # Range for mutation standard deviation

ITERATIONS = 100


fitness = ReactiveFitness()

def run(p, sigma):
    global i

    algorithm = Algorithm(
        ind_factory = ReactiveIndividualFactory(), 
        pairing = ElitistPairing(), 
        cross = SimpleCross(),
        mutation = NormalMutation(p=p, sigma=sigma),
        fitness = fitness,
        selection = EliteSelection(),
        init_pop_size = 10
    )
    iterator = iter(algorithm)

    global_fitnesses = []

    for _ in range(ITERATIONS):
        population = next(iterator)
        max_local_fitness = max([fitness.apply(_) for _ in population])
        global_fitnesses.append( max_local_fitness )

    # print(f"Iteration: {i}")
    i += 1

    return max(global_fitnesses)

def worker(args):
    return [run(args[0], args[1])]

def cartesian(A, B):
    return [(a,b) for a in A for b in B]

def chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

if __name__ == "__main__":
    pool = Pool(8)
    fitnesses = pool.map(worker, cartesian(P, S))
    fitnesses = chunks(fitnesses, len(P))
    pool.close()

    fig, ax = plt.subplots()
    im = ax.imshow(fitnesses)

    ax.set_xticks(np.arange(len(S)), labels=S)
    ax.set_yticks(np.arange(len(P)), labels=P)

    plt.xlabel('Standard deviation (σ)')
    plt.ylabel('Probability of mutation (p)')
    plt.title('Maximum global fitness')

    plt.show()