while True:
    try:
        print("Please two numbers 'a' and 'b' to calculate their sum.")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        break
    except ValueError:
        print("Please enter a number in both fields.")

c = a + b
print(f"{a} + {b} = {c}")