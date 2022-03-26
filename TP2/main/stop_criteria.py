from main.fitness import Fitness
from main.individual import Individual

from typing import List

class StopCriteria:

    """
    Returns whether the algorithm should continue running or not
    based on the current population genes and the fitness function
    """
    def should_stop(self, population: List[Individual], fitness: Fitness) -> bool:
        raise NotImplementedError