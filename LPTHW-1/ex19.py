def che_and_cra(cheese, boxes):
    print(f"You have {cheese} cheeses!")
    print(f"You have {boxes} of crackers")
    print("Enough for a party")

print("we can just give the function numbers directly:")
che_and_cra(20, 30)

print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_boxes = 50

che_and_cra(amount_of_cheese, amount_of_boxes)

print("We can even do math inside too:")
che_and_cra(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
che_and_cra(amount_of_cheese + 100, amount_of_boxes + 1000)
