import sys
sys.path.append("..")

from main.fitness import Fitness
from main.individual import Individual
from main.pairing.elitist_pairing import ElitistPairing

class TestIndividual(Individual):

    @staticmethod
    def genome_size() -> int:
        return 1

    def _initialize_genes(self):
        return [0]

    def __str__(self) -> str:
        return f"{self.genes}"

    def __eq__(self, __o: object) -> bool:
        return self.genes == __o.genes

class TestFitness(Fitness):
    
    def apply(self, individual: TestIndividual) -> float:
        return individual.genes[0]

def test_elitist_pairing():

    individuals = [TestIndividual(genes = [i]) for i in range(0, 200, 40)]

    # P(160 chosen) = 160 / sum(0,200,40) = 0.4
    # P(120 chosen) = 120 / [sum(0,200,40)-160] = 0.5
    # P(160 and 120 paired) = 0.4 * 0.5 = 0.2

    # P(80 chosen) = 80 / sum(0,200,40) = 0.2
    # P(40 chosen) = 40 / [sum(0,200,40)-80] = 0.125
    # P(80 and 40 paired) = 0.2 * 0.125 = 0.025

    count_upper, count_lower = 0, 0
    for _ in range(0,1000):
        pairs = ElitistPairing().apply(population=individuals, fitness=TestFitness())
        
        if (TestIndividual([160]), TestIndividual([120])) in pairs:
            count_upper += 1

        if (TestIndividual([80]), TestIndividual([40])) in pairs:
            count_lower += 1
    
    print(f"> Perc. of times the BEST individuals were paired: {count_upper / 1000 * 100}%")
    print(f"> Perc. of times the WORST individuals were paired: {count_lower / 1000 * 100}%")

test_elitist_pairing()