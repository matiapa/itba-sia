from main.runner import Runner
from eight_game.state import EightGameState
from eight_game.heuristics import *
import json

class EightGameRunner(Runner):

  def read_config(self):
    super().read_config()
    conf = json.loads(open('conf.json', 'r').read())
    self.INITIAL_GRID = conf['eight_game']['initialGrid']
    self.GOAL_GRID = conf['eight_game']['goalGrid']
    self.HEURISTIC = conf['eight_game']['heuristic']

  def create_initial_state(self):
    zero = -1
    for i in range(0, len(self.INITIAL_GRID)):
      if self.INITIAL_GRID[i] == 0:
        zero = i

    if zero < 0:
      print("The grid must have number zero to represent the free place")
      exit(-1)

    EightGameState.setGoalTable(self.GOAL_GRID)

    return EightGameState(table=self.INITIAL_GRID, target=zero, source=zero)

  def get_heuristics(self):
    return {'correctness': correctnes_heuristic, 'manhattan': manhattan_heuristic, 'manhattan_squared': manhattan_squared_heuristic}

EightGameRunner().run()