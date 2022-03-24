from typing import List
from fitness import Fitness
from individual import Individual, IndividualFactory
from mutation import Mutation
from cross import Cross
from selection import Selection

import random

from stop_criteria import StopCriteria

class Algorithm:

    ind_factory: IndividualFactory
    cross: Cross
    mutation: Mutation
    fitness: Fitness
    selection: Selection
    stop_criteria: StopCriteria
    

    def __init__(self, ind_factory: IndividualFactory, cross: Cross, mutation: Mutation, fitness: Fitness, selection: Selection, \
            stop_criteria: StopCriteria, init_pop_size: int) -> None:
        self.ind_factory = ind_factory
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

            while len(new_population) < self.init_pop_size:
                # Choose two individuals and make them create new life
                parents = random.sample(population = self.population, k = 2)
                i1, i2 = self.cross.apply(i1 = parents[0], i2 = parents[1], factory = self.ind_factory)

                # Mutate the new ones and hope they wont become parasites
                self.mutation.apply(i1)
                self.mutation.apply(i2)

                # Incorporate them to our new population
                new_population.append(i1)
                new_population.append(i2)

            # Select the glorious beings that will thrive and survive
            self.population = self.selection.apply(individuals = self.population + new_population, fitness = self.fitness)

