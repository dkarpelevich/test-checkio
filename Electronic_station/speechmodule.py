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


def checkio(number: int) -> str:
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


if __name__ == '__main__':
    print(checkio(1000))
    assert checkio(12) == 'twelve', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')