from numbers_to_words_representation import all_numbers_representation as anr


def secret_room(number: int) -> int:
    list_numbers = []
    for i in range(1, number+1):
        list_numbers.append(anr(i))
    max_door = anr(number)
    return sorted(list_numbers).index(max_door) + 1

if __name__ == '__main__':
    print("Example:")
    print(secret_room(5))

    assert secret_room(5) == 1  # five, four, one, three, two
    assert secret_room(3) == 2  # one, three, two
    assert secret_room(1000) == 551
    print("Coding complete? Click 'Check' to earn cool rewards!")
