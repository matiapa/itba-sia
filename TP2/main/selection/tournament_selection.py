from main.selection.selection import Selection
from main.fitness import Fitness
from main.individual import Individual
from typing import List

# TODO
class TournamentSelection(Selection):

    """
    Selects individuals using Tournament Method
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        ...