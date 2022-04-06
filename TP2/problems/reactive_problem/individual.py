from random import random
from typing import List
import numpy as np

from main.individual import Individual, IndividualFactory


class ReactiveIndividual(Individual):

    @staticmethod
    def genome_size() -> int:
        return 11

    def _initialize_genes(self) -> List[float]:
        return [round(np.random.uniform(-1, 1), 4) for _ in range(0, 11)]

    def __str__(self) -> str:
        precition = 4

        return "W " + str([round(a, precition) for a in self.W]) + '\n'  + "w " + str([round(a, precition) for a in self.w[0]]) + '\n' + str([round(a, precition) for a in self.w[1]]) + '\n'+"w_0 " + str([round(a, precition) for a in self.w_0])

    @property
    def W(self) -> List[float]:
        return self.genes[0:3]

    @property
    def w(self) -> List[List[float]]:
        res = []
        res.append(self.genes[3:6])
        res.append(self.genes[6:9])
        return res

    @property
    def w_0(self) -> List[float]:
        return self.genes[9:11]

class ReactiveIndividualFactory(IndividualFactory):
    def instantiate(self, genes: List[float]) -> Individual:
        return ReactiveIndividual(genes)
