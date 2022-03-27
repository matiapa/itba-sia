import sys
sys.path.append("..")

from fitness import BagFitness
from individual import BagIndividualFactory
from stop_criteria import BagStopCriteria

from main.algorithm import Algorithm
from main.crossing.uniform_cross import SimpleCross
from main.individual import Individual
from main.mutation import BinaryMutation
from main.pairing.elitist_pairing import ElitistPairing
from main.selection.elite_selection import EliteSelection

from typing import List
from numpy import argmax


fitness = BagFitness()

algorithm = Algorithm(
    ind_factory = BagIndividualFactory(), pairing = ElitistPairing(), cross = SimpleCross(p=0.5),
    mutation = BinaryMutation(p=0.05),    fitness = fitness,          selection = EliteSelection(),
    stop_criteria = BagStopCriteria(),    init_pop_size = 100
)

individuals : List[Individual] = algorithm.run()

scores = [fitness.apply(i) for i in individuals]
i_max = argmax(scores)

print(f'> Best individual is: {i_max}')
print(f'> Fitness: {scores[i_max]}')
print(f'> Genes: {individuals[i_max].genes}')