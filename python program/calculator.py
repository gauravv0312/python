sum = 0
while (True):
    userInput = input("Enter the price or press q to quit:\n");
    if (userInput != 'q'):
        sum = sum + int(userInput)
        print(f" total price:{sum}")
    else:
        print(f"your Total Amount is{sum}.Thanks You Much")
        break
