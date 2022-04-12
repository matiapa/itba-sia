from turtle import color
from fitness import ReactiveFitness, ReactiveFitnessConcave, ReactiveFitnessConvex,  F, inputs
from individual import ReactiveIndividual, ReactiveIndividualFactory
from typing import List
from main.algorithm import Algorithm
from main.crossing.simple_cross import SimpleCross
from main.mutation import NormalMutation
from main.pairing.elitist_pairing import ElitistPairing
from main.selection.tournament_selection import TournamentSelection
from main.selection.elite_selection import EliteSelection
from main.selection.rank_selection import RankSelection
from main.selection.roulette_selection import RouletteSelection
from main.selection.boltzmann_selection import BoltzmannSelection
from main.selection.truncated_selection import TruncatedSelection
from main.selection.selection import Selection
from matplotlib import pyplot as plt
import sys
sys.path.append("..")
sys.path.append("../..")

algo = Algorithm(
        ind_factory=ReactiveIndividualFactory(),
        pairing=ElitistPairing(),
        cross=SimpleCross(),
        mutation=NormalMutation(p=0.5, sigma=0.3),
        fitness=ReactiveFitness(),
        selection=RouletteSelection(),
        init_pop_size=70,
        replace=False
)

fitness = ReactiveFitness()
res = []
it = iter(algo)
for t in range(400):
    individuals: List[ReactiveIndividual] = next(it)
    res.append(min([fitness.error(indi) for indi in individuals]))


plt.plot(range(400), res, 'k', linewidth = 0.5)
plt.show()

