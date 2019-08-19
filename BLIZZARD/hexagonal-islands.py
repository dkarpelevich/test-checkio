from typing import Set, Iterable
from graph_module import graph_methods as gm


def hexes_around_vertex(vertex: str) -> set:
    one_cell = set()
    if vertex[0] in 'ACEGIK':
        one_cell.add(chr(ord(vertex[0]) - 1) + str(int(vertex[1]) - 1))  # l
        one_cell.add(chr(ord(vertex[0]) - 1) + str(int(vertex[1])))  # l
        one_cell.add(chr(ord(vertex[0]) + 1) + str(int(vertex[1]) - 1))  # r
        one_cell.add(chr(ord(vertex[0]) + 1) + str(int(vertex[1])))  # r
    else:  # 'BDFHJL'
        one_cell.add(chr(ord(vertex[0]) - 1) + str(int(vertex[1])))  # l
        one_cell.add(chr(ord(vertex[0]) - 1) + str(int(vertex[1]) + 1))  # l
        one_cell.add(chr(ord(vertex[0]) + 1) + str(int(vertex[1])))  # r
        one_cell.add(chr(ord(vertex[0]) + 1) + str(int(vertex[1]) + 1))  # r
    one_cell.add(chr(ord(vertex[0])) + str(int(vertex[1]) - 1))
    one_cell.add(chr(ord(vertex[0])) + str(int(vertex[1]) + 1))
    try:
        one_cell.remove(None)
    except KeyError:
        pass
    return one_cell


def hexagonal_islands(coasts: Set[str]) -> Iterable[int]:
    graph = gm.Graph.prepare_graph_hex(coasts)
    list_of_islands = [sorted(x) for x in gm.Graph.island(graph)]
    for i in list_of_islands:
        for j in range(len(i)-1):
            if i[j+1][0] == i[j][0]:
                i.extend([i[j][0] + str(int(i[j][1]) + num) for num in
                          range(1, int(i[j+1][1]) - int(i[j][1]))
                          if hexes_around_vertex(i[j][0] + str(int(i[j][1]) + num)).issubset(coasts)])
            else:
                pass
    return sorted([len(x) for x in list_of_islands])


if __name__ == '__main__':
    assert(sorted(hexagonal_islands({'A1', 'A2', 'A3', 'A4', 'B1', 'B4', 'C2', 'C5', 'D2', 'D3', 'D4', 'D5',
                                     'H6', 'H7', 'H8', 'I6', 'I9', 'J5', 'J9', 'K6', 'K9', 'L6', 'L7', 'L8'}))) == [16, 19]


