from main.runner import Runner
from canibal_game.state import CanibalGameState
from canibal_game.heuristics import *
import json

class CanibalGameRunner(Runner):

  def get_heuristics(self):
      return {'lefting_people': lefting_people_heuristic}

  def create_initial_state(self):
    return CanibalGameState()


def get_config_from_file():
  conf = json.loads(open('conf.json', 'r').read())
  conf['heuristic'] = conf['canibal_game']['heuristic']
  return conf

result = CanibalGameRunner(get_config_from_file()).run()

# print(result)