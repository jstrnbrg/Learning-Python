from sys import exit

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> (left or right)\n" )

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

# def start first prints a few statements. Then it asks for an input
#and saves that input to the var choice.
#then we have an if, elif, else statement, if triggers def bear_room()
#elif triggers def cthulhu_room()
#else triggers def dead() with the sentence as the input var 'why'

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> take honey or taunt bear or open door\n")

        if choice == "take honey":
            dead("Eaten by bear")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")

#def bear_room first prints a few statements and sets var bear_moved to False
#then it asks for input and saves it to var choice
# then we have an if, elif, elif, elif, else statement


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> (flee or head)\n")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input(">\n")

    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, not greedy, win!")
        exit(0)
    else:
        dead("You're too greedy!")



def dead(why):
    print(why, "Good job!")
    exit(0)



start()
