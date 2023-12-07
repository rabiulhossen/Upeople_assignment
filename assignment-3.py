def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)

# Get a number from the user

number = int(input("Enter a number: "))

if number > 0:
        countdown(int(number))  # Call countdown for positive numbers
elif number < 0:
        countup(int(number))  # Call countup for negative numbers
else:
        print("Blastoff!")  # Call Blastoff for zero


