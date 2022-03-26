from main.fitness import Fitness
from main.individual import Individual
from main.selection.selection import Selection
from typing import List

class EliteSelection(Selection):

    """
    Selects the best individuals for each generation
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        sorted(individuals, key=fitness.apply, reverse=True)
        return individuals[:len(individuals)//2]