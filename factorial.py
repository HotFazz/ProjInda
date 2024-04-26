def get_integer_input(prompt):
    """Utility function to get a valid integer input from the user."""
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a non-negative integer.")

def factorial(n):
    """Recursively calculates the factorial of a non-negative integer."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    print("Welcome to the Factorial Calculator!")
    number = get_integer_input("Enter a non-negative integer to compute the factorial: ")
    result = factorial(number)
    print(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()


# Hej jag heter fleix

