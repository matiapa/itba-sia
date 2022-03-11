from main.informed_solvers import *
from main.uninformed_solvers import *
from main.visualization import *
from eight_game.state import EightGameState
from eight_game.heuristics import *
import json
import timeit

# Leemos el archivo de configuración

conf = json.loads(open('conf.json', 'r').read())

INITIAL_GRID = conf['initialGrid']
GOAL_GRID = conf['goalGrid']
SEARCH_METHOD = conf['searchMethod']
BPPV_START_LIMIT = conf['bppvStartLimit']
HEURISTIC = conf['heuristic']
HEU_WEIGHT = conf['heu_weight']
PLOT_DECISION_TREE = conf['plotDecisionTree']
SEARCH_TIMEOUT = conf['timeout']

# Preparamos el estado inicial del juego

zero = -1
for i in range(0, len(INITIAL_GRID)):
  if INITIAL_GRID[i] == 0:
    zero = i

if zero < 0:
  print("The grid must have number zero to represent the free place")
  exit(-1)

EightGameState.setGoalTable(GOAL_GRID)

gs = EightGameState(table=INITIAL_GRID, target=zero, source=zero)

# Peparamos el solver a utilizar

heuristics = {'correctness': correctnes_heuristic, 'manhattan': manhattan_heuristic, 'manhattan_squared': manhattan_squared_heuristic}

solver = None
if SEARCH_METHOD == 'bpa':
  solver = SolverBPA(gs)
elif SEARCH_METHOD == 'bpp':
  solver = SolverBPP(gs) 
elif SEARCH_METHOD == 'bppv':
  solver = SolverBPPV(gs, BPPV_START_LIMIT)
elif SEARCH_METHOD == 'heu_local':
  solver = SolverLocalHeuristic(gs, heuristics[HEURISTIC])
elif SEARCH_METHOD == 'heu_global':
  solver = SolverGlobalHeuristic(gs, heuristics[HEURISTIC])
elif SEARCH_METHOD == 'heu_weighted':
  solver = SolverWeightHeuristic(gs, heuristics[HEURISTIC], HEU_WEIGHT)
else:
  print(f"Unknown search method: {SEARCH_METHOD}")
  exit(-1)

# Mostramos los parámetros de la búsqueda

print("> Search parameters")
print(f"-  Search method: {SEARCH_METHOD}")
if SEARCH_METHOD == 'bppv':
  print(f"-  Initial depth limit: {BPPV_START_LIMIT}")
elif 'heu' in SEARCH_METHOD:
  print(f"-  Heuristic: {HEURISTIC}")
  if SEARCH_METHOD == 'heu_weighted':
    print(f"-  Weight: {HEU_WEIGHT}")

# Comenzamos la iteración

print(f"\n> Searching solution...")

iterator = iter(solver)
solved = False
n = None

start_time = timeit.default_timer()
elapsed_time = 0
while not solved and (elapsed_time <= SEARCH_TIMEOUT or SEARCH_TIMEOUT < 0):
  n, solved = next(iterator)
  elapsed_time = timeit.default_timer() - start_time

# Mostramos el resultado

if solved:
  print("\n> Solution found")
  print(f"-  Depth: {n.depth}")
  print(f"-  Cost: {n.cost}")
  print(f"-  Expanded nodes: {len(solver.explored)}")
  print(f"-  Frontier nodes: {len(solver.frontier)}")
else:
  print("\n> Solution not found")
print(f"-  Processing time: {elapsed_time} ms")

if solved:
  print("\n> Generating solution graph...")
  renderBranch(n)
  print("-  Graph generated at out/solution_branch.pdf")

if PLOT_DECISION_TREE:
  print("\n> Generating decision tree graph...")
  renderTree(solver.initial_node)
  print("-  Graph generated at out/decision_tree.pdf")