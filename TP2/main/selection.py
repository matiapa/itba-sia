from typing import List
from fitness import Fitness
from individual import Individual

class Selection:

    """
    Selects half of the individuals for surviving to the next generation
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        raise NotImplementedError()