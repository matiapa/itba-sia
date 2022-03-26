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

n1, n2 = MultipleCross().apply(i1, i2, factory=TestIndividualFactory(), npoints=2, points=[2,4])

if n1.genes == [1,0,0,1,1,0] and n2.genes == [0,1,1,0,0,1]:
    print("Passed!")
else:
    print("Failed")