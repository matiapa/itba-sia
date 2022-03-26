from main.fitness import Fitness
from main.individual import Individual
from main.selection.selection import Selection
from typing import List

# TODO
class BoltzmannSelection(Selection):

    """
    Selects individuals using Boltzmann Method
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        ...