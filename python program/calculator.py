sum = 0
while (True):
    userInputNumber = input("Enter the price or press q to quit:\n");
    if (userInputNumber != 'q'):
        sum = sum + int(userInputNumber)
        print(f" total price:{sum}")
    else:
        print(f"your Total Amount is{sum}.Thanks You Much")
        break
