from graph_module import graph_methods as gm


def disconnected_users(net, users, source, crushes):
    graph = {}
    for connect in net:
        first_connect = graph.get(connect[0], set())
        first_connect.add(connect[1])
        graph.update({connect[0]: first_connect})
        second_connect = graph.get(connect[1], set())
        second_connect.add(connect[0])
        graph.update({connect[1]: second_connect})
    for keys, items in graph.items():
        if keys in crushes:
            graph[keys] = set()
        if items & set(crushes):
            graph.update({keys: items - set(crushes)})
    connected_users = gm.Graph.dfs(graph, source)
    count = 0
    if source in crushes:
        connected_users.remove(source)
    for i in users:
        if i not in connected_users:
            count += users[i]
    return count


if __name__ == '__main__':
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['A']) == 100, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"

    print('Done. Try to check now. There are a lot of other tests')