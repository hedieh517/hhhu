class FoodItem:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    def __str__(self):
        return f"{self.name} - {self.base_price}"

    def calculate_cost(self):
        return self.base_price


class Pizza(FoodItem):
    def __init__(self, name, base_price):
        super().__init__(name, base_price)

        size = input("اندازه غذا را وارد کنید (s/m/l): ")

        if size == 's':
            self.size = 'small'
            self.zarib = 1
        elif size == 'm':
            self.size = 'medium'
            self.zarib = 1.2
        elif size == 'l':
            self.size = 'large'
            self.zarib = 1.5
        else:
            print("اندازه نامعتبر است!")
            exit()

    def calculate_cost(self):
        return self.base_price * self.zarib


class Burger(FoodItem):
    def __init__(self, name, base_price):
        super().__init__(name, base_price)

        is_double = input("آیا دوبل باشد؟ (T/F): ")

        if is_double.lower() == 't':
            self.is_double = True
            self.base_price *= 1.3
        elif is_double.lower() == 'f':
            self.is_double = False
        else:
            print("ورودی نامعتبر!")
            exit()


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, count):
        self.items.append((item, count))

    def calculate_cost(self):
        total = 0
        for item, count in self.items:
            total += item.calculate_cost() * count
        return total
