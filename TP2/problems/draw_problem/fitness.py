from math import hypot
from typing import Dict, List
from draw_problem.individual import PointIndividual
from main.fitness import Fitness

class BorderFitness(Fitness):

    def apply(self, i: PointIndividual) -> float:
        dist_tr = hypot(i.genes[0] - PointIndividual.GRID_SIZE, i.genes[1] - PointIndividual.GRID_SIZE)
        return dist_tr