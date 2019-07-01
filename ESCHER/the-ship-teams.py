def two_teams(sailors):
    first_team, second_team = [], []
    for i in sailors:
        if 20 <= sailors[i] <= 40:
            second_team.append(i)
        else:
            first_team.append(i)
    return [
        sorted(first_team),
        sorted(second_team)
    ]


if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    assert two_teams({
        'Smith': 34,
        'Wesson': 22,
        'Coleman': 45,
        'Abrahams': 19}) == [
            ['Abrahams', 'Coleman'],
            ['Smith', 'Wesson']
            ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
            ['Fernandes', 'Kale', 'McCortney'],
            ['Johnson']
            ]
    print("Coding complete? Click 'Check' to earn cool rewards!")
