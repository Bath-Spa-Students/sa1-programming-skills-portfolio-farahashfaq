# Ask the user to type their entire name, eliminating any spaces.
user_name = input("Enter your full name: ").strip() #.strip() eliminates unnecessary spaces surrounding input

# Request the user's hometown and eliminate any unnecessary whitespace.
user_hometown = input("Enter your hometown: ").strip() #.strip() eliminates unnecessary spaces surrounding input

# To verify correct entry, repeatedly ask the user for their age.
while True:
    try:
        # Make an integer out of the input.
        user_age = int(input("Enter your age: "))
        break  # If the conversion is successful, end the loop.
    except ValueError:
        # If the input is not a valid integer, display an error.
        print("Invalid input. Please enter a numerical value for age.")

# Present the gathered data.
print("\nUser Information:")
print(f"Name: {user_name}")
print(f"Hometown: {user_hometown}")
print(f"Age: {user_age}")