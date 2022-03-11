"""
lefting_people_heuristic: Retorna la cantidad de misioneros y caníbales que
aun restan trasladar a la otra orilla. Es una heurística admisible.
"""
def lefting_people_heuristic(state): 
  data = state.data
  return data['origin_canibals'] + data['origin_missioners']