class User():
    def __init__(self, first, last, gender, age):
        self.first = first
        self.last = last
        self.age = age
        self.gender = gender
        self.attempts = 0

    def describe(self):
        if self.gender is "m":
            print(f"This user's name is {self.first} {self.last}, he is {self.age} years old")
        else:
            print(f"This user's name is {self.first} {self.last}, she is {self.age} years old")

    def inc_attempts(self):
        self.attempts += 1
        print(f"you tried {self.attempts} times")

    def reset_attempts(self):
        self.attempts = 0
        print(f"Attempts was reset to: {self.attempts}")


u1 = User("Amy", "Wilson", "f", 20)
#u2 = User("John", "Stern", "m", 19)

u1.describe()
#u2.describe()

u1.inc_attempts()
u1.inc_attempts()
u1.inc_attempts()
u1.reset_attempts()
u1.inc_attempts()
