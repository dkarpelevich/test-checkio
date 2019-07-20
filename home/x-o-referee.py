def check_win_line(table):
    for i in table:
        if i == ['X', 'X', 'X']:
            return 'X'
        if i == ['O', 'O', 'O']:
            return 'O'
    if table[0][0] == table[1][1] == table[2][2] == 'X' or \
       table[0][2] == table[1][1] == table[2][0] == 'X':
        return 'X'
    if table[0][0] == table[1][1] == table[2][2] == 'O' or \
       table[0][2] == table[1][1] == table[2][0] == 'O':
        return 'O'
    return 'D'

def checkio(table):
    for i in range(len(table)):
        table[i] = [j for j in table[i]]
    if check_win_line(table) == 'D':
        table = [list(i) for i in list(zip(*table[::-1]))]
        return check_win_line(table)
    else:
        return check_win_line(table)


if __name__ == '__main__':
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"