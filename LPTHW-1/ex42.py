## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has a name name
        self.name = name
## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## cat has-a name name
        self.name = name
## Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None 28

class Employee(Person):
    def __init__(self, name, salary):
    ## ??hmm what is this strange magic?
    super(Employee, self).__init__(name)
    ##Employee has-a sala   ry
    self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
