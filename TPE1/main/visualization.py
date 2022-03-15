from main.informed_solvers import SolverHeuristic
import graphviz

def node_label(node): 
  string = f"Ord: {node.explore_order}\n"
  string += f"Cost: {node.cost}\n"
  if type(node) is SolverHeuristic.HeuristicNode:
    string += f"Heu: {node.heuristic}\n"
    # string += f"A*: {node.cost*0.5 + node.heuristic*0.5}\n"
  string += f"\n{node.game_state}"
  return string

def build_graphviz_tree(node, graph):
    color = 'green' if node.game_state.isobjective else 'white' 
    graph.node(str(node.id), node_label(node), style='filled', fillcolor=color)

    for child in node.children:
        build_graphviz_tree(child, graph)
        graph.edge(str(node.id), str(child.id), label=child.src_action)

def build_graphviz_branch(node, graph):
    color = 'green' if node.game_state.isobjective else 'white' 
    graph.node(str(node.id), node_label(node), style='filled', fillcolor=color)

    if node.parent != None:
        build_graphviz_branch(node.parent, graph)
        graph.edge(str(node.parent.id), str(node.id), label=node.src_action)

def renderTree(root):
    graph = graphviz.Digraph('decision_tree')
    build_graphviz_tree(root, graph)
    graph.render(directory='out')

def renderBranch(leaf):
    graph = graphviz.Digraph('solution_branch')
    build_graphviz_branch(leaf, graph)
    graph.render(directory='out')

def get_solution_sequence(node):
  sequence = [{'move': node.src_action, 'state': node.state.data}]

  if node.parent != None:
    sequence += get_solution_sequence(node.parent)

  return sequence