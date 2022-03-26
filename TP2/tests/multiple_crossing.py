from main.individual import Individual
from main.crossing.multiple_cross import MultipleCross

class TestIndividual(Individual):

    @staticmethod
    def genome_size() -> int:
        return 6

    def __initialize_genes(self):
        return None

    def __str__(self) -> str:
        return f"{self.genes[0]}"


individuals = [
    TestIndividual(genes = [0, 1, 0, 1, 0, 1]),
    TestIndividual(genes = [1, 0, 1, 0, 1, 0])
]
