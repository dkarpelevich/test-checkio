class Capital:
    __instance = None
    __city = None

    def __new__(cls, city_name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
            Capital.__city = city_name

        return cls.__instance

    @staticmethod
    def name():
        return Capital.__city


if __name__ == '__main__':
    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Marocco")

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1
