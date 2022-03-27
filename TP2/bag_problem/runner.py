import sys
sys.path.append("..")

from fitness import BagFitness
from individual import BagIndividualFactory, BagIndividual

from main.algorithm import Algorithm
from main.crossing.uniform_cross import SimpleCross
from main.individual import Individual
from main.mutation import BinaryMutation
from main.pairing.elitist_pairing import ElitistPairing
from main.selection.roulette_selection import RouletteSelection
from main.selection.elite_selection import EliteSelection
from main.stop_criteria import IterationStopCriteria

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

algorithm = Algorithm(
    ind_factory = BagIndividualFactory(), pairing = ElitistPairing(), cross = SimpleCross(p=0.5),
    mutation = BinaryMutation(p=0.05),    fitness = fitness,          selection = EliteSelection(),
    init_pop_size = 100
)
iterator = iter(algorithm)

generation = 0
while generation < 5:
    individuals : List[BagIndividual] = next(iterator)

    scores = [fitness.apply(i) for i in individuals]
    i_max = argmax(scores)
    
    print(f'{generation}: {round(scores[i_max], 6)}')

    generation += 1