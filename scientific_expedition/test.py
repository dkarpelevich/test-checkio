graph = {'A': {'B', 'C'},
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': {'B', 'F'},
         'F': set(['C', 'E']),
         'G': set(['H']),
         'H': set(['G']),
         'I': set()}


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


print(dfs(graph, 'I'))
