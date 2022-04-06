from main.fitness import Fitness
from main.individual import Individual
from main.selection.selection import Selection
from typing import Set
import numpy as np

class RouletteSelection(Selection):

    def __str__(self):
        return "Roulette"

    """
    Selects individuals based on their relative fitness
    """
    def apply(self, individuals: Set[Individual], fitness: Fitness) -> Set[Individual]:
        max = sum(fitness.apply(individual) for individual in individuals) 
        probabilities = [fitness.apply(individual) / max for individual in individuals]
        np_array = np.random.choice(list(individuals), size=len(individuals)//2, replace=True, p=probabilities)
        return set(np_array)