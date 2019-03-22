from abc import ABC, abstractmethod

class Unit:
    def __init__(self, type_unit, army_type, name):
        self.type_unit = type_unit
        self.army_type = army_type
        self.name = name
        self.specialization = 'default_unit'

    def introduce(self):
        return self.type_unit + ' ' + self.name + ', ' + self.army_type + ' ' + self.specialization


class Swordsman(Unit):
    def __init__(self, type_unit, army_type, name):
        super().__init__(type_unit, army_type, name)
        self.specialization = 'swordsman'


class Lancer(Unit):
    def __init__(self, type_unit, army_type, name):
        super().__init__(type_unit, army_type, name)
        self.specialization = 'lancer'


class Archer(Unit):
    def __init__(self, type_unit, army_type, name):
        super().__init__(type_unit, army_type, name)
        self.specialization = 'archer'


class Army(ABC):
    def __init__(self):
        self.army_type = 'default_army_type'

    @abstractmethod
    def train_swordsman(self, name):
        pass

    @abstractmethod
    def train_lancer(self, name):
        pass

    @abstractmethod
    def train_archer(self, name):
        pass


class EuropeanArmy(Army):
    def __init__(self):
        super().__init__()
        self.army_type = 'European'

    def train_swordsman(self, name):
        type_unit = 'Knight'
        return Swordsman(type_unit, self.army_type, name)

    def train_lancer(self, name):
        type_unit = 'Raubritter'
        return Lancer(type_unit, self.army_type, name)

    def train_archer(self, name):
        type_unit = 'Ranger'
        return Archer(type_unit, self.army_type, name)


class AsianArmy(Army):
    def __init__(self):
        super().__init__()
        self.army_type = 'Asian'

    def train_swordsman(self, name):
        type_unit = 'Samurai'
        return Swordsman(type_unit, self.army_type, name)

    def train_lancer(self, name):
        type_unit = 'Ronin'
        return Lancer(type_unit, self.army_type, name)

    def train_archer(self, name):
        type_unit = 'Shinobi'
        return Archer(type_unit, self.army_type, name)


if __name__ == '__main__':
    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"

    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"
