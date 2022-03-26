from main.fitness import Fitness
from main.individual import Individual

from typing import List
import numpy as np

class Selection:

    """
    Selects half of the individuals for surviving to the next generation
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        raise NotImplementedError()

class EliteSelection(Selection):

    """
    Selects the best individuals for each generation
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        sorted(individuals, key=fitness.apply, reverse=True)
        return individuals[:len(individuals)//2]

# TODO implement
class StochasticSelection(Selection):

    """
    Selects individuals mixing aptitude and randomness
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        ...
        # sorted(individuals, key=fitness.apply)
        # return individuals[:len(individuals)//2]

class RouletteSelection(Selection):

    """
    Selects individuals based on their relative fitness
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        max = sum(fitness.apply(individual) for individual in individuals)
        r = np.random.uniform(0, 1)
        q_j, j = fitness.apply(individuals[0]) / max, 0
        q_j_next = q_j
        for individual in individuals[1:]:
            q_j = q_j_next if j > 0 else q_j
            j+=1
            q_j_next += fitness.apply(individual) / max
            if q_j < r <= q_j_next:
                return individuals[j]

        # TODO: ver que devolver si no hay ningun individuo que cumpla la condicion
        return individuals[-1]

# TODO
class RankSelection(Selection):

    """
    Selects individuals using Rank Method
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        ...

# TODO
class TournamentSelection(Selection):

    """
    Selects individuals using Tournament Method
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        ...

# TODO
class BoltzmannSelection(Selection):

    """
    Selects individuals using Boltzmann Method
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        ...

# TODO
class TruncatedSelection(Selection):

    """
    Selects individuals using Truncated Method
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        ...