# Establish the system's correct password.
correct_password = "123456"

# Decide how many password attempts are permitted.
Max_attempts = 5

# Set up a counter to record the quantity of attempts made.
attempts = 0

# Begin a loop that keeps going until the right password is typed in or all tries have been made.
while attempts < Max_attempts:
    # Request that the user input their password.
    user_password = input("enter the password: ").strip()
    
    # After every entry, increase the number of attempts by one.
    attempts += 1

    # Verify that the password you typed and the one you have stored are the same.
    if user_password == correct_password:
        # If it's right, allow access and close the loop.
        print("Access granted. Greetings User.")
        break
    else:
        # Determine the number of attempts left to notify the user.
        Remaining_attempts = Max_attempts - attempts
        # Show the user's previous attempts and inform them that the password is wrong.
        print(f"Access denied. You have {Remaining_attempts} attempt(s) remaining.")
        
        # Issue a last warning if the user has made all of the permitted attempts.
        if attempts == Max_attempts:
            print("No access. Because of too many unsuccessful attempts, you have been locked out.")