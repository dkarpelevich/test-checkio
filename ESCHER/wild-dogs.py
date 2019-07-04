from math import sqrt

def linear_equation_coefficient(x1, y1, x2, y2) -> tuple:
    try:
        k = (y2 - y1) / (x2 - x1)
        b = (y1 * x2 - x1 * y2) / (x2 - x1)
    except ZeroDivisionError:
        k = y2 - y1
        b = y1 * x2 - x1 * y2
    return k, b

def calculate_distance(k, b):
    return round(abs(b / sqrt(k**2 + 1)), 2)

def wild_dogs(coords: list) -> float:
    dict_coeff_for_coord = dict()
    for i, e in list(enumerate(coords)):
        dict_coeff_for_coord[e] = \
            [linear_equation_coefficient(
                coords[j][0], coords[j][1], coords[i][0], coords[i][1])
             for j in range(len(coords))]

    dict_coeff_with_count = {}
    for keys in dict_coeff_for_coord:
        dict_coeff_for_coord[keys].remove((0, 0))
        for values in dict_coeff_for_coord[keys]:
            dict_coeff_with_count[values] =\
                dict_coeff_for_coord[keys].count(values)

    list_all_coeff_with_max_count = \
        [i for i in dict_coeff_with_count.keys()
         if dict_coeff_with_count[i] == max(dict_coeff_with_count.values())]

    min_distance = calculate_distance(list_all_coeff_with_max_count[0][0],
                                      list_all_coeff_with_max_count[0][1])
    for coeff in list_all_coeff_with_max_count:
        if calculate_distance(coeff[0], coeff[1]) <= min_distance:
            min_distance = calculate_distance(coeff[0], coeff[1])
    return min_distance


if __name__ == '__main__':
    print("Example:")
    print(wild_dogs([(7, 122), (8, 139), (9, 156),
                     (10, 173), (11, 190), (-100, 1)]))

    assert wild_dogs([(7, 122), (8, 139), (9, 156),
                      (10, 173), (11, 190), (-100, 1)]) == 0.18

    assert wild_dogs([(6, -0.5), (3, -5), (1, -20)]) == 3.63

    assert wild_dogs([(10, 10), (13, 13), (21, 18)]) == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
