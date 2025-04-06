filename = 'guest_book.txt'

while True:
    print("Please input a name, or enter 'close' to quit:")
    name = input()
    
    if name.lower() == 'close':
        print("Exiting the guest book.")
        break
    else:
        with open(filename, 'a') as message:
            message.write(f"{name}\n")
        print(f"Thank you, {name}! Your visit has been recorded.")