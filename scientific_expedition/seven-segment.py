import itertools

numbers_collection = [
    {'a', 'b', 'c', 'd', 'e', 'f'},
    {'b', 'c'},
    {'a', 'b', 'g', 'e', 'd'},
    {'a', 'b', 'g', 'c', 'd'},
    {'b', 'g', 'c', 'f'},
    {'a', 'f', 'g', 'c', 'd'},
    {'a', 'c', 'd', 'e', 'f', 'g'},
    {'a', 'b', 'c'},
    {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    {'a', 'b', 'c', 'd', 'f', 'g'},
]


def prepare_sets(seg):
    first_seg, second_seg = set(), set()
    for i in seg:
        if i.isupper():
            first_seg.update(i.lower())
        else:
            second_seg.update(i.lower())
    return first_seg, second_seg


def find_combinations(lit_seg, broken_seg):
    count = 0
    for L in range(0, len(broken_seg) + 1):
        for subset in itertools.combinations(broken_seg, L):
            union_lit_and_broken = lit_seg.union(set(subset))
            for item in numbers_collection:
                if item == union_lit_and_broken:
                    count += 1
    return count


def seven_segment(lit_seg, broken_seg):
    first_lit_seg, second_lit_seg = prepare_sets(lit_seg)
    first_broken_seg, second_broken_seg = prepare_sets(broken_seg)
    first_number = find_combinations(first_lit_seg, first_broken_seg)
    second_number = find_combinations(second_lit_seg, second_broken_seg)
    return first_number * second_number


if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
