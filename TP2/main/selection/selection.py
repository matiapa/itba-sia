from main.fitness import Fitness
from main.individual import Individual
from typing import List

class Selection:

    """
    Selects half of the individuals for surviving to the next generation
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        raise NotImplementedError()