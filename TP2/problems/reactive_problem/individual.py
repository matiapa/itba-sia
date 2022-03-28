from typing import List
import numpy as np

from main.individual import Individual, IndividualFactory

class ReactiveIndividual(Individual):

    @staticmethod
    def genome_size() -> int:
        return 11

    def _initialize_genes(self) -> List[float]:
        return [round(np.random.uniform(-5, 5), 4) for _ in range(0, 11)]
        
    def __str__(self) -> str:
        return " W " + str(self.W) + " w " + str(self.w) + " w_0 " + str(self.w_0)

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
