from fitness import ReactiveFitness, F, inputs
from individual import ReactiveIndividual, ReactiveIndividualFactory
from typing import List
from main.algorithm import Algorithm
from main.crossing.simple_cross import SimpleCross
from main.mutation import UniformMutation
from main.pairing.elitist_pairing import ElitistPairing
from main.selection.tournament_selection import TournamentSelection
from main.selection.elite_selection import EliteSelection
from main.selection.rank_selection import RankSelection
from main.selection.roulette_selection import RouletteSelection
from main.selection.boltzmann_selection import BoltzmannSelection
from main.selection.truncated_selection import TruncatedSelection
from matplotlib import pyplot as plt
import sys
sys.path.append("..")
sys.path.append("../..")

q_experiments = 5
fitness = ReactiveFitness()

# TournamentSelection(0.6),
selections = [EliteSelection(), RouletteSelection(), 
RankSelection(),  BoltzmannSelection(25, 100, 0.005), TruncatedSelection(10)]

iterators = []
algorithms = []

for i in range(q_experiments):
    algorithms.append(Algorithm(
        ind_factory=ReactiveIndividualFactory(),
        pairing=ElitistPairing(),
        cross=SimpleCross(),
        mutation=UniformMutation(p=0.5, _range=0.1),
        fitness=fitness,
        selection=selections[i],
        init_pop_size=30
    ))
    iterators.append(iter(algorithms[i]))

experiments = []
experiments_avg = []

iterations_per_experiment = 500

for k in range(q_experiments):
    t = 0
    experiments.append([])
    experiments_avg.append([])
    while t < iterations_per_experiment:
        individuals: List[ReactiveIndividual] = next(iterators[k])
        experiments[k].append(min([fitness.error(indi)
                              for indi in individuals]))
        experiments_avg[k].append(sum([fitness.error(indi) 
                            for indi in individuals])/len(individuals))
        t += 1


for i in range(5):
    plt.plot(range(iterations_per_experiment), experiments[i], 'k')
    plt.plot(range(iterations_per_experiment), experiments_avg[i], 'r')
    plt.title('Experiment' + str(i))
    plt.xlabel("Generation")
    plt.ylabel("Error")
    plt.show()
