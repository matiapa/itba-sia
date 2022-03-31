import sys
sys.path.append("..")
sys.path.append("../..")

from matplotlib import pyplot as plt
from main.selection.truncated_selection import TruncatedSelection
from main.selection.boltzmann_selection import BoltzmannSelection
from main.selection.roulette_selection import RouletteSelection
from main.selection.rank_selection import RankSelection
from main.selection.elite_selection import EliteSelection
from main.pairing.elitist_pairing import ElitistPairing
from main.mutation import UniformMutation
from main.crossing.simple_cross import SimpleCross
from main.algorithm import Algorithm
from typing import List
from individual import ReactiveIndividual, ReactiveIndividualFactory
from fitness import ReactiveFitness, F, inputs

fitness = ReactiveFitness()

algorithm = Algorithm(
    ind_factory=ReactiveIndividualFactory(), 
    pairing=ElitistPairing(), 
    cross=SimpleCross(),
    mutation=UniformMutation(p=0.5, _range=0.1), 
    fitness=fitness, 
    selection=EliteSelection(),
    init_pop_size=10
)
iterator = iter(algorithm)

experiments = []

iterations_per_experiment = 500
q_experiments = 1 
for k in range(q_experiments): 
    t = 0
    experiments.append([])
    while t < iterations_per_experiment:
        individuals: List[ReactiveIndividual] = next(iterator)
        experiments[k].append(max([fitness.apply(indi) for indi in individuals]))
        t += 1

plt.plot(range(iterations_per_experiment), experiments[0], 'k') 
plt.show()



