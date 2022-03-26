from main.fitness import Fitness
from main.individual import Individual

from typing import List, Tuple

class Pairing:

    """
    Makes pairs of individuals to be crossed based on their fitness or a random criteria.
    If population size is N, it must return exactly N/2 pairs.
    """
    def apply(self, population: List[Individual], fitness: Fitness) -> List[Tuple[Individual, Individual]]:
        raise NotImplementedError