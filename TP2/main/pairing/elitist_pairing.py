from main.fitness import Fitness
from main.individual import Individual
from main.pairing.pairing import Pairing

from functools import reduce
from math import floor
from typing import List, Tuple
from numpy.random import choice

class ElitistPairing(Pairing):

    """
    Chooses pairs of individuals randomly, but prioritizing those with higher fitness score
    """

    def apply(self, population: List[Individual], fitness: Fitness) -> List[Tuple[Individual, Individual]]:

        fitness_sum = sum(fitness.apply(individual) for individual in population)
        
        probabilities = [fitness.apply(individual) / fitness_sum for individual in population]

        pairs : List[Tuple[Individual, Individual]] = []

        for _ in range(0, len(population) // 2):
            pair = choice(population, size=2, replace=False, p=probabilities)
            pairs.append((pair[0], pair[1]))

        return pairs

    # The following code is equivalent to the previous one, numpy automatically updates the
    # weights of the elements after taking one out by using: w = [x / sum(w) for x in w]
    #
    # def __choose(self, fitness, population):
    #     fitness_sum = sum(fitness.apply(individual) for individual in population)
    #     probabilities = [fitness.apply(individual) / fitness_sum for individual in population]
    #     return choice(population, size=1, p=probabilities)[0]
    #
    # def apply(self, population: List[Individual], fitness: Fitness) -> List[Tuple[Individual, Individual]]:
    #     pairs : List[Tuple[Individual, Individual]] = []
    #     for _ in range(0, len(population) // 2):
    #         i1 = self.__choose(fitness, population)
    #         population.remove(i1)
    #         i2 = self.__choose(fitness, population)
    #         population.append(i1)
    #         pairs.append((i1, i2))