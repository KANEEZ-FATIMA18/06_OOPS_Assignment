class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting.")

my_car = Car("Toyota")
print(my_car.brand)  # Output: Toyota
my_car.start()  # Output: Toyota is starting.