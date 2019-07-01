def house(plan):
    plan = plan.split('\n')
    first_height, last_height = 0, 0
    left_border, right_border = [], []
    for line in plan:
        if '#' in line:
            left_border.append(line.index('#'))
            right_border.append(line.rindex('#'))
    try:
        width = max(right_border) - min(left_border) + 1
    except ValueError:
        width = 0
    for i, e in list(enumerate(plan)):
        if '#' in e:
            first_height = i
            break
    for i, e in reversed(list(enumerate(plan))):
        if '#' in e:
            last_height = i
            break

    return width*(last_height - first_height + 1)


if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
##00
''') == 9

    print("Coding complete? Click 'Check' to earn cool rewards!")
