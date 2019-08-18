from itertools import accumulate
from typing import List


def search(rest_points, way, cur=0, min_way=99999):
    result_way = [[]]
    cur_way = sum(map(abs, way))

    if min_way < cur_way:
        return min_way

    if not rest_points:
        cur_way += cur

        if min_way > cur_way:
            result_way[0] = way + [-cur]

        return [min_way, cur_way][min_way > cur_way]

    for i, (p, t) in enumerate(rest_points):
        min_way = search(rest_points[:i] + rest_points[i + 1:],
                         way + [p - cur, t - p], t, min_way)

    return min_way

def delivery_drone(orders: List[int]) -> int:
    orders = [(i, d) for i, d in enumerate(orders) if d]

    rs = search(orders, [])
    # steps = list(accumulate(result_way[0]))

    return rs