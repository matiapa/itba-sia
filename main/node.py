from main.game_state import GameState

class Node:

    LAST_ID = 0
    LAST_EXPLORED_ORDER = 0

    def __init__(self, game_state: GameState, parent, depth, cost, src_action):
        self.game_state = game_state
        self.children = [] # TODO: idealmente es un set pero I'll allow it :) 
        self.parent = parent
        self.depth = depth
        self.cost = cost
        self.id = Node.LAST_ID
        self.explore_order = -1
        self.src_action = src_action
        Node.LAST_ID += 1

    def add(self, node):
      self.children.append(node)

    def mark_explored(self):
      self.explore_order = Node.LAST_EXPLORED_ORDER
      Node.LAST_EXPLORED_ORDER += 1

    @property
    def state(self): 
      return self.game_state

    def __hash__(self): 
      return hash(self.game_state)

    def __eq__(self, other):
      return type(other) is Node and self.game_state == other.game_state