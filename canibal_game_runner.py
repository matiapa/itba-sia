from main.runner import Runner
from canibal_game.state import CanibalGameState
import json

class CanibalGameRunner(Runner):

  def get_heuristics(self):
      return {}

  def create_initial_state(self):
    return CanibalGameState()

CanibalGameRunner().run()