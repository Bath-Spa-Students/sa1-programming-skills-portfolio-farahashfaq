#Establish the system's correct password.
Correct_password = "12345"

#Decide how many password attempts are permitted.
Max_attempts = 5

#Set up a counter to record the quantity of attempts made.
Attempts = 0

#Begin a loop that keeps going until the right password is typed in or all tries have been made.
while Attempts < Max_attempts:
    #Request that the user input their password.
    User_password = input("Enter the password: ").strip()
    
    #For privacy, hide the entered password with asterisks.
    masked_password = '*' * len(User_password)
    
    #After every entry, increase the number of attempts by one.
    Attempts += 1

    #Verify that the password you typed and the one you have stored are the same.
    if User_password == Correct_password:
        #If it's right, allow access and close the loop.
        print("Access is granted. Greetings, User.")
        break
    else:
        #If it's wrong, show the masked password and an error message.
        print(f"Access denied: {masked_password}")
        
        #If this is the user's second-to-last try, give them a clue.
        if Attempts == Max_attempts - 1:
            print("Hint: The password is number.")
        
        #Lock the user out and let them know if they've tried everything.
        if Attempts == Max_attempts:
            print("No access. Because of too many unsuccessful attempts, you have been locked out.")
