def computepay(hours, rate):
    hours = input("Hours: ")
    rate = input("Rate: ")
    try:
        hours = int(hours)
        rate = int(rate)
        if hours > 40:
            extra_hours = hours - 40
            pay = (extra_hours * (1.5*rate)) + (40 * rate)
        else:
            pay = hours * rate
        print(pay)
    except:
        print("Please give number input")

computepay()
