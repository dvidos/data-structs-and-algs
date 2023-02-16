from typing import List
import random

# how do we define a graph?
# as a table of nodes and a table of vertices?
# stack: append(), pop(), queue: append(), pop(0)


class Node:
    def __init__(self, value, vertices) -> None:
        self.value = value
        self.vertices = vertices
        self.visited = False

    def __str__(self) -> str:
        return f"Node(value={self.value}, vertices={self.vertices}, visited={self.visited})"


class Graph:
    def __init__(self, nodes: List[Node], vertices) -> None:
        self.nodes = nodes
        self.vertices = vertices

    def reset_visits(self):
        for n in self.nodes:
            n.visited = False

    def __str__(self) -> str:
        return "  " + "\n  ".join([str(n) for n in self.nodes])


def generate_random_graph() -> Graph:
    g = Graph([], [])
    value = 0
    for i in range(random.randint(4, 12)):
        node = Node(value, [])
        value += 1
        g.nodes.append(node)
    
    for node in g.nodes:
        node.vertices = []
        for r in range(0, random.randint(1, 3)):
            node.vertices.append(random.randrange(0, value))
    
    return g


def breadth_first_search(g: Graph, initial_node: Node):
    to_visit = [initial_node]
    visits = []
    while len(to_visit) > 0:
        node = to_visit.pop(0)  # hence using a queue
        if node.visited:
            continue

        visits.append(node.value)
        node.visited = True
        for target in node.vertices:
            to_visit.append(g.nodes[target])
    print("  visited " + ", ".join([str(v) for v in visits]))


def depth_first_search(g: Graph, initial_node: Node):
    to_visit = [initial_node]
    visits = []
    while len(to_visit) > 0:
        node = to_visit.pop()  # hence using a stack
        if node.visited:
            continue

        visits.append(node.value)
        node.visited = True
        for target in node.vertices:
            to_visit.append(g.nodes[target])
    print("  visited " + ", ".join([str(v) for v in visits]))


def test():
    print("Generating random graph");
    g = generate_random_graph()
    print(g)
    starting_node = random.choice(g.nodes)
    print(f"  Random starting node is {starting_node}")

    print("Breadth First Traverse")
    g.reset_visits()
    breadth_first_search(g, starting_node)

    print("Depth First Traverse")
    g.reset_visits()
    depth_first_search(g, starting_node)


test()
"""
Generating random graph
  Node(value=0, vertices=[2, 1], visited=False)
  Node(value=1, vertices=[4, 5], visited=False)
  Node(value=2, vertices=[2], visited=False)
  Node(value=3, vertices=[3, 3, 5], visited=False)
  Node(value=4, vertices=[5, 2], visited=False)
  Node(value=5, vertices=[3, 0], visited=False)
  Random starting node is Node(value=0, vertices=[2, 1], visited=False)
Breadth First Traverse
  visited 0, 2, 1, 4, 5, 3
Depth First Traverse
  visited 0, 1, 5, 3, 4, 2
"""