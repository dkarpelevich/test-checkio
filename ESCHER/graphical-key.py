def g_key(grid, path):
    H = len(grid)
    W = len(grid[0])
    valid = [(x, y) for x in range(H) for y in range(W)]
    res = []

    def pathfinder(x, y, step, vlist, Sm):
        if not (x, y) in vlist: return 0
        if path - step < H - x - 1 or path - step < W - y - 1: return 0
        if step == path:
            if x < H - 1 or y < W - 1: return 0
            res.append(Sm + grid[x][y])
            return 1
        vlist.remove((x, y))
        for (a, b) in [(0, -1), (0, 1), (-1, -1), (-1, 1), (-1, 0), (1, -1), (1, 0), (1, 1)]:
            z = pathfinder(x + a, y + b, step + 1, vlist[:], Sm + grid[x][y])
        return 1

    if H * W == path: return sum([sum(x) for x in grid])

    pathfinder(0, 0, 1, valid, 0)

    return max(res)


if __name__ == '__main__':
    print("Example:")
    print(g_key([[1, 6, 7, 2, 4],
                 [0, 4, 9, 5, 3],
                 [7, 2, 5, 1, 4],
                 [3, 3, 2, 2, 9],
                 [2, 6, 1, 4, 0]], 9))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert g_key([[1, 6, 7, 2, 4],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 0]], 9) == 46

    assert g_key([[2, 5, 4, 1, 8],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 1]], 6) == 27

    assert g_key([[1, 2, 3, 4, 5],
                  [2, 3, 4, 5, 1],
                  [3, 4, 5, 1, 2],
                  [4, 5, 1, 2, 3],
                  [5, 1, 2, 3, 4]], 25) == 75

    assert g_key([[1, 6],
                  [5, 1]], 2) == 2

    print("Coding complete? Click 'Check' to earn cool rewards!")