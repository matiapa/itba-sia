from eight_game_state import EightGameState
from informed_solvers import *
from uninformed_solvers import *
from visualization import *
from heuristics import *
import json

# Leemos el archivo de configuración

conf = json.loads(open('conf.json', 'r').read())

INITIAL_GRID = conf['initialGrid']
GOAL_GRID = conf['goalGrid']
SEARCH_METHOD = conf['searchMethod']
BPPV_START_LIMIT = conf['bppvStartLimit']
HEURISTIC = conf['heuristic']
HEU_WEIGHT = conf['heu_weight']
PLOT_DECISION_TREE = conf['plotDecisionTree']

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

# Comenzamos la iteración

iterator = iter(solver)
solved = False
n = None

print(f"Searching solution with '{SEARCH_METHOD}'...")

while not solved:
# for i in range(30):
  n, solved = next(iterator)

# Mostramos el resultado

print("Solution found")

renderBranch(n)
if PLOT_DECISION_TREE:
  renderTree(solver.initial_node)