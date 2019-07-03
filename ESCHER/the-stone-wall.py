def stone_wall(wall):
    wall = wall.split('\n')
    wall = wall[1:len(wall)-1]
    for j in range(len(wall)):
        wall[j] = [i for i in wall[j]]
    wall = list(zip(*wall[::-1]))
    list_0 = []
    for i in wall:
        list_0.append(i.count('0'))
    return list_0.index(max(list_0))

if __name__ == '__main__':
    print("Example:")
    print(stone_wall('''
##########
####0##0##
00##0###00
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
