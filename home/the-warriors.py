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

def fight(unit_1, unit_2) -> bool:
    while unit_1.health > 0 and unit_2.health > 0:
        unit_2.health -= unit_1.attack
        if unit_2.health <= 0:
            unit_2.is_alive = False
            return True
        unit_1.health -= unit_2.attack
        if unit_1.health <= 0:
            unit_1.is_alive = False
            return False


if __name__ == '__main__':
    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
