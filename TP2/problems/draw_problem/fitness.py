from math import hypot
from typing import Dict, List
from draw_problem.individual import PointIndividual
from main.fitness import Fitness

class BorderFitness(Fitness):

    # def apply(self, i: PointIndividual) -> float:
    #     dist_bl = hypot(PointIndividual.GRID_SIZE - i.genes[0], PointIndividual.GRID_SIZE - i.genes[1])
    #     dist_br = hypot(PointIndividual.GRID_SIZE - i.genes[0], i.genes[1])
    #     dist_tl = hypot(i.genes[0], PointIndividual.GRID_SIZE - i.genes[1])
    #     dist_tr = hypot(i.genes[0], i.genes[1])

    #     min_dist = min([dist_br, dist_bl, dist_tr, dist_tl])
    #     in_radius = dist_br < 10 or dist_bl < 10 or dist_tl < 10

    #     return in_radius + 1

    def apply(self, i: PointIndividual) -> float:
        dist_ctr = hypot(i.genes[0] - PointIndividual.GRID_SIZE / 2, i.genes[1] - PointIndividual.GRID_SIZE / 2)
        return 1/abs(dist_ctr - 10) if dist_ctr != 10 else 100