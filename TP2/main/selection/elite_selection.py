from main.fitness import Fitness
from main.individual import Individual
from main.selection.selection import Selection
from typing import Set

class EliteSelection(Selection):

    def __str__(self):
        return "Elite"
        
    """
    Selects the best individuals for each generation
    """
    def apply(self, individuals: Set[Individual], fitness: Fitness) -> Set[Individual]:
        individuals = sorted(individuals, key=fitness.apply, reverse=True)
        return set(individuals[:len(individuals)//2])