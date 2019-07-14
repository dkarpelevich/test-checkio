from graph_module import graph_methods as gm

def g_key(grid, path):
    graph = gm.Graph.prepare_graph(grid, True, True)
    path_list = list(gm.Graph.dfs_paths_recursion(graph, (0, 0), (len(grid)-1, len(grid[0])-1)))
    short_path_list = []
    for i in path_list:
        if len(i) <= path:
            short_path_list.append(i)
    sum_island = [0 for _ in range(len(short_path_list))]
    for item in range(len(short_path_list)):
        for j in short_path_list[item]:
            sum_island[item] += grid[j[0]][j[1]]
    return max(sum_island)

if __name__ == '__main__':
    print("Example:")
    print(g_key([[1, 6, 7],
                 [0, 4, 9],
                 [2, 6, 1]], 4))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert g_key([[1, 6, 7, 2, 4],
    #               [0, 4, 9, 5, 3],
    #               [7, 2, 5, 1, 4],
    #               [3, 3, 2, 2, 9],
    #               [2, 6, 1, 4, 0]], 9) == 46
    #
    # assert g_key([[2, 5, 4, 1, 8],
    #               [0, 4, 9, 5, 3],
    #               [7, 2, 5, 1, 4],
    #               [3, 3, 2, 2, 9],
    #               [2, 6, 1, 4, 1]], 6) == 27
    #
    # assert g_key([[1, 2, 3, 4, 5],
    #               [2, 3, 4, 5, 1],
    #               [3, 4, 5, 1, 2],
    #               [4, 5, 1, 2, 3],
    #               [5, 1, 2, 3, 4]], 25) == 75

    assert g_key([[1, 6],
                  [5, 1]], 2) == 2

    print("Coding complete? Click 'Check' to earn cool rewards!")
