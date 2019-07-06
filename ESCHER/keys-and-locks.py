"""
s
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
clockwise = list(zip(*s[::-1]))
[(7, 4, 1), (8, 5, 2), (9, 6, 3)]
counterclockwise = list(zip(*s))[::-1]
[(3, 6, 9), (2, 5, 8), (1, 4, 7)]
around = list(zip(*clockwise[::-1]))
[(9, 8, 7), (6, 5, 4), (3, 2, 1)]
"""

def remove_redundant_0_lines(matrix):
    return list(filter(lambda b: b != ['0']*len(matrix[1])
                                 and b != tuple('0')*len(matrix[1])
                                 and b != [], matrix))

def turn_matrix_to_90_degrees(matrix):
    return list(zip(*matrix[::-1]))

def keys_and_locks(lock, some_key):
    # list from string
    list_lock = lock.split('\n')
    list_key = some_key.split('\n')

    # separate string to single letters
    for j in range(len(list_lock)):
        list_lock[j] = [i for i in list_lock[j]]
    for j in range(len(list_key)):
        list_key[j] = [i for i in list_key[j]]

    # remove redundant '0' rows
    list_lock = remove_redundant_0_lines(list_lock)
    list_key = remove_redundant_0_lines(list_key)

    # turn key and lock to 90 degrees to remove redundant '0' columns
    list_lock = turn_matrix_to_90_degrees(list_lock)
    list_key = turn_matrix_to_90_degrees(list_key)
    list_lock = remove_redundant_0_lines(list_lock)
    list_key = remove_redundant_0_lines(list_key)

    # check if key fits to lock in all positions
    if list_lock == list_key:
        return True
    elif list_lock == turn_matrix_to_90_degrees(list_key):
        return True
    elif list_lock == turn_matrix_to_90_degrees(list_key):
        return True
    elif list_lock == turn_matrix_to_90_degrees(list_key):
        return True
    else:
        return False

if __name__ == '__main__':
    print("Example:")
    print(keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000''') == True

    assert keys_and_locks('''
###0
00#0''',
'''
00000
00000
#0000
###00
0#000
0#000''') == False

    assert keys_and_locks('''
0##0
0#00
0000''',
'''
##000
#0000
00000
00000
00000''') == True

    assert keys_and_locks('''
###0
0#00
0000''',
'''
##00
##00''') == False

    print("Coding complete? Click 'Check' to earn cool rewards!")
