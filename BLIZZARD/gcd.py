from math import gcd

def great_common_divisor(*args):
    res = gcd(args[0], args[1])
    for i in range(2, len(args)):
        res = gcd(res, args[i])
    return res

if __name__ == '__main__':
    print(great_common_divisor(8, 4, 24))
