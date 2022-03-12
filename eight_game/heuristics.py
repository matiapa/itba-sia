"""
correctnes_heuristic: Retorna la cantidad de casilleros en la posición
incorrecta. Es una heurística admisible.
"""
def correctnes_heuristic(state): 
  table = state.data
  count = 0

  for position in table.keys():
    number = table[position]
    count += 1 if number != 0 and int(position) != number else 0

  return count

"""
manhattan_heuristic: Retorna la suma de las distancias con norma 1 de
las fichas a su posición objetivo. Es una heurística admisible.
"""
def manhattan_heuristic(state): 
  table = state.data
  distance_sum = 0

  for position in table.keys():
    number = table[position]
    if number == 0:
      continue

    x1 = int(position) % 3
    y1 = int(int(position) / 3)

    x2 = (number-1) % 3
    y2 = int((number-1) / 3)
    
    distance_sum += x2-x1 + y2-y1
  
  return distance_sum

"""
manhattan_squared_heuristic: Se comporta igual que manhattan_heuristic
pero eleva las distancias al cuadrado para penalizar más las fichas
lejanas. Es una heurística no admisible.
"""
def manhattan_squared_heuristic(state): 
  table = state.data
  distance_sum = 0

  for position in table.keys():
    number = table[position]
    if number == 0:
      continue

    x1 = int(position) % 3
    y1 = int(int(position) / 3)

    x2 = (number-1) % 3
    y2 = int((number-1) / 3)
    
    distance_sum += (x2-x1 + y2-y1)^2
  
  return distance_sum