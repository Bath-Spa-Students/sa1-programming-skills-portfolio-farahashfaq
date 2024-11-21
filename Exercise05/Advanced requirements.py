#A dictionary that associates the number of days in a non-leap year with each month number (1–12).
days_in_month = {
    1: 31,   # January, 31 days
    2: 28,   # February, 28 days (in a non-leap year)
    3: 31,   # March, 31 days
    4: 30,   # April, 30 days
    5: 31,   # May, 31 days
    6: 30,   # June, 30 days
    7: 31,   # July, 31 days
    8: 31,   # August, 31 days
    9: 30,   # September, 30 days
    10: 31,  # October, 31 days
    11: 30,  # November, 30 days
    12: 31   # December, 31 days
}

#Request a month number from 1 to 12 from the user.
try:
    month_number = int(input("Enter the month number (1-12): ").strip())  #Empty the excess spaces surrounding the input

    #Verify that the month number you entered falls between 1 and 12.
    if 1 <= month_number <= 12:
        
        #A special example where we must verify for a leap year is February (second month).
        if month_number == 2:
            #Inquire with the user if it's a leap year.
            is_leap = input("Is it a leap year? (yes/no): ").strip().lower()
            #February will have 28 days if it is not a leap year, and 29 days otherwise.
            days = 29 if is_leap == "yes" else 28
        else:
            #For every other month, simply check the dictionary for the amount of days.
            days = days_in_month[month_number]
        
        #Display how many days there are in the chosen month.
        print(f"The number of days in month {month_number} is {days}.")
    else:
        #If the month number is not between 1 and 12, let the user know.
        print("incorret, That's not a valid month number. Please enter a number between 1 and 12.")

except ValueError:
    #Deal with situations in which the user enters text or something other than a number.
    print("I apologize, but that input is invalid. Kindly input a number from 1 to 12.")