from graph_module import graph_methods as gm
circle = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def fill_vertex_around(regional_map, i, j):
    for g in circle:
        if i + g[0] < 0 or j + g[1] < 0:
            continue
        try:
            if regional_map[i + g[0]][j + g[1]] == '.':
                regional_map[i + g[0]][j + g[1]] = 'S'
        except IndexError:
            pass
    return regional_map

def find_safe_places(regional_map):
    regional_map = [[i for i in row] for row in regional_map]
    for i in range(len(regional_map)):
        for j in range(len(regional_map[i])):
            if regional_map[i][j] == 'X':
                regional_map = fill_vertex_around(regional_map, i, j)
    return regional_map

def finish_map(regional_map):
    regional_map = find_safe_places(regional_map)
    regional_map_for_prepare_graph = [[0 for _ in row] for row in regional_map]
    D_list = []
    for i, row in enumerate(regional_map):
        for j, value in enumerate(row):
            if value == 'S' or value == 'X':
                regional_map_for_prepare_graph[i][j] = 0
            else:
                regional_map_for_prepare_graph[i][j] = value
            if value == 'D':
                D_list.append((i, j))
    graph = gm.Graph.prepare_graph(regional_map_for_prepare_graph, False, False)
    for i in range(len(D_list)):
        D_list[i] = gm.Graph.dfs(graph, D_list[i])
        for D_tuple in D_list[i]:
            regional_map[D_tuple[0]][D_tuple[1]] = 'D'

    for i, row in enumerate(regional_map):
        for j, value in enumerate(row):
            if value == '.':
                regional_map[i][j] = 'S'
    a = ["".join(i) for i in regional_map]
    return a


if __name__ == '__main__':
    assert isinstance(finish_map(("D..", "...", "...")), (list, tuple)), "List or tuple"
    assert list(finish_map(("D..XX.....",
                            "...X......",
                            ".......X..",
                            ".......X..",
                            "...X...X..",
                            "...XXXXX..",
                            "X.........",
                            "..X.......",
                            "..........",
                            "D...X....D"))) == ["DDSXXSDDDD",
                                                "DDSXSSSSSD",
                                                "DDSSSSSXSD",
                                                "DDSSSSSXSD",
                                                "DDSXSSSXSD",
                                                "SSSXXXXXSD",
                                                "XSSSSSSSSD",
                                                "SSXSDDDDDD",
                                                "DSSSSSDDDD",
                                                "DDDSXSDDDD"], "Example"
    assert list(finish_map(("........",
                            "........",
                            "X.X..X.X",
                            "........",
                            "...D....",
                            "........",
                            "X.X..X.X",
                            "........",
                            "........",))) == ["SSSSSSSS",
                                               "SSSSSSSS",
                                               "XSXSSXSX",
                                               "SSSSSSSS",
                                               "DDDDDDDD",
                                               "SSSSSSSS",
                                               'XSXSSXSX',
                                               "SSSSSSSS",
                                               "SSSSSSSS"], "Walls"
