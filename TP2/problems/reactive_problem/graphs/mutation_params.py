import sys
sys.path.append("..")
sys.path.append("../..")
sys.path.append("../../..")

from main.selection.elite_selection import EliteSelection
from main.pairing.elitist_pairing import ElitistPairing
from main.mutation import NormalMutation, UniformMutation
from main.crossing.simple_cross import SimpleCross
from main.algorithm import Algorithm
from problems.reactive_problem.individual import ReactiveIndividualFactory
from problems.reactive_problem.fitness import ReactiveFitness

import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Pool, cpu_count


P = [(_ + 1) / 10 for _ in range(10)]           # Range for mutation probability
S = [(_ + 1) / 100 for _ in range(10)]          # Range for normal mutation deviation
R = [(_ + 1) / 100 for _ in range(10)]          # Range for uniform mutation range

ITERATIONS = 100


fitness = ReactiveFitness()

def run(mutation):
    algorithm = Algorithm(
        ind_factory = ReactiveIndividualFactory(), 
        pairing = ElitistPairing(), 
        cross = SimpleCross(),
        mutation = mutation,
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

    return max(max_local_fitnesses)

def normal_worker(args):
    mutation = NormalMutation(p=args[0], sigma=args[1])
    return [run(mutation)]

def uniform_worker(args):
    mutation = UniformMutation(p=args[0], _range=args[1])
    return [run(mutation)]

def cartesian(A, B):
    return [(a,b) for a in A for b in B]

def chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

if __name__ == "__main__":
    pool = Pool(cpu_count())
    # fitnesses = pool.map(normal_worker, cartesian(P, S))
    fitnesses = pool.map(uniform_worker, cartesian(P, R))
    fitnesses = chunks(fitnesses, len(P))
    pool.close()

    fig, ax = plt.subplots()
    im = ax.imshow(fitnesses)

    ax.set_xticks(np.arange(len(S)), labels=S)
    ax.set_yticks(np.arange(len(P)), labels=P)

    # plt.xlabel('Standard deviation (σ)')
    plt.xlabel('Range (r)')
    plt.ylabel('Probability of mutation (p)')
    plt.title('Maximum global fitness')

    plt.show()