import sys
sys.path.append("..")
sys.path.append("../..")
sys.path.append("../../..")

from main.selection.boltzmann_selection import BoltzmannSelection
from main.selection.elite_selection import EliteSelection
from main.selection.rank_selection import RankSelection
from main.selection.roulette_selection import RouletteSelection
from main.selection.softmax_selection import SoftmaxSelection
from main.selection.tournament_selection import TournamentSelection
from main.selection.truncated_selection import TruncatedSelection
from main.mutation import NormalMutation
from main.mutation import UniformMutation
from main.crossing.uniform_cross import UniformCross
from main.crossing.multiple_cross import MultipleCross
from main.pairing.elitist_pairing import ElitistPairing
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

def run(cross, selection, mutation):
    algorithm = Algorithm(
        ind_factory = ReactiveIndividualFactory(), 
        pairing = ElitistPairing(), 
        cross = cross,
        mutation = mutation,
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

def permutation_compare():
    crossing = [UniformCross(p=0.5), MultipleCross(npoints=5)]

    selections = [BoltzmannSelection(tc=10, to=1, k=0.1), EliteSelection(), RankSelection(), \
        RouletteSelection(), SoftmaxSelection(), TournamentSelection(u=0.9), TruncatedSelection(k=7)]
    

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