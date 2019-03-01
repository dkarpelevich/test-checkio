def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def prepare_graph(matrix):
    print(len(matrix))
    graph = {}
    for i in range(len(matrix)):
        list_in_set = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                list_in_set.append(j)
        graph.update({i: set(list_in_set)})
    print(graph)
    return graph


def prepare_weights(matrix):

    pass


matrix = [[0, 1, 0, 1, 0, 1],
          [1, 8, 1, 0, 0, 0],
          [0, 1, 2, 0, 0, 1],
          [1, 0, 0, 1, 1, 0],
          [0, 0, 0, 1, 3, 1],
          [1, 0, 1, 0, 1, 2]]
graph = prepare_graph(matrix)
print(list(dfs_paths(graph, 0, 2)))

'''
if __name__ == '__main__':
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
'''

"""
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
"""
