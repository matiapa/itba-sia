import sys
sys.path.append("..")
sys.path.append("../..")
import numpy as np 
from problems.brachistochrone_problem.fitness import BrachistochroneFitness
from problems.brachistochrone_problem.individual import BrachistochroneIndividual, BrachistochroneIndividualFactory
from problems.brachistochrone_problem.plotter import plot_individual

from main.algorithm import Algorithm
from main.crossing.uniform_cross import UniformCross
from main.individual import Individual
from main.mutation import NormalMutation
from main.pairing.elitist_pairing import ElitistPairing
from main.selection.roulette_selection import RouletteSelection
from main.selection.elite_selection import EliteSelection
from main.selection.boltzmann_selection import BoltzmannSelection

from typing import List
from numpy import argmax



fitness = BrachistochroneFitness()
BrachistochroneIndividual.q_control_points = 25
BrachistochroneIndividual.angle_limit = 0.1


algorithm = Algorithm(
    ind_factory = BrachistochroneIndividualFactory(), 
    pairing = ElitistPairing(), 
    cross = UniformCross(p=0),
    mutation = NormalMutation(p=1, sigma=0.1), 
    fitness = fitness, 
    selection = EliteSelection(),
    init_pop_size = BrachistochroneIndividual.q_control_points*10, 
    replace = True
)

iterator = iter(algorithm)

# generation = 0
# best = None
# best_fit = 0.09
# while generation < 1000000:
#     r = BrachistochroneIndividual(None)
#     random_fitness = fitness.apply(r)
#     if  random_fitness > best_fit: 
#         best = r
#         best_fit = random_fitness
#         print(best_fit)

#     generation += 1
t = 0
iterly = iter(algorithm)
time = np.infty 
best_individual = None 
best_fitness = -np.infty 

while t < 1000:
    print(t)
    individuals: List[BrachistochroneIndividual] = next(iterly)
    for x in individuals: 
        fit = fitness.apply(x)
        if fit > best_fitness: 
            best_fitness = fit 
            best_individual = x
    t += 1 


# print()
plot_individual(best_individual)


