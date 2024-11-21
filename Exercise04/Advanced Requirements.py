# For the quiz, a dictionary listing nations and their capitals
# The values are the capitals of the countries, and the keys are their names.
quiz_data = {
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Greece": "Athens",
    "Switzerland": "Bern",
    "Austria": "Vienna",
    "Spain": "Madrid",
    "France": "Paris",
    "Italy": "Rome",
    "Germany": "Berlin"
}

# Variable to monitor the user's rating
score = 0

# Go over each pair of capitals and countries in the test.
for country, capital in quiz_data.items():
    # Request the user's current country's capital.
    user_answer = input(f"What's the capital of {country}? ").strip() #.strip() eliminates unnecessary spaces surrounding input

    # Verify the response, disregarding case differences.
    if user_answer.lower() == capital.lower():
        # If accurate, note it and raise the score.
        print("Good. That's correct.")
        score += 1
    else:
        # If wrong, politely give the right response.
        print(f"Close, but the capital of {country} is actually {capital}.")

# Encourage the user by displaying their ultimate score.
print(f"\nGreat job. You scored {score} out of {len(quiz_data)}.")