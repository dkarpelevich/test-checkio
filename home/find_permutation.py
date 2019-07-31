from itertools import permutations


def permutation(*args, multiply):
    if len(args) % 2 != 0:
        return Exception('Error! Odd number!')
    permutations_list = list(permutations(args, len(args)))
    for combination in permutations_list:
        fpstr, spstr = str(), str()
        for i in combination[:int(len(combination)/2)]:
            fpstr += str(i)
        for j in combination[int(len(combination)/2):]:
            spstr += str(j)
        if int(fpstr) * multiply == int(spstr):
            return '{0}{1}{2}={3}'.format(fpstr, '*', multiply, spstr)
    return Exception('No combinations found!')

print(permutation(1, 2, 4, 5, 6, 9, multiply=5))
