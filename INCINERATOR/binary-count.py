def binary_count(number):
    return bin(number).count('1')


if __name__ == '__main__':
    assert binary_count(5) == 2
