from copy import copy
from main.game_state import GameState

class CanibalGameState(GameState):

    def __init__(self) :
        self.origin_canibals = 3
        self.origin_missioners = 3
        self.destination_canibals = 0
        self.destination_missioners = 0
        self.boat_position = 'O'

    @property
    def isobjective(self):
        return self.destination_canibals == 3 and self.destination_missioners == 3

    @property
    def game_moves(self):
        # Notation is 'src_missioners_canibals, so for example 'O_1_1'
        # means move 1 missioner and 1 canibal from origin to destiny
        return {
            'O_2_0': 2, 'O_1_1': 2, 'O_0_2': 2, 'O_1_0': 1, 'O_0_1': 1,
            'D_2_0': 2, 'D_1_1': 2, 'D_0_2': 2, 'D_1_0': 1, 'D_0_1': 1,
        }

    def make_move(self, m: str):
        if m not in self.game_moves.keys():
            raise 'Invalid move code'
        
        source, missioners, canibals = m.split('_')
        sign = 1 if source == 'O' else -1
        missioners = int(missioners)
        canibals = int(canibals)

        new_state = copy(self)
        new_state.origin_canibals -= sign * canibals
        new_state.origin_missioners -= sign * missioners
        new_state.destination_canibals += sign * canibals
        new_state.destination_missioners += sign * missioners
        new_state.boat_position = 'D' if source == 'O' else 'O'

        if source != self.boat_position\
            or new_state.origin_canibals < 0 or new_state.origin_missioners < 0 or new_state.destination_canibals < 0 or new_state.destination_missioners < 0 \
            or (new_state.origin_canibals > new_state.origin_missioners and new_state.origin_missioners > 0) \
            or (new_state.destination_canibals > new_state.destination_missioners and new_state.destination_missioners > 0):
                return None

        return new_state

    @property
    def data(self):
        return {
            'origin_canibals': self.origin_canibals, 'origin_missioners': self.origin_missioners,
            'destination_canibals': self.destination_canibals, 'destination_missioners': self.destination_missioners
        }

    def __str__(self):
        string = ''.join(['C' for i in range(0, self.origin_canibals)])
        string += ''.join(['M' for i in range(0, self.origin_missioners)])
        string += ' \\\_/~~' if self.boat_position == 'O' else '~~\\\_/ '
        string += ''.join(['C' for i in range(0, self.destination_canibals)])
        string += ''.join(['M' for i in range(0, self.destination_missioners)])
        return string

    def __hash__(self): 
        return hash((self.origin_canibals, self.origin_missioners, self.destination_canibals, self.destination_missioners, self.boat_position))

    def __eq__(self, o): 
        return isinstance(o, CanibalGameState) and o.origin_canibals == self.origin_canibals and o.origin_missioners == self.origin_missioners \
            and o.destination_canibals == self.destination_canibals and o.destination_missioners == self.destination_missioners \
            and o.boat_position == self.boat_position