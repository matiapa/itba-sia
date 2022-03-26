import sys
sys.path.append("..")

from main.fitness import Fitness
from main.individual import Individual
from main.pairing.elitist_pairing import ElitistPairing

class TestIndividual(Individual):

    @staticmethod
    def genome_size() -> int:
        return 1

    def __initialize_genes(self):
        return [0]

    def __str__(self) -> str:
        return f"{self.genes[0]}"

class TestFitness(Fitness):
    
    def apply(self, individual: TestIndividual) -> float:
        return individual.genes[0]

def test_elitist_pairing():

    individuals = list(map(lambda i : TestIndividual(genes = [i]), range(0, 5)))

    pairs = ElitistPairing().apply(population=individuals, fitness=TestFitness())

    for p in pairs:
        print(f"{p[0]} {p[1]}")

test_elitist_pairing()