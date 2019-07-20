def safe_pawns(pawns: set) -> int:
    v = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    amount = 0
    for i in pawns:
        ver_left = v[v.index(i[0]) - 1] if v.index(i[0]) - 1 >= 0 else None
        hor = str(int(i[1]) - 1)
        try:
            ver_right = v[v.index(i[0]) + 1]
        except IndexError:
            ver_right = 'g'
        if str(ver_left)+hor in pawns or ver_right+hor in pawns:
            amount += 1
    return amount

if __name__ == '__main__':
    # assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    # assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns({"a1", "b2", "h1", "h8", "a8", "h7"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")