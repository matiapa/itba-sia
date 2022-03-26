import sys
sys.path.append("..")

from typing import List
from main.individual import Individual, IndividualFactory
from main.crossing.multiple_cross import MultipleCross

class TestIndividual(Individual):

    @staticmethod
    def genome_size() -> int:
        return 6

    def __initialize_genes(self):
        return None

    def __str__(self) -> str:
        return f"{self.genes}"

class TestIndividualFactory(IndividualFactory):
    
    def instantiate(self, genes: List[float]) -> Individual:
       return TestIndividual(genes)

i1 = TestIndividual(genes = [0, 1, 0, 1, 0, 1])
i2 = TestIndividual(genes = [1, 0, 1, 0, 1, 0])

print(i1)
print(i2)

n1, n2 = MultipleCross().apply(i1, i2, factory=TestIndividualFactory(), npoints=2)

print(n1)
print(n2)