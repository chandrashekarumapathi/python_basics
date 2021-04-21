hours = input("Enter the hours worked:")
x = input("Enter the rate per hour:")
gross_pay = 0

try:
    rate = float(x)
    hours = int(hours)

except:
    rate = -1

if rate == -1:
    print("Invalid input!!!\nPlease enter correctly!!!")
elif hours <= 40:
    gross_pay = hours * rate
    print(gross_pay)
elif hours > 40:
    gross_pay = (40 * rate) + (int(hours) - 40) * (1.5 * rate)
    print(gross_pay)
