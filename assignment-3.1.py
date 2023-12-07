def divide_numbers():
    try:
        # Get user input for two numbers
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        # Attempt division
        result = numerator / denominator

        # Display the result
        print(f"The result of {numerator} / {denominator} is: {result}")

    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Division by zero is not allowed.")

    except ValueError:
        # Handle invalid input error (e.g., non-numeric input)
        print("Error: Please enter valid numeric values.")

    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Call the function to deliberately introduce a division by zero error
divide_numbers()
