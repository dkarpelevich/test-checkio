# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
from graph_module import graph_methods as gm


def prepare_graph(matrix):
    graph = {}
    for i in range(len(matrix)):
        list_in_set = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                list_in_set.append(j)
            if matrix[i][i] == 1 and i in list_in_set:
                list_in_set.remove(i)
        graph.update({i: set(list_in_set)})
    return graph


def prepare_weights(matrix):
    weights_dict = {}
    for i in range(len(matrix)):
        weights_dict.update({i: matrix[i][i]})
    return weights_dict


def min_node_value(graph_list, weights):
    min_value = [0 for _ in range(len(graph_list))]
    for i in range(len(graph_list)):
        for j in graph_list[i]:
            min_value[i] += weights[j]
    return min(min_value)


def capture(matrix):
    graph = prepare_graph(matrix)
    weights = prepare_weights(matrix)
    list_of_paths = []
    list_of_max_times = []
    for i in range(1, len(weights)):
        list_of_paths.append(list(gm.Graph.dfs_paths(graph, 0, i)))
    for node in list_of_paths:
        list_of_max_times.append(min_node_value(node, weights))
    return max(list_of_max_times)


if __name__ == '__main__':
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"

    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"

    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
