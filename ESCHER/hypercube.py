def check_hypercube_letters_in_grid(grid, THE_DICT):
    grid = [j.lower() for i in grid for j in i]
    for key in THE_DICT:
        if key not in grid:
            return False

def find_neighbour(grid, coord: tuple, next_letter: str):
    return_set = set()
    try:
        if coord[0] - 1 >= 0 and next_letter == grid[coord[0] - 1][coord[1]]:   # up
            return_set.add((coord[0] - 1, coord[1]))
        if coord[0] + 1 <= len(grid) - 1 and next_letter == grid[coord[0] + 1][coord[1]]:  # down
            return_set.add((coord[0] + 1, coord[1]))
        if coord[1] - 1 >= 0 and next_letter == grid[coord[0]][coord[1] - 1]:  # left
            return_set.add((coord[0], coord[1] - 1))
        if coord[1] + 1 <= len(grid[0]) - 1 and next_letter == grid[coord[0]][coord[1] + 1]:  # right
            return_set.add((coord[0], coord[1] + 1))
    except TypeError:
        pass
    return return_set

def hypercube(grid):
    hypercube_list = ['h', 'y', 'p', 'e', 'r', 'c', 'u', 'b', 'e']
    THE_DICT = {char: set() for char in hypercube_list}
    check_hypercube_letters_in_grid(grid, THE_DICT)

    # matrix to lowercase and 'h' initialize
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].isupper():
                grid[i][j] = grid[i][j].lower()
            if grid[i][j] == 'h':
                THE_DICT['h'].add((i, j))
    if THE_DICT['h'] == set():
        return False

    for number, key in list(enumerate(hypercube_list))[:len(hypercube_list) - 1]:
        for coord in THE_DICT[key]:
            THE_DICT[hypercube_list[number + 1]].update(find_neighbour(grid, coord, hypercube_list[number + 1]))
        if THE_DICT[hypercube_list[number + 1]] == {None}:
            return False
        if key == 'r':
            THE_DICT['e'] = {None}
    return True

if __name__ == '__main__':
    assert hypercube([
               ['w', 'y', 'w'],
               ['y', 'h', 'y'],
               ['w', 'y', 'w'],
               ['w', 'p', 'w'],
               ['w', 'e', 'w'],
               ['w', 'r', 'w'],
               ['w', 'c', 'w'],
               ['w', 'u', 'w'],
               ['w', 'b', 'w'],
               ['w', 'e', 'w']]) == True

    assert hypercube([["h", "y", "p", "e", "w"],
                      ["b", "u", "c", "r", "f"],
                      ["h", "e", "r", "b", "e"],
                      ["y", "p", "c", "u", "q"],
                      ["y", "p", "c", "u", "q"]]) == True
