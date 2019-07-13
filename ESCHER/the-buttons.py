from graph_module import graph_methods as gm

def buttons(land_map):
    land_map = land_map.split('\n')[1:]
    for i in range(len(land_map)):
        land_map[i] = [int(j) for j in land_map[i]]
    graph = gm.Graph.prepare_graph(land_map, False)
    list_of_squares = []
    for i in graph:
        cell_path = gm.Graph.dfs(graph, i)
        if cell_path not in list_of_squares:
            list_of_squares.append(cell_path)
    return sorted([len(x) for x in list_of_squares])


if __name__ == '__main__':
    print("Example:")
    print(buttons('''
001203
023001
100220'''))

    assert buttons('''
001203
023001
100220''') == [8, 4, 4, 1]

    assert buttons('''
000000
000055
000055''') == [20]

    assert buttons('''
908070
060504
302010''') == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
