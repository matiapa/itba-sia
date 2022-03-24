from typing import List
from fitness import Fitness

from individual import Individual


class StopCriteria:

    """
    Returns whether the algorithm should continue running or not
    based on the current population genes and the fitness function
    """
    def should_stop(self, population: List[Individual], fitness: Fitness) -> bool:
        raise NotImplementedError