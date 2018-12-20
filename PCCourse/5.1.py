requested_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'salami', 'rocket']
out_stocks = ['rocket', 'green peppers']

for requested_topping in requested_toppings:
    if requested_topping in out_stocks:
        print(f"Sorry, we are out of that {requested_topping} right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
