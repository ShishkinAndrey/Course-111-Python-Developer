from typing import Hashable, List
from collections import deque

import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    path = [] #пройденный путь
    d = deque() #стек
    visited = {node: False for node in g.nodes}
    visited[start_node] = True
    d.append(start_node)
    while d:
        current_node = d.pop()
        visited[current_node] = True
        path.append(current_node)
        for neighbor in g[current_node]:
            if not visited[neighbor]:
                d.append(neighbor)
    return path

if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'F'),
        ('E', 'G'),
    ])
    print(dfs(graph, 'A'))