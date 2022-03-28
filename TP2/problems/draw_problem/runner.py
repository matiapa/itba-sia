import sys
sys.path.append("..")
sys.path.append("../..")

from problems.draw_problem.fitness import BorderFitness
from problems.draw_problem.individual import PointIndividual, PointIndividualFactory

from main.algorithm import Algorithm
from main.crossing.uniform_cross import SimpleCross
from main.mutation import UniformIntegerMutation
from main.pairing.elitist_pairing import ElitistPairing
from main.selection.elite_selection import EliteSelection
from main.selection.roulette_selection import RouletteSelection

from typing import List

fitness = BorderFitness()

algorithm = Algorithm(
    ind_factory = PointIndividualFactory(), pairing = ElitistPairing(), cross = SimpleCross(p=0),
    mutation = UniformIntegerMutation(p=1, _range=5), fitness = fitness, selection = EliteSelection(),
    init_pop_size = 100
)
iterator = iter(algorithm)

f = open("output.csv", "w")
f.write('t,x,y,a\n')

for i in algorithm.population:
    f.write(f'0,{i.genes[0]},{i.genes[1]},1\n')
t = 1

while t < 100:
    individuals : List[PointIndividual] = next(iterator)

    for i in individuals:
        f.write(f'{t},{i.genes[0]},{i.genes[1]},1\n')
        # f.write(f'{t},{i.genes[0]},{i.genes[1]},{round(fitness.apply(i),6)}\n')
    t += 1