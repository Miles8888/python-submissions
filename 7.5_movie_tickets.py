print("Type 'quit' to end the program or enter your age to get a ticket price.")
while True:
    number = input("Enter your age: ")
    if number.lower() == 'quit':
        break
    number = int(number)
    if number < 3:
        print("Tickets for infants are free!")
    elif number < 13:
        print("Kids' tickets are given a discount and only cost $10.")
    else:
        print("Your ticket will be $15.")