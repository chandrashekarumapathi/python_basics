def computepay(x, hours):
    try:
        rate = float(x)
        hours = int(hours)

    except:
        rate = -1

    if rate == -1:
        return "Invalid input!!!\nPlease enter correctly!!!"
    elif hours <= 40:
        gross_pay = hours * rate
        return gross_pay
    elif hours > 40:
        gross_pay = (40 * rate) + (int(hours) - 40) * (1.5 * rate)
        return gross_pay


for i in range(4):
    hour = input("Enter the hours worked:")
    rate = input("Enter the rate per hour:")

    print("Pay", computepay(x=rate, hours=hour))
