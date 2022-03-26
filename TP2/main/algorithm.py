from main.crossing.cross import Cross
from main.pairing.pairing import Pairing
from main.selection.selection import Selection
from main.fitness import Fitness
from main.mutation import Mutation
from main.stop_criteria import StopCriteria

from typing import List
from individual import Individual, IndividualFactory

class Algorithm:

    ind_factory: IndividualFactory
    pairing: Pairing
    cross: Cross
    mutation: Mutation
    fitness: Fitness
    selection: Selection
    stop_criteria: StopCriteria
    

    def __init__(self, ind_factory: IndividualFactory, pairing: Pairing, cross: Cross, mutation: Mutation, fitness: Fitness, \
            selection: Selection, stop_criteria: StopCriteria, init_pop_size: int) -> None:
        self.ind_factory = ind_factory
        self.pairing = pairing
        self.cross = cross
        self.mutation = mutation
        self.fitness = fitness
        self.selection = selection
        self.init_pop_size = init_pop_size
        self.stop_criteria = stop_criteria
    
    def run(self):
        # Create an initial population of silly beings

        self.population = []
        
        for _ in range(0, self.init_pop_size):
            individual = self.ind_factory.instantiate(genes = None)
            self.population.append(individual)

        # Evolve until Singularity happens or the universe reaches thermal death

        while not self.stop_criteria.should_stop(population = self.population, fitness = self.fitness):
            new_population : List[Individual] = []

            # Make pairs of individuals that will love each other for eternity
            pairs = self.pairing.apply(self.population, self.fitness)
            if len(pairs) != len(self.population) / 2:
                raise RuntimeError("Invalid pairing method, it must return exactly N/2 pairs being N the population size")

            for pair in pairs:
                # Give the individuals the miracle of creating new beings
                i1, i2 = self.cross.apply(i1 = pair[0], i2 = pair[1], factory = self.ind_factory)

                # Mutate the new ones and hope they wont become parasites
                self.mutation.apply(i1)
                self.mutation.apply(i2)

                # Incorporate them to our new population
                new_population.append(i1)
                new_population.append(i2)

            # Select the glorious beings that will thrive and survive
            self.population = self.selection.apply(individuals = self.population + new_population, fitness = self.fitness)

