def correctnes_heuristic(state): 
  table = state.data
  count = 0
  for position in table.keys():
    number = table[position]
    count += 1 if number != 0 and int(position) != number else 0
  return count