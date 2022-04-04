from main.fitness import Fitness
from main.individual import Individual
from main.selection.selection import Selection
from typing import Set
import numpy as np

class RankSelection(Selection):

    def __str__(self):
        return "Rank"
    """
    Selects individuals using Rank Method
    """
    def apply(self, individuals: Set[Individual], fitness: Fitness, replace: bool) -> Set[Individual]:
        P = len(individuals)
        individuals = sorted(individuals, key=fitness.apply, reverse=True)
        f_1 = [(P-i)/i for i in range(1, P+1)]
        sum_f_1 = sum(f_1)
        probabilities = [(f_1[i] / sum_f_1) for i in range(0, P)]
        np_array = np.random.choice(list(individuals), size=P//2, replace=replace, p=probabilities)
        return set(np_array)

