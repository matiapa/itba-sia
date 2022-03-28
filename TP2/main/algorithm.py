from time import time
from turtle import back
from main.crossing.cross import Cross
from main.pairing.pairing import Pairing
from main.selection.selection import Selection
from main.fitness import Fitness
from main.mutation import Mutation
from main.stop_criteria import StopCriteria
from individual import Individual, IndividualFactory

import time
import numpy
import multiprocessing
from joblib import Parallel, delayed
from typing import List, Set, Tuple

class Algorithm:

    ind_factory: IndividualFactory
    pairing: Pairing
    cross: Cross
    mutation: Mutation
    fitness: Fitness
    selection: Selection    


    def __init__(
        self, ind_factory: IndividualFactory, pairing: Pairing, cross: Cross, mutation: Mutation, \
        fitness: Fitness, selection: Selection, init_pop_size: int
    ) -> None:
        self.ind_factory = ind_factory
        self.pairing = pairing
        self.cross = cross
        self.mutation = mutation
        self.fitness = fitness
        self.selection = selection
        self.init_pop_size = init_pop_size

    
    def __iter__(self):
        # Create an initial population of silly beings

        self.population : Set[Individual] = set()
        self.generation = 0

        while len(self.population) < self.init_pop_size:
            individual = self.ind_factory.instantiate(genes = None)
            if individual not in self.population:
                self.population.add(individual)

        return self


    def __next__(self):
        # Make pairs of individuals that will love each other for eternity

        pairs = self.pairing.apply(self.population, self.fitness)
        if len(pairs) != len(self.population) / 2:
            raise RuntimeError("Invalid pairing method, it must return exactly N/2 pairs being N the given population size")
        
        # Create new beings and incorporate them to our population

        for pair in pairs:
            n1, n2 = self.reproduce(pair)
            self.population.add(n1)
            self.population.add(n2)

        # Select the glorious beings that will thrive and survive
        
        self.population = self.selection.apply(individuals = self.population, fitness = self.fitness)
        if len(self.population) != self.init_pop_size:
            print(len(self.population))
            raise RuntimeError("Invalid selection method, it must return exactly N/2 individuals being N the given population size")

        self.generation += 1

        return self.population


    def reproduce(self, pair: Tuple[Individual, Individual]):
        # Give the individuals the miracle of creating new beings
        i1, i2 = self.cross.apply(i1 = pair[0], i2 = pair[1], factory = self.ind_factory)

        # Mutate the new ones and hope they wont become parasites

        self.mutation.apply(i1)
        while i1 in self.population:
            self.mutation.apply(i1)
        
        self.mutation.apply(i2)
        while i2 in self.population or i2 == i1:
            self.mutation.apply(i2)

        return [i1, i2]