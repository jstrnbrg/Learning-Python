#While loopsself.

#A while-loop will keep executing the code block under it as long as a boolean expression is True.

numbers = []



def test(up, inc):
    for i in range(0, up):
        i = i * inc
        print(f"At the top i is: {i}")
        numbers.append(i)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")



test(11, 2)
