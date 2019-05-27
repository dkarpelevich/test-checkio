class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True if self.health > 0 else False


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5


class Rookie(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 1

class Army:
    def __init__(self):
        self.list_of_units = []

    def add_units(self, units, units_amount: int):
        self.list_of_units += [units() for _ in range(units_amount)]


class Battle:
    @staticmethod
    def fight(army_1, army_2) -> bool:
        army_1_unit = len(army_1.list_of_units) - 1
        army_2_unit = len(army_2.list_of_units) - 1
        while army_2_unit >= 0 and army_1_unit >= 0:
            if fight(army_1.list_of_units[army_1_unit], army_2.list_of_units[army_2_unit]):
                army_2_unit -= 1
            else:
                army_1_unit -= 1
            if army_2_unit < 0:
                return True
            elif army_1_unit < 0:
                return False

def fight_conditions(a, b):
    defense = b.defense if isinstance(b, Defender) else 0
    vampirism = a.vampirism if isinstance(a, Vampire) else 0
    if a.attack > defense:
        attack = a.attack - defense
        b.health -= attack
        a.health += int(attack * vampirism)


def fight(unit_1, unit_2) -> bool:
    while unit_1.health > 0 and unit_2.health > 0:
        fight_conditions(unit_1, unit_2)
        if unit_2.health <= 0:
            unit_2.is_alive = False
            return True

        fight_conditions(unit_2, unit_1)
        if unit_1.health <= 0:
            unit_1.is_alive = False
            return False


if __name__ == '__main__':
    unit_one = Warrior()
    unit_two = Rookie()
    # noinspection PyTypeChecker
    fight(unit_one, unit_two)
    print(unit_one.health)

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    # noinspection PyTypeChecker
    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
