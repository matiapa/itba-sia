from main.fitness import Fitness
from main.individual import Individual
from main.selection.selection import Selection
from typing import List

# TODO
class TruncatedSelection(Selection):

    """
    Selects individuals using Truncated Method
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        ...