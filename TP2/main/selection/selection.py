from main.fitness import Fitness
from main.individual import Individual
from typing import List, Set

class Selection:

    def __str__(self):
        raise NotImplementedError()

    """
    Selects half of the individuals for surviving to the next generation
    """
    def apply(self, individuals: Set[Individual], fitness: Fitness) -> Set[Individual]:
        raise NotImplementedError()