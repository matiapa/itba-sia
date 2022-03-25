from functools import reduce
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
        
        fitness_sum = reduce(lambda f1, f2: f1 + f2, map(lambda i : fitness.apply(i), population), 0)

        probabilities = map(lambda i : fitness.apply(i) / fitness_sum, population)

        pairs : List[Tuple[Individual, Individual]] = []

        for _ in range(0, len(population) / 2):
            pair = choice(population, size=2, replace=False, p=probabilities)
            pairs.append((pair[0], pair[1]))

        return pairs