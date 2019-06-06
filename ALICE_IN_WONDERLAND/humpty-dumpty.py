import math

def checkio(height, width):
    width = width / 2
    height = height / 2
    volume = 4/3 * math.pi * width ** 2 * height
    if height > width:  # Prolate
        e = math.sqrt(1 - width ** 2 / height ** 2)
        area = 2 * math.pi * width**2 * (1 + height/(width*e) * math.asin(e))
    elif height < width:
        e = math.sqrt(1 - height ** 2 / width ** 2)
        area = 2 * math.pi * width**2 * (1 + (1-e**2)/e * math.atanh(e))
    else:
        area = 4 * math.pi * width**2
    return [round(volume, 2), round(area, 2)]


if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"