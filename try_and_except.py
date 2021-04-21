for i in range (5):
    score = input("Enter a score:")

    try:
        point = float(score)

    except:
        point = -1

    if point > 1.0 or point < 0.0:
        print("Invalid input\nPlease enter a valid score!!!")
    elif point >= 0.9:
        print("A")
    elif point >= 0.8:
        print("B")
    elif point >= 0.7:
        print("C")
    elif point >= 0.6:
        print("D")
    elif point < 0.6:
        print("F")

