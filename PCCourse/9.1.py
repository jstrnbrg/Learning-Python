class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.type = cuisine
        self.n_served = 0

    def describe(self):
        print(f"This is a {self.type} restaurant, called {self.name}")

    def open(self):
        print(f"Restaurant {self.name} is open")

    def set_n_served(self, number):
        self.n_served = number

    def increment_served(self, inc):
        self.n_served += inc


restaurant1 = Restaurant("Beanhouse", "asian")
#restaurant2 = Restaurant("Steakhouse", "mexican")
#restaurant3 = Restaurant("TuckTuck", "korean")

restaurant1.describe()
#restaurant2.describe()
#restaurant3.describe()
print(restaurant1.n_served)
restaurant1.set_n_served(100)
print(restaurant1.n_served)
restaurant1.increment_served(10)
print(restaurant1.n_served)
