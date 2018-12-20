#Is-A, Has-A, Objects, and Classes

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog ia-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat ia-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

#Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## Emplyee has a super function????? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary equal to var salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Hailbut is-a Fish
class Halibut(Fish):
    pass

#Rover is-a dog, Set rover to an instance of Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## marry is-a Person
mary = Person("Mary")

#marry has-a pet rover
mary.pet = satan

#Frank is-a Employee that makes 120000
frank = Employee("Frank", 120000)

#frank has-a pet rover
frank.pet = rover

#Flipper is-a instance of Fish()
flipper = Fish()

## course is a instance of Salmon()
crouse = Salmon()

## Harry is-a instance of Hailbut()
harry = Halibut()
