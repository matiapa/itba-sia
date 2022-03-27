from main.fitness import Fitness
from main.individual import Individual

from typing import List

class StopCriteria:

    """
    Returns whether the algorithm should continue running or not
    based on the current population genes and the fitness function
    """
    def should_stop(self, population: List[Individual], fitness: Fitness, generation: int) -> bool:
        raise NotImplementedError

class IterationStopCriteria(StopCriteria):

    n: int

    def __init__(self, n: int) -> None:
        self.n = n

    def should_stop(self, population: List[Individual], fitness: Fitness, generation: int) -> bool:
        return generation > self.n