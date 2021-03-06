import sys
sys.path.append("..")
sys.path.append("../..")

from problems.bag_problem.fitness import BagFitness
from problems.bag_problem.individual import BagIndividualFactory, BagIndividual

from main.algorithm import Algorithm
from main.crossing.uniform_cross import UniformCross
from main.individual import Individual
from main.mutation import BinaryMutation
from main.pairing.elitist_pairing import ElitistPairing
from main.selection.roulette_selection import RouletteSelection
from main.selection.elite_selection import EliteSelection
from main.selection.boltzmann_selection import BoltzmannSelection

from typing import List
from numpy import argmax


def print_details(n : int):
    individual = individuals[n]
    
    weight_sum = 0
    for i in range(0, len(individual.genes)):
        if individual.genes[i] == 1:
            weight_sum += BagFitness.weights[i]

    print(f'Individual {n}')
    print(f'> Genes: {individual.genes}')
    print(f'> Fitness: {scores[n]}')
    print(f'> Weight: {weight_sum}')


fitness = BagFitness()
BagIndividual.bag_genome_size = 100

# BoltzmannSelection(tc=0, to=100, k=0.1)

algorithm = Algorithm(
    ind_factory = BagIndividualFactory(), pairing = ElitistPairing(), cross = UniformCross(p=0.5),
    mutation = BinaryMutation(p=0.1), fitness = fitness, selection = EliteSelection(),
    init_pop_size = 100
)
iterator = iter(algorithm)

generation = 0
individuals : List[BagIndividual] = []

while generation < 5000:
    individuals : List[BagIndividual] = list(next(iterator))

    scores = [fitness.apply(i) for i in individuals]
    i_max = argmax(scores)
    
    # for i in individuals:
    #     print(i, end=' ')
    # print('')

    # print(f'{generation}: {individuals[i_max].genes}')
    print(f'{generation}: {round(scores[i_max], 9)}')

    generation += 1

scores = [fitness.apply(i) for i in individuals]
i_max = argmax(scores)

print("Best genome:")
print(individuals[i_max].genes)