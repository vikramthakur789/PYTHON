# Topic: Simple class example
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show(self):
        print(f"Car: {self.brand} {self.model}")

c1 = Car("Tesla", "Model S")
c1.show()
