"""
https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
"""
from typing import List

class Graph:
    @staticmethod
    def decorator(land_map: List[List[int]], i, j):
        try:
            if land_map[i][j] != 0 and i >= 0 and j >= 0:
                return i, j
        except IndexError:
            pass

    """
    prepare_graph(land_map: list, diagonal: bool) returns dict of vertex connected horizontally,
    vertically and/or diagonally  
    [[1, 0, 1, 0],
     [1, 0, 0, 1],
     [0, 1, 0, 1]]
         ||
         \/
    {(1, 3): {(2, 3), (0, 2)}, (2, 3): {(1, 3)}, (2, 1): {(1, 0)},
     (1, 0): {(0, 0), (2, 1)}, (0, 2): {(1, 3)}, (0, 0): {(1, 0)}}
    """
    @staticmethod
    def prepare_graph(land_map: List[List[int]], diagonal: bool) -> dict:
        dict_of_cells = {}
        for i in range(len(land_map)):
            for j in range(len(land_map[i])):
                one_cell = set()
                if land_map[i][j] != 0:
                    if diagonal:
                        one_cell.add(Graph.decorator(land_map, i - 1, j - 1))  # d
                        one_cell.add(Graph.decorator(land_map, i - 1, j + 1))  # d
                        one_cell.add(Graph.decorator(land_map, i + 1, j - 1))  # d
                        one_cell.add(Graph.decorator(land_map, i + 1, j + 1))  # d
                    one_cell.add(Graph.decorator(land_map, i - 1, j))      # v
                    one_cell.add(Graph.decorator(land_map, i + 1, j))      # v
                    one_cell.add(Graph.decorator(land_map, i, j - 1))      # h
                    one_cell.add(Graph.decorator(land_map, i, j + 1))      # h
                    try:
                        one_cell.remove(None)
                    except KeyError:
                        pass
                    dict_of_cells.update({(i, j): one_cell})
        return dict_of_cells

    """
    [[1, 0, 1, 0],
     [1, 0, 0, 1],
     [0, 1, 0, 1]]
         ||
         \/
    island returns list of sets with coordinates of islands w/ or w/o diagonal connections
    [{(1, 3), (2, 3), (0, 2)}, {(1, 0), (0, 0), (2, 1)}]
    """
    @staticmethod
    def island(land_map: List[List[int]], diagonal: bool) -> List[set]:
        graph = Graph.prepare_graph(land_map, diagonal)
        list_of_squares = []
        for i in graph:
            cell_path = Graph.dfs(graph, i)
            if cell_path not in list_of_squares:
                list_of_squares.append(cell_path)
        return list_of_squares

    @staticmethod
    def dfs(graph, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(graph[vertex] - visited)
        return visited

    @staticmethod
    def dfs_paths(graph, start, goal):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))
