from graph_module import graph_methods as gm

def buttons(land_map):
    land_map = land_map.split('\n')[1:]
    for i in range(len(land_map)):
        land_map[i] = [int(j) for j in land_map[i]]
    list_of_squares = gm.Graph.island(land_map, False)
    sum_island = [0 for _ in range(len(list_of_squares))]
    for item in range(len(list_of_squares)):
        for j in list_of_squares[item]:
            sum_island[item] += land_map[j[0]][j[1]]
    return sorted(sum_island, reverse=True)


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
