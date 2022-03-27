import sys
sys.path.append("..")

from draw_problem.fitness import BorderFitness
from draw_problem.individual import PointIndividual, PointIndividualFactory

from main.algorithm import Algorithm
from main.crossing.uniform_cross import SimpleCross
from main.mutation import BinaryMutation, NormalMutation
from main.pairing.elitist_pairing import ElitistPairing
from main.selection.elite_selection import EliteSelection
from main.selection.roulette_selection import RouletteSelection

from typing import List

algorithm = Algorithm(
    ind_factory = PointIndividualFactory(), pairing = ElitistPairing(), cross = SimpleCross(p=0.5),
    mutation = BinaryMutation(p=0.5), fitness = BorderFitness(), selection = RouletteSelection(),
    init_pop_size = 100
)
iterator = iter(algorithm)

f = open("output.csv", "w")
f.write('t,x,y,a')

t = 0
while t < 100:
    individuals : List[PointIndividual] = next(iterator)

    for i in individuals:
        f.write(f'{t},{i.genes[0]},{i.genes[1]},1\n')

    t += 1