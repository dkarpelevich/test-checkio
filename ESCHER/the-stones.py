def stones(pile: int, moves):
    results_list = [False for _ in range(pile+1)]
    results_list[0] = True
    for i in range(2, len(results_list)):
        for j in moves:
            if i - j >= 0:
                if not results_list[i - j]:
                    results_list[i] = True
                    break
                else:
                    results_list[i] = False
    return 1 if results_list[pile] else 2

if __name__ == '__main__':
    print("Example:")
    # print(stones(4, [1, 3]))
    assert stones(17, [1, 3, 4]) == 2
    assert stones(17, [1, 3, 4, 6, 9]) == 1
    assert stones(99, [1]) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
