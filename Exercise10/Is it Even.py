# A function for deciding if a given number is odd or even.
def check_even_odd(number):
    # A number is viewed as even if it is also divisible by 2.
    if number % 2 == 0:
        return f"{number} is even."
    else:
        # It's odd if not.
        return f"{number} is odd."

# Main task to process user input and show the result.
def main():
    # Request that the user input a number.
    try:
        user_number = int(input("Please enter a number: "))
        # Get the result message by calling the check_even_odd function.
        result_message = check_even_odd(user_number)
        # Output the outcome message.
        print(result_message)
    except ValueError:
        # Show an error message if the user inputs a value that isn't an integer.
        print("The input is invalid. Please input a number.")

# Only execute the main function when running this script directly.
if __name__ == "__main__":
    main()