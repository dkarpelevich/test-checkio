def count_table(first_bin, second_bin, operator):
    summ = 0
    for i in range(len(first_bin)):
        raw = str()
        for j in range(len(second_bin)):
            if operator == '&':
                raw += str(int(first_bin[i]) & int(second_bin[j]))
            elif operator == '|':
                raw += str(int(first_bin[i]) | int(second_bin[j]))
            elif operator == '^':
                raw += str(int(first_bin[i]) ^ int(second_bin[j]))
            else:
                return Exception('Incorrect operator!')
        summ += int(raw, 2)
    return summ

def checkio(first, second):
    first_bin = '{0:b}'.format(first)
    second_bin = '{0:b}'.format(second)
    And = count_table(first_bin, second_bin, '&')
    Or = count_table(first_bin, second_bin, '|')
    XOr = count_table(first_bin, second_bin, '^')
    return And + Or + XOr

if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18