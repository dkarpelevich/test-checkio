from typing import List
from graph_module import graph_methods as gm


def checkio(land_map: List[List[int]]) -> List[int]:
    graph = gm.Graph.prepare_graph(land_map, True)
    list_of_squares = []
    for i in graph:
        cell_path = gm.Graph.dfs(graph, i)
        if cell_path not in list_of_squares:
            list_of_squares.append(cell_path)
    return sorted([len(x) for x in list_of_squares])


if __name__ == '__main__':
    print("Example:")

    checkio([[1, 0, 1, 0],
             [1, 0, 0, 1],
             [0, 1, 0, 1]])

    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
