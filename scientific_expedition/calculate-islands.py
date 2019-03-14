from typing import List


def decorator(land_map, i, j):
    try:
        if land_map[i][j] == 1 and i >= 0 and j >= 0:
            return i, j
    except IndexError:
        pass


def prepare_graph(land_map: List[List[int]]) -> dict:
    dict_of_cells = {}
    for i in range(len(land_map)):
        for j in range(len(land_map[i])):
            one_cell = set()
            if land_map[i][j] == 1:
                one_cell.add(decorator(land_map, i - 1, j - 1))
                one_cell.add(decorator(land_map, i - 1, j))
                one_cell.add(decorator(land_map, i - 1, j + 1))
                one_cell.add(decorator(land_map, i, j - 1))
                one_cell.add(decorator(land_map, i, j + 1))
                one_cell.add(decorator(land_map, i + 1, j - 1))
                one_cell.add(decorator(land_map, i + 1, j))
                one_cell.add(decorator(land_map, i + 1, j + 1))
                try:
                    one_cell.remove(None)
                except KeyError:
                    pass
                dict_of_cells.update({(i, j): one_cell})
    return dict_of_cells

# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def checkio(land_map: List[List[int]]) -> List[int]:
    graph = prepare_graph(land_map)
    list_of_squares = []
    for i in graph:
        cell_path = dfs(graph, i)
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
