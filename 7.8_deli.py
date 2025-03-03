sandwiches = ['salad', 'grilled cheese', 'tuna', 'turkey']
finished_sandwiches = []

while sandwiches:
    current_sandwich = sandwiches.pop(0)

    print(f"I made your {current_sandwich} sandwich.".format(current_sandwich.title()))
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(" {} sandwich".format(finished_sandwich.title()))