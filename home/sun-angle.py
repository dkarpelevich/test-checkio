def sun_angle(time: str):
    hours_coefficient = 15.0
    minutes_coefficient = 0.25
    hours, minutes = time.split(':')
    result = (int(hours)-6.0) * hours_coefficient + int(minutes) * minutes_coefficient
    if 18 <= int(hours) and int(minutes) > 0 or int(hours) < 6:
        return "I don't see the sun!"

    if result.is_integer():
        result = int(result)

    return result

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("05:00"))

    assert sun_angle("12:15") == 93.75
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
