def dist(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

def navigation(seaside):
    Y = C = M = S = [0, 0]
    for row, column in list(enumerate(seaside)):
        if 'Y' in column:
            Y = [row, column.index('Y')]
        if 'C' in column:
            C = [row, column.index('C')]
        if 'M' in column:
            M = [row, column.index('M')]
        if 'S' in column:
            S = [row, column.index('S')]
    YC = dist(Y, C)
    YM = dist(Y, M)
    YS = dist(Y, S)
    return YC + YM + YS


if __name__ == '__main__':
    print("Example:")
    print(navigation([[ 0,  0,  0, 0, 'C'],
                      [ 0, 'Y', 0, 0,  0],
                      [ 0,  0,  0, 0,  0],
                      ['M', 0,  0, 0, 'S']]))

    assert navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[ 0,  0, 'C'],
                       [ 0, 'S', 0],
                       ['M','Y', 0]]) == 4

    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")
