def hypotenuse(
    leg1, leg2
):  # function has 2 arguments for the first leg and second leg respectively
    return (leg1**2 + leg2**2) ** (
        1 / 2
    )  # According to Pythagorean theorem, the hypotenuse is equal to the square root of the sum of the squares of the two legs or Hypotenuse = √(Perpendicular^2 + Base^2)


print(
    "Test number 1: triangle with legs 3 and 4, hypotenuse is:", hypotenuse(3, 4)
)  # prints the call for triangle with legs 3 and 4
Output: 5  # expected result


print(
    "Test number 2: triangle with legs 12 and 5, hypotenuse is:", hypotenuse(12, 5)
)  # same for 12 and 5
Output: 13  # expected result
print(
    "Test number 3: triangle with legs 50 and 51, hypotenuse is:", hypotenuse(50, 51)
)  # 50 and 51 are arguments
Output: 71.42128534267638  # expected result


def custom_calculator(a, b, operation):
    """
    Performs basic arithmetic operations on two numbers.
    Parameters:
    - a (float): The first number.
    - b (float): The second number.
    - operation (str): The operation to perform (e.g., '+', '-', '*', '/').
    Returns:
    float: The result of the arithmetic operation.
    """
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:  # condition check for denominator not equal zero
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")  # when denominator equal 0


# Test
addition_result = custom_calculator(5, 3, "*")
print(addition_result)  # Output: 15

division_result = custom_calculator(55, 11, "/")
print(division_result)  # Output: 5

# Test complex number:  # Complex numbers are the numbers that are expressed in the form of a+ib where, a,b are real numbers and  ‘i’ is an imaginary number called “iota”. The value of i = (√-1). For example, 2+3i is a complex number, where 2 is a real number (Re) and 3i is an imaginary number (Im).
complex_result = custom_calculator(5 + 3j, 3 - 4j, "+")
print(complex_result)  # Output: (8-1j)
