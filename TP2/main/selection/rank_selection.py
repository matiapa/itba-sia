from main.fitness import Fitness
from main.individual import Individual
from main.selection.selection import Selection
from typing import List

# TODO
class RankSelection(Selection):

    """
    Selects individuals using Rank Method
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        ...