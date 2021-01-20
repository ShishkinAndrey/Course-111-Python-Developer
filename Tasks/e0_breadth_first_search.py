from typing import Hashable, List
from collections import deque

import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(g: nx.Graph):
    nx.draw(g, with_labels=True)
    plt.show()

def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    visited = {node: False for node in g.nodes} #словарь непосещенных вершин
    d = deque() #поддоженные вершины
    path = []
    visited[start_node] = True
    d.append(start_node)
    while d:
        current_node = d.popleft()
        visited[current_node] = True
        path.append(current_node)
        for neighbor in g[current_node]:
            if not visited[neighbor] and neighbor not in d:
                d.append(neighbor)
    return path

if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('I', 'H'),
        ('H', 'D'),
        ('H', 'E'),
        ('H', 'J'),
        ('E', 'D'),
    ])
    draw_graph(graph)
    print(bfs(graph, 'A'))