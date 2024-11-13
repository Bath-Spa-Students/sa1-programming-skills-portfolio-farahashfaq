# A dictionary to keep track of each month's days
# Month numbers are represented by keys (1 for January, 2 for February, etc.), while the days of each month are represented by values.
Days_in_month = {
    1: 31,   #January
    2: 28,   #February (assuming a non-leap year)
    3: 31,   #March
    4: 30,   #April
    5: 31,   #May
    6: 30,   #June
    7: 31,   #July
    8: 31,   #August
    9: 30,   #September
    10: 31,  #October
    11: 30,  #November
    12: 31   #December
}

#Gently prompt the user to enter the month number.
try:
    Month_number = int(input("Enter a month number (1-12): ").strip())#.strip() eliminates unnecessary spaces surrounding input

   #Verify that the month number falls within the acceptable range.
    if Month_number in Days_in_month:
        #Show the number of days in the month that was entered.
        print(f"Number of days in month {Month_number} is {Days_in_month[Month_number]}.")
    else:
        #Let the user know if the input is not between 1 and 12.
        print("Sorry, That's not a valid month number. Please enter a number between 1 and 12")

except ValueError:
    #Use a kind message to handle non-integer input.
    print("Invalid number. Enter a numerical value between 1 and 12")