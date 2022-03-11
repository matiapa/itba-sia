from main.runner import Runner
from canibal_game.state import CanibalGameState
from canibal_game.heuristics import *
import json

class CanibalGameRunner(Runner):

  def read_config(self):
    super().read_config()
    conf = json.loads(open('conf.json', 'r').read())
    self.HEURISTIC = conf['canibal_game']['heuristic']

  def get_heuristics(self):
      return {'lefting_people': lefting_people_heuristic}

  def create_initial_state(self):
    return CanibalGameState()

CanibalGameRunner().run()