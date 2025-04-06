import random

# Create a list of 10 numbers and 5 letters
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
letters = ['a', 'b', 'c', 'd', 'e']

# Random selection for four numbers and one letter
random_numbers = random.sample(numbers, 4)
random_letter = random.choice(letters)
random_selection = random_numbers + [random_letter]

# Print the winning selection
print("Winning lottery rolls: {}".format(random_selection))

# Getting user input for a lottery number
user_input = input("Enter your lottery number (4 numbers followed by 1 letter, e.g., 1235a): ")

# Check if input is valid: 4 digits + 1 letter
#(I wasn't really sure how to do this part, I had to ask a friend to help with it.)
if len(user_input) == 5 and user_input[:-1].isdigit() and user_input[-1].isalpha():
    user_numbers = [int(digit) for digit in user_input[:-1]]
    user_letter = user_input[-1]

    # Compare the user input with the winning selection
    if sorted(user_numbers) == sorted(random_numbers) and user_letter == random_letter:
        print("Congratulations, you are a winner!")
    else:
        print("Sorry, you did not win. Better luck next time!")
else:
    print("Invalid input! Please enter 4 numbers followed by 1 letter.")