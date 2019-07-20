def check_hyp(i, j, grid, n_h, checked):
    hypercube = 'hypercube'
    if i \
            not in range(0, len(grid)) \
            or j not in range(0, len(grid[0])) \
            or (i, j) in checked:
        return False
    if grid[i][j].lower() != hypercube[n_h]:
        return False
    else:
        if n_h == len(hypercube) - 1:
            return True
        directions = [
            (-1, 0),
            (0, -1), (0, 1),
            (1, 0)
        ]
        return any(
            [check_hyp(i + di, j + dj, grid, n_h + 1, checked+[(i, j)]) for
             di, dj in directions])


def hypercube(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].lower() == 'h':
                if check_hyp(i, j, grid, 0, []):
                    return True
    return False

if __name__ == '__main__':
    assert hypercube([
               ['w', 'y', 'w', 'w', 'w', 'w'],
               ['y', 'h', 'y', 'y', 'y', 'y'],
               ['w', 'y', 'w', 'w', 'w', 'w'],
               ['w', 'p', 'w', 'e', 'w', 'w'],
               ['w', 'e', 'w', 'b', 'w', 'w'],
               ['w', 'r', 'c', 'u', 'w', 'w']]) == True

    # assert hypercube([["h", "y", "p", "e", "w"],
    #                   ["b", "u", "c", "r", "f"],
    #                   ["h", "e", "r", "b", "e"],
    #                   ["y", "p", "c", "u", "q"],
    #                   ["y", "p", "c", "u", "q"]]) == True
