import sys
sys.path.append("..")

from main.fitness import Fitness
from main.individual import Individual
from main.selection.elite_selection import EliteSelection
from main.selection.roulette_selection import RouletteSelection

class TestIndividual(Individual):

    @staticmethod
    def genome_size() -> int:
        return 1

    def _initialize_genes(self):
        return [0]

    def __str__(self) -> str:
        return f"{self.genes[0]}"

    def __eq__(self, __o: object) -> bool:
        return self.genes == __o.genes

class TestFitness(Fitness):
    
    def apply(self, individual: TestIndividual) -> float:
        return individual.genes[0]

def test_elite():
    individuals = list(map(lambda i : TestIndividual(genes = [i]), range(0, 5)))
    print("Individuos creados")
    for individual in individuals:
        print(individual)
    print()
    fitness = TestFitness()
    for individual in individuals:
        fitness.apply(individual)
    # sort individuals by fitness
    individuals.sort(key = lambda i: fitness.apply(i), reverse = True)
    print("Individuos ordenados")
    for individual in individuals:
        print(individual)
    print()
    # select individuals
    selected_individuals = EliteSelection().apply(individuals = individuals, fitness = fitness)
    print("Individuos seleccionados")
    for individual in selected_individuals:
        print(individual)
    print()
    # assert that selected individuals are in the same order as individuals
    for i in range(0, len(individuals)//2):
        assert selected_individuals[i] == individuals[i]

def test_roulette():
    individuals = list(map(lambda i : TestIndividual(genes = [i]), range(0, 100, 10)))
    fitness = TestFitness()

    # select individuals
    populations = []
    for _ in range (0, 100):
        selected_individuals = RouletteSelection().apply(individuals = individuals, fitness = fitness)
        populations.append(selected_individuals)

    count = 0
    # assert that 1000 is included in each element of populations
    for population in populations:
        if TestIndividual(genes = [90]) in population:
            count += 1

    print(count/100)

# test_elite()
test_roulette()