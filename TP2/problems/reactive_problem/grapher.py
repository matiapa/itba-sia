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
from main.selection.selection import Selection
from matplotlib import pyplot as plt
import sys
sys.path.append("..")
sys.path.append("../..")

fitness = ReactiveFitness()

# TournamentSelection(0.6),
selections = [TournamentSelection(0.6), EliteSelection(), RouletteSelection(), 
RankSelection(),  BoltzmannSelection(25, 100, 0.005), TruncatedSelection(5)]

q_experiments = len(selections)

def selection_str(selection: Selection):
    return str(selection)

iterators = []
algorithms = []

for i in range(len(selections)):
    algorithms.append(Algorithm(
        ind_factory=ReactiveIndividualFactory(),
        pairing=ElitistPairing(),
        cross=SimpleCross(),
        mutation=UniformMutation(p=0.5, _range=0.1),
        fitness=fitness,
        selection=selections[i],
        init_pop_size=10,
        replace=False
    ))
    iterators.append(iter(algorithms[i]))

experiments = []
experiments_avg = []
experiments_fitness = []
iterations_per_experiment = 500

for k in range(q_experiments):
    t = 0
    experiments.append([])
    experiments_avg.append([])
    experiments_fitness.append([])
    while t < iterations_per_experiment:
        individuals: List[ReactiveIndividual] = next(iterators[k])
        experiments[k].append(min([fitness.error(indi)
                              for indi in individuals]))
        experiments_fitness[k].append(max([fitness.apply(indi) for indi in individuals]))
        experiments_avg[k].append(sum([fitness.error(indi) 
                            for indi in individuals])/len(individuals))
        t += 1


for i in range(q_experiments):
    plt.plot(range(iterations_per_experiment), experiments[i], label="Error minimo")
    plt.plot(range(iterations_per_experiment), experiments_avg[i], label="Error promedio")
    plt.figtext(.8, .8, str(max(experiments_fitness[k])))
    plt.suptitle('Selection: ' + selection_str(selections[i]))
    plt.title('Title')
    plt.legend()
    plt.xlabel("Generation")
    plt.ylabel("Error")
    plt.show()


# Las 6 muestras de Selecciones con 100 individuos y 500 generaciones
# 1 usando Roulette pero variando la cantidad de individuos (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# Con trazo muy fino, mostrar la convergencia con valores distintos de k (Boltzmann)
