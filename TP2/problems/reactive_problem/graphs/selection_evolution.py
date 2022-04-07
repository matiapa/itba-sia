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
from main.crossing.uniform_cross import UniformCross
from main.pairing.elitist_pairing import ElitistPairing
from main.algorithm import Algorithm

from problems.reactive_problem.individual import ReactiveIndividualFactory
from problems.reactive_problem.fitness import ReactiveFitness

import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Pool, cpu_count

ITERATIONS = 500

fitness = ReactiveFitness()

def run(selection):
    algorithm = Algorithm(
        ind_factory = ReactiveIndividualFactory(), 
        pairing = ElitistPairing(), 
        cross = UniformCross(p=0.9),
        mutation = NormalMutation(p=1, sigma=0.1),
        fitness = fitness,
        selection = selection,
        init_pop_size = 100
    )
    iterator = iter(algorithm)

    max_local_fitnesses = []

    for _ in range(ITERATIONS):
        population = next(iterator)
        max_local_fitness = max([fitness.apply(_) for _ in population])
        max_local_fitnesses.append( max_local_fitness )

    return max_local_fitnesses

def graph():
    selections = [
        BoltzmannSelection(tc=10, to=1, k=0.1), EliteSelection(), RankSelection(), RouletteSelection(),
        SoftmaxSelection(), TournamentSelection(u=0.7), TruncatedSelection(k=7)
    ]

    for selection in selections:
        fitnesses = run(selection)
        plt.plot(range(len(fitnesses)), fitnesses, label=f'{selection}')
        print(selection)
    
    plt.xlabel('Generation')
    plt.ylabel('Max fitness')
    plt.legend()
    plt.show()

graph()