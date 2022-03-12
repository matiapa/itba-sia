from main.runner import Runner
from eight_game.state import EightGameState
from eight_game.heuristics import *
import json

class EightGameRunner(Runner):

  def create_initial_state(self):
    zero = -1
    for i in range(0, len(self.config['initialGrid'])):
      if self.config['initialGrid'][i] == 0:
        zero = i

    if zero < 0:
      print("The grid must have number zero to represent the free place")
      exit(-1)

    EightGameState.setGoalTable(self.config['goalGrid'])

    return EightGameState(table=self.config['initialGrid'], target=zero, source=zero)

  def get_heuristics(self):
    return {'correctness': correctnes_heuristic, 'manhattan': manhattan_heuristic, 'manhattan_squared': manhattan_squared_heuristic}


def get_config_from_file():
    conf = json.loads(open('conf.json', 'r').read())
    conf['heuristic'] = conf['eight_game']['heuristic']
    conf['initialGrid'] = conf['eight_game']['initialGrid']
    conf['goalGrid'] = conf['eight_game']['goalGrid']
    return conf

if __name__ == "__main__":
    EightGameRunner(get_config_from_file()).run()
    # print(result)