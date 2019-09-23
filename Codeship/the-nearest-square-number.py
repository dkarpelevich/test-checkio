from math import sqrt

def nearest_square(number):
    return round(sqrt(number))**2

#
# def nearest_square(number):
#     up = down = -1
#     for i in range(number, 1000000):
#         if i % sqrt(i) == 0.0:
#             up = i
#             break
#
#     for i in range(number, 0, -1):
#         if i % sqrt(i) == 0.0:
#             down = i
#             break
#     return up if up - number < number - down and up > 0 else down

if __name__ == '__main__':
    assert nearest_square(998500)