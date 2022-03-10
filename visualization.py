from informed_solvers import SolverHeuristic
import graphviz

def node_label(node): 
  string = f"Ord: {node.explore_order}\n"
  string += f"Cost: {node.cost}\n"
  if type(node) is SolverHeuristic.HeuristicNode:
    string += f"Heu: {node.heuristic}\n"
    # string += f"A*: {node.cost*0.5 + node.heuristic*0.5}\n"
  string += f"\n{node.game_state.matrix}"
  return string

def build_graphviz_tree(node, graph):
    graph.node(str(node.id), node_label(node))
    for child in node.children:
        build_graphviz_tree(child, graph)
        graph.edge(str(node.id), str(child.id))

def build_graphviz_branch(node, graph):
    graph.node(str(node.id), node_label(node))

    if node.parent != None:
        build_graphviz_branch(node.parent, graph)
        graph.edge(str(node.parent.id), str(node.id))

def renderTree(root):
    graph = graphviz.Digraph('Decision tree')
    build_graphviz_tree(root, graph)
    graph.render(directory='out', view=True)

def renderBranch(leaf):
    graph = graphviz.Digraph('Solution branch')
    build_graphviz_branch(leaf, graph)
    graph.render(directory='out', view=True)