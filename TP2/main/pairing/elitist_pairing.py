from functools import reduce
from math import floor
from typing import List, Tuple
from main.fitness import Fitness
from main.individual import Individual
from main.pairing.pairing import Pairing
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