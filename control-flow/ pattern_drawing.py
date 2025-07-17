# pattern_drawing.py

# Prompt the user for input
prompt = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for each row
while row < prompt:
    # Inner for loop to print each asterisk in the row
    for col in range(prompt):
        print("*", end="")  # Print star without newline
    print()  # Print newline after each row
    row += 1
