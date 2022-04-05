import sys
sys.path.append("..")
sys.path.append("../..")

from main.selection.boltzmann_selection import BoltzmannSelection
from main.selection.elite_selection import EliteSelection
from main.selection.rank_selection import RankSelection
from main.selection.roulette_selection import RouletteSelection
from main.selection.softmax_selection import SoftmaxSelection
from main.selection.tournament_selection import TournamentSelection
from main.selection.truncated_selection import TruncatedSelection
from main.mutation import NormalMutation
from main.mutation import UniformMutation
from main.crossing.simple_cross import SimpleCross
from main.crossing.uniform_cross import UniformCross
from main.crossing.multiple_cross import MultipleCross
from main.pairing.elitist_pairing import ElitistPairing
from main.algorithm import Algorithm
from main.algorithm_parallel import AlgorithmParallel

from problems.reactive_problem.individual import ReactiveIndividual, ReactiveIndividualFactory
from problems.reactive_problem.fitness import ReactiveFitness, F, inputs

from time import time
from numpy import argmax
from typing import List
from tqdm import tqdm
import json


def run_algorithm_parallel(crossing, mutation, fitness, selection, population_size, generations):
    algorithmParallel = AlgorithmParallel(
        ind_factory = ReactiveIndividualFactory(), pairing = ElitistPairing(), cross=crossing,
        mutation=mutation, fitness=fitness, selection=selection, init_pop_size=population_size, generations=generations
    )
    return algorithmParallel.run_multiple()

def run_algorithm_sequential(crossing, mutation, fitness, selection, population_size, generations):
    algorithm = Algorithm(
        ind_factory=ReactiveIndividualFactory(), pairing=ElitistPairing(), cross=crossing,
        mutation=mutation, fitness=fitness, selection=selection, init_pop_size=population_size
    )

    iterator = iter(algorithm)
    for t in tqdm(range(generations)):
        individuals = next(iterator)

    return individuals

if __name__ == '__main__':
    # Read config parameters

    if len(sys.argv) < 2:
        print('Usage: ./runner.py config.json')

    config = json.loads(open(sys.argv[1], 'r').read())

    population_size = int(config['populationSize'])
    generations = int(config['generations'])

    fitness = ReactiveFitness()

    if config['crossing']['method'] == 'uniform':
        p = config['crossing']['uniform']['p']
        crossing = UniformCross(p)
    elif config['crossing']['method'] == 'multiple':
        n = int(config['crossing']['multiple']['n'])
        if 'points' in config['crossing']['multiple']:
            crossing = MultipleCross(n, config['crossing']['multiple']['points'])
        else:
            crossing = MultipleCross(n)

    p = float(config['mutation']['probability'])
    if config['mutation']['method'] == 'uniform':
        r = float(config['mutation']['params']['range'])
        mutation = UniformMutation(p, r)
    elif config['mutation']['method'] == 'normal':
        s = float(config['mutation']['params']['deviation'])
        mutation = NormalMutation(p, s)

    if config['selection']['method'] == 'elite':
        selection = EliteSelection()
    elif config['selection']['method'] == 'rank':
        selection = RankSelection()
    elif config['selection']['method'] == 'roulette':
        selection = RouletteSelection()
    elif config['selection']['method'] == 'softmax':
        selection = SoftmaxSelection()
    elif config['selection']['method'] == 'tournament':
        u = float(config['selection']['tournament']['u'])
        selection = TournamentSelection(u)
    elif config['selection']['method'] == 'truncated':
        k = int(config['selection']['truncated']['k'])
        selection = TruncatedSelection(k)
    elif config['selection']['method'] == 'boltzmann':
        tc = float(config['selection']['boltzmann']['tc'])
        t0 = float(config['selection']['boltzmann']['t0'])
        k = float(config['selection']['boltzmann']['k'])
        selection = BoltzmannSelection(tc, t0, k)

    # Print parameters being used

    print('> Input parameters')
    print(f'>> Population size: {population_size}')
    print(f'>> Generations: {generations}')
    print(f'>> Crossing method: {crossing}')
    print(f'>> Mutation method: {mutation}')
    print(f'>> Selection method: {selection}')

    # Run the algorithm

    print("\n> Running algorithm")

    s = time()
    if len(sys.argv)==3 and sys.argv[2] == 'parallel':
        individuals = run_algorithm_parallel(crossing, mutation, fitness, selection, population_size, generations)
    else:
        individuals = run_algorithm_sequential(crossing, mutation, fitness, selection, population_size, generations)
    ellapsed_time = time() - s

    # Print the results

    individuals = list(individuals)    
    fitnesses = [fitness.apply(i) for i in individuals]
    opt_arg = argmax(fitnesses)
    opt_ind = individuals[opt_arg]
    F0 = F(opt_ind.W, opt_ind.w, opt_ind.w_0, inputs["xi"][0])
    F1 = F(opt_ind.W, opt_ind.w, opt_ind.w_0, inputs["xi"][1])
    F2 = F(opt_ind.W, opt_ind.w, opt_ind.w_0, inputs["xi"][2])

    print("\n> Results")
    print(f">> Ellapsed time: {ellapsed_time} s")
    print(f">> Optimal individual")
    print(f">>> Argument: {opt_arg}")
    print(f">>> Error: {fitness.error(opt_ind)}")
    print(f">>> F0: {F0}")
    print(f">>> F1: {F1}")
    print(f">>> F2: {F2}")