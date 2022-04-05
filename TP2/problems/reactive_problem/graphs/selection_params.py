import sys
sys.path.append("..")
sys.path.append("../..")
sys.path.append("../../..")

from main.selection.boltzmann_selection import BoltzmannSelection
from main.selection.tournament_selection import TournamentSelection
from main.selection.truncated_selection import TruncatedSelection
from main.pairing.elitist_pairing import ElitistPairing
from main.mutation import NormalMutation
from main.crossing.simple_cross import SimpleCross
from main.algorithm import Algorithm
from problems.reactive_problem.individual import ReactiveIndividualFactory
from problems.reactive_problem.fitness import ReactiveFitness

import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Pool, cpu_count


t0 = 10
TC = np.arange(0.1, 1, 0.1)           # Range for final temperature
K = np.arange(0.01, 0.1, 0.01)        # Range for decayment ration
U = np.arange(0.50, 1, 0.05)          # Range for probability in tournament selection

ITERATIONS = 100
POP_SIZE = 10

fitness = ReactiveFitness()

def run(selection):
    algorithm = Algorithm(
        ind_factory = ReactiveIndividualFactory(), 
        pairing = ElitistPairing(), 
        cross = SimpleCross(),
        mutation = NormalMutation(p=1, sigma=0.1),
        fitness = fitness,
        selection = selection,
        init_pop_size = POP_SIZE
    )
    iterator = iter(algorithm)

    max_local_fitnesses = []

    for _ in range(ITERATIONS):
        population = next(iterator)
        max_local_fitness = max([fitness.apply(_) for _ in population])
        max_local_fitnesses.append( max_local_fitness )

    return max(max_local_fitnesses)

def boltzmann_worker(args):
    global t0
    selection = BoltzmannSelection(tc=args[0], to=t0, k=args[1])
    return [run(selection)]

def cartesian(A, B):
    return [(a,b) for a in A for b in B]

def chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def boltzmann_graph():
    pool = Pool(cpu_count())
    fitnesses = pool.map(boltzmann_worker, cartesian(TC, K))
    fitnesses = chunks(fitnesses, len(TC))
    pool.close()

    _, ax = plt.subplots()
    ax.imshow(fitnesses)

    ax.set_xticks(np.arange(len(K)), labels=K)
    ax.set_yticks(np.arange(len(TC)), labels=TC)

    plt.xlabel('Decayment ratio (k)')
    plt.ylabel('Final temperature (Tc)')
    plt.title('Maximum global fitness (Boltzmann, t0=10)')

    plt.show()

def tournament_graph():
    fitnesses = [run(TournamentSelection(u)) for u in U]

    plt.plot(U, fitnesses)

    plt.xlabel('Probability (u)')
    plt.ylabel('Maximum global fitness')
    plt.title('Tournament selection')

    plt.grid()
    plt.show()

def truncated_graph():
    fitnesses = [run(TruncatedSelection(k)) for k in range(POP_SIZE)]

    plt.plot([k for k in range(POP_SIZE)], fitnesses)

    plt.xlabel('Truncate value (k)')
    plt.ylabel('Maximum global fitness')
    plt.title('Truncated selection')

    plt.grid()
    plt.show()

if __name__ == '__main__':
    truncated_graph()