def solve_equation(digits_range, sign, first_addend, second_addend, summa):
    for i in digits_range:
        a = int(first_addend.replace('#', str(i)))
        b = int(second_addend.replace('#', str(i)))
        c = int(summa.replace('#', str(i)))
        if sign == '*':
            if a * b == c:
                return i
        elif sign == '+':
            if a + b == c:
                return i
        else:
            if a - b == c:
                return i
    return -1


def safe_code(equation):
    if '*' in equation:
        first_addend = equation[:equation.index('*')]
        second_addend = equation[equation.index('*') + 1:equation.index('=')]
        sign = '*'
    elif '+' in equation:
        first_addend = equation[:equation.index('+')]
        second_addend = equation[equation.index('+') + 1:equation.index('=')]
        sign = '+'
    else:
        if equation.startswith('-'):
            first_addend = equation[:equation[1:].index('-') + 1]
            second_addend = equation[len(first_addend) + 1:equation.index('=')]
        else:
            first_addend = equation[:equation.index('-')]
            second_addend = equation[equation.index('-') + 1:equation.index('=')]
        sign = '-'
    summa = equation[equation.index('=') + 1:]
    unused_digits = [int(i) for i in list(filter(str.isdigit, equation))]
    if first_addend.startswith('#') or \
            second_addend.startswith('#') or \
            summa.startswith('#'):
        range_start = 1
    else:
        range_start = 0

    digits_range = [x for x in range(range_start, 10) if x not in unused_digits]
    return solve_equation(digits_range, sign, first_addend, second_addend, summa)


if __name__ == '__main__':
    assert safe_code("123*45#=5#088") == 6
