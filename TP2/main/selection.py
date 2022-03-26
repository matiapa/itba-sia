from typing import List
from fitness import Fitness
from individual import Individual
import numpy as np
from numpy.random import choice

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
        probabilities = [fitness.apply(individual) / max for individual in individuals]
        return choice(individuals, size=len(individuals)//2, replace=False, p=probabilities)

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