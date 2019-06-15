def calculate_amount_of_rows(message, key):
    matrix = [[]]
    for j in range(len(str(key))):
        for i in message:

         matrix[j] =9
'''
Четный ключ:
4 + 4//2
6
3 + 3//2
4

Нечетный ключ, нечетная строка:
3 + 3//2
4

Нечетный ключ, четная строка:
3 + 3//2 + 1
5
'''

'''
0  1 2  3 4  5
qw e rt y ui o

1 - 2  +1
2 - 3  +1
3 - 5  +2
4 - 6  +2
5 - 8  +3
6 - 9  +3
7 - 11 +4
8 - 12 +4
9 - 14 +5
10 -15 +5
11 -17 +6
12 -18 +6
13 -20 +7
'''


def decode_amsco(message, key):
    calculate_amount_of_rows(message, key)


if __name__ == '__main__':
    decode_amsco("oruoreemdstmioitlpslam", 4123)
    # assert decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    # assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
    # assert decode_amsco('hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"