FIRST_TEN = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "one thousand"

def first_ten_representation(number: int) -> str:
    if len(str(number)) == 1:
        return FIRST_TEN[number]
    else:
        raise Exception('More then 1 digit in first ten')

def other_tens_representation(number: int) -> str:
    breaked_number_10 = number // 10
    if len(str(number)) == 2:
        if breaked_number_10 == 1:
            return SECOND_TEN[number - 10]
        else:
            first_part = OTHER_TENS[breaked_number_10 - 2]
            second_part = FIRST_TEN[number - breaked_number_10*10]
            return " ".join([first_part, second_part]).rstrip()
    else:
        raise Exception('More then 2 digits in second ten')


def all_numbers_representation(number: int) -> str:
    breaked_number_100 = number // 100
    tens_part = number - breaked_number_100 * 100
    if len(str(number)) == 4:
        return THOUSAND
    elif len(str(number)) == 3:
        first_part = FIRST_TEN[breaked_number_100] + " " + HUNDRED
        if tens_part >= 10:
            second_part = other_tens_representation(tens_part)
        else:
            second_part = first_ten_representation(tens_part)
        return ' '.join([first_part, second_part]).rstrip()
    elif len(str(number)) == 2:
        return other_tens_representation(number)
    elif len(str(number)) == 1:
        return first_ten_representation(number)
    else:
        return 'Incorrect number!'

def secret_room(number: int) -> int:
    list_numbers = []
    for i in range(1, number+1):
        list_numbers.append(all_numbers_representation(i))
    max_door = all_numbers_representation(number)
    return sorted(list_numbers).index(max_door) + 1

if __name__ == '__main__':
    print("Example:")
    print(secret_room(5))

    assert secret_room(5) == 1 #five, four, one, three, two
    assert secret_room(3) == 2 #one, three, two
    assert secret_room(1000) == 551
    print("Coding complete? Click 'Check' to earn cool rewards!")
