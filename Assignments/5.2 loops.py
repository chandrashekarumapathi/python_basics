my_list = []
error_case = ""
largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        num = float(num)

    except:
        num = -1

    my_list.append(num)
    for i in my_list:
        if i > largest:
            largest = i

    for j in my_list:
        if j == -1:
            continue
        if smallest is None:
            smallest = j
        elif j < smallest:
            smallest = j

    if num == -1:
        error_case = "Invalid input!!!"

print(error_case)
print("Maximum is ", largest)
print("Minimum is ", smallest)




