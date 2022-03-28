from main.fitness import Fitness
from main.individual import Individual
from main.selection.selection import Selection
from typing import Set
import numpy as np

class RankSelection(Selection):

    """
    Selects individuals using Rank Method
    """
    def apply(self, individuals: Set[Individual], fitness: Fitness) -> Set[Individual]:
        individuals = sorted(individuals, key=fitness.apply, reverse=True)
        P = len(individuals)
        ranking_sum = (P+1)*P/2
        probabilities = [i/ranking_sum for i in range(1,P+1)]
        np_array = np.random.choice(list(individuals), size=P//2, replace=False, p=probabilities)
        return set(np_array)