import copy

GRID_SIZE = 3
INITIAL_GRID = [[8,3,5],[4,'x',1],[2,7,6]]

class Node:

    childs = []

    def __init__(self, grid):
        self.grid = grid

def swap(grid, i1, j1, i2, j2):
    temp = grid[i1][j1]
    grid[i1][j1] = grid[i2][j2]
    grid[i2][j2] = temp

def explore_node(node):

    # Exploramos todas las posibilidades

    for i in range(0, GRID_SIZE):
        for j in range(0, GRID_SIZE):
            if node.grid[i][j] == 'x':

                # Si hay una ficha arriba
                if i > 0:
                    new_grid = copy.deepcopy(node.grid)
                    swap(new_grid, i-1, j, i, j)
                    node.childs.append(Node(new_grid))

                # Si hay una ficha abajo
                if i < 2:
                    new_grid = copy.deepcopy(node.grid)
                    swap(new_grid, i+1, j, i, j)
                    node.childs.append(Node(new_grid))

                # Si hay una ficha a la izquierda
                if j > 0:
                    new_grid = copy.deepcopy(node.grid)
                    swap(new_grid, i, j-1, i, j)
                    node.childs.append(Node(new_grid))

                # Si hay una ficha a la derecha
                if j < 2:
                    new_grid = copy.deepcopy(node.grid)
                    swap(new_grid, i, j+1, i, j)
                    node.childs.append(Node(new_grid))

def print_node(node):
    for i in range(0, GRID_SIZE):
        for j in range(0, GRID_SIZE):
            print(node.grid[i][j], end=' ')
        print('')
    print('---------')


def visit_node(node):
    explore_node(node)
    print_node(node)
    # Chequear si es solucion

def bfs(root):
    if root is None:
        return

    queue = [root]
  
    while(len(queue) > 0):
        visit_node(queue[0])
        node = queue.pop(0)
 
        # Enqueue childs
        for child in node.childs:
            queue.append(child)


# Crear nodo inicial

root = Node(INITIAL_GRID)
bfs(root)