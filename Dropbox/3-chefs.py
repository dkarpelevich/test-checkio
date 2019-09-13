class AbstractCook:
    def __init__(self, dish, beverage):
        self.dish, self.beverage = dish, beverage
        self.food, self.drink, self.total_amount = 0, 0, 0

    def add_food(self, food_amount, food_price):
        self.food += food_amount * food_price

    def add_drink(self, drink_amount, drink_price):
        self.drink += drink_amount * drink_price

    def total(self):
        self.total_amount = self.food + self.drink
        return "{dish}: {food}, {beverage}: {drink}, Total: {total_amount}". \
            format(dish=self.dish, food=self.food, beverage=self.beverage, drink=self.drink,
                   total_amount=self.total_amount)


class JapaneseCook(AbstractCook):
    def __init__(self):
        super().__init__('Sushi', 'Tea')


class RussianCook(AbstractCook):
    def __init__(self):
        super().__init__('Dumplings', 'Compote')


class ItalianCook(AbstractCook):
    def __init__(self):
        super().__init__('Pizza', 'Juice')


if __name__ == '__main__':
    client_1 = JapaneseCook()
    client_1.add_food(2, 20)
    client_1.add_drink(5, 4)
    assert client_1.total() == "Sushi: 40, Tea: 20, Total: 60"

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_drink(5, 20)
    assert client_2.total() == "Dumplings: 40, Compote: 100, Total: 140"

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_drink(2, 10)
    assert client_3.total() == "Pizza: 40, Juice: 20, Total: 60"
