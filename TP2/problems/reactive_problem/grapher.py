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
import numpy as np
import sys
sys.path.append("..")
sys.path.append("../..")

fitness = ReactiveFitness()

# TournamentSelection(0.6),
selections = [EliteSelection(), RouletteSelection(),
              RankSelection(),  TournamentSelection(0.6), 
              BoltzmannSelection(25, 100, 0.005), TruncatedSelection(5)]

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
        init_pop_size=100,
        replace=False
    ))
    iterators.append(iter(algorithms[i]))

experiments_err = []
experiments_avg = []
experiments_fitness = []
iterations_per_experiment = 500
optimos = []            # por cada experimento, guarda el optimo de cada generacion [k][t]
optimo = []             # el mejor de cada experimento

for k in range(q_experiments):
    t = 0
    experiments_err.append([])
    experiments_avg.append([])
    experiments_fitness.append([])
    optimos.append([])
    while t < iterations_per_experiment:
        individuals: List[ReactiveIndividual] = next(iterators[k])
        experiments_err[k].append(min([fitness.error(indi)
                                       for indi in individuals]))
        experiments_fitness[k].append(
            max([fitness.apply(indi) for indi in individuals]))
        experiments_avg[k].append(sum([fitness.error(indi)
                                       for indi in individuals])/len(individuals))
        max_fitness = np.argmax([fitness.apply(indi) for indi in individuals])
        optimos[k].append(list(individuals)[max_fitness])
        t += 1

    print(len(optimos[k]))
    print(len([fitness.apply(indi) for indi in optimos[k]]))

    optimo.append(optimos[k][np.argmax([fitness.apply(indi) for indi in optimos[k]])])

for i in range(q_experiments):
    plt.plot(range(iterations_per_experiment),
             experiments_err[i], label="Error minimo")
    plt.plot(range(iterations_per_experiment),
             experiments_avg[i], label="Error promedio")
    plt.suptitle('Selección: ' + selection_str(selections[i]))
    plt.figtext(.25, .75, str(algorithms[i]), fontsize='small')
    # plt.title("Individuo óptimo: " + str(optimo[i]))
    plt.figtext(.6, .6, 'Óptimo:' + '\n' + str(optimo[i]) + '\n' + '\n' + 'F(óptimo): ' + '\n' + str(max(experiments_fitness[i])) + '\n' + ' E(óptimo):' + '\n' + str(min(experiments_err[i])), fontsize='small')
    plt.xlabel("Generation")
    plt.ylabel("Error")
    plt.show()


# Las 6 muestras de Selecciones con 100 individuos y 500 generaciones
# 1 usando Roulette pero variando la cantidad de individuos (10, 30, 40, 50, 60, 70, 80, 90, 100)
# Con trazo muy fino, mostrar la convergencia con valores distintos de k (Boltzmann)
