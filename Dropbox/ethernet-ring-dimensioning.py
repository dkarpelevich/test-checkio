ETHERNET = (100, 40, 10, 1, 0.1)  # Ethernet bandwidth capacity in Gbps
from graph_module import graph_methods as gm


def prepare_graph(ring: str) -> dict:
    graph = {}
    for i in range(len(ring) - 1):
        graph.update({ring[i]: {ring[i - 1], ring[i + 1]}})
    graph.update({ring[len(ring) - 1]: {ring[len(ring) - 2], ring[0]}})
    return graph


def find_shortest_path(ring, flows):
    graph = prepare_graph(ring)
    shortest_paths = {}
    ring = [j for j in ring]
    for s in flows:
        unsorted_paths = list(gm.Graph.dfs_paths(graph, s[0][0], s[0][1]))
        key = lambda vertex: [ring.index(c) for c in vertex]
        if ring.index(s[0][0]) < ring.index(s[0][1]):
            paths = sorted(unsorted_paths, key=key)
        else:
            paths = sorted(unsorted_paths, key=key, reverse=True)

        shortest_paths.update({s[0]: min(paths, key=lambda x: len(x))})
    return shortest_paths


def checkio(ring, *flows):
    shortest_paths = find_shortest_path(ring, flows)
    traffic_dict = {}
    for i in flows:
        key = shortest_paths[i[0]]
        for j in range(len(key) - 1):
            link = tuple(sorted((key[j], key[j + 1])))
            traffic_dict[link] = traffic_dict.get(link, 0) + i[1]
    res_list = [0 for _ in range(5)]
    for traffic in traffic_dict.values():
        if traffic <= ETHERNET[4]:
            res_list[4] += 1
        elif traffic > ETHERNET[0]:
            res_list[0] += (traffic // 100) if traffic % 100 == 0 else (traffic // 100) + 1
        else:
            for i in range(len(ETHERNET) - 1):
                if ETHERNET[i] >= traffic > ETHERNET[i + 1]:
                    res_list[i] += 1
                    break
    return res_list


if __name__ == '__main__':
    checkio("ABCDEFGH", ["AE", 170], ["EA", 10000], ["HF", 1])
