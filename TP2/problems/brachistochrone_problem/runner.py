import sys
sys.path.append("..")
sys.path.append("../..")

from problems.brachistochrone_problem.fitness import BrachistochroneFitness
from problems.brachistochrone_problem.individual import BrachistochroneIndividual, BrachistochroneIndividualFactory
from problems.brachistochrone_problem.plotter import plot_individual

from main.algorithm import Algorithm
from main.crossing.uniform_cross import SimpleCross
from main.individual import Individual
from main.mutation import NormalMutation
from main.pairing.elitist_pairing import ElitistPairing
from main.selection.roulette_selection import RouletteSelection
from main.selection.elite_selection import EliteSelection
from main.stop_criteria import IterationStopCriteria
from main.selection.boltzmann_selection import BoltzmannSelection

from typing import List
from numpy import argmax



fitness = BrachistochroneFitness()
BrachistochroneIndividual.q_control_points = 25
BrachistochroneIndividual.angle_limit = 0.1


algorithm = Algorithm(
    ind_factory = BrachistochroneIndividualFactory(), 
    pairing = ElitistPairing(), 
    cross = SimpleCross(p=0),
    mutation = NormalMutation(p=1, sigma=0.1), 
    fitness = fitness, 
    selection = RouletteSelection(),
    init_pop_size = 100
)
iterator = iter(algorithm)

generation = 0
print("OKEY")
best = None
best_fit = 0.09
while generation < 500:
    # print('STARTING')
    individuals : List[BrachistochroneIndividual] = list(next(iterator))

    scores = [fitness.apply(i) for i in individuals]
    i_max = argmax(scores)

    # print(generation, individuals[i_max])

    
    # # for i in individuals:
    # #     print(i, end=' ')
    # # print('')


    # # print(f'{generation}: {individuals[i_max].genes}')
    # # print(f'{generation}: {round(scores[i_max], 9)}')
    # print(scores)
    # if (max(scores) > 1): 
    #     plot_individual(individuals[i_max])
    if max(scores) > best_fit: 
        best_fit = max(scores)
        best = individuals[i_max]

    generation += 1

print(best_fit)
plot_individual(best)


