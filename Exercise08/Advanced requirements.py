# A pre-made list of names to look up
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Inquire about the name the user wishes to look up, eliminating any additional spaces.
search_term = input("Kindly type the name you're trying to find: ").strip()

# Use a case-insensitive search to see if the entered name is present in the list.
if search_term.lower() in [name.lower() for name in names]:
    # Send a kind success message if the name is located.
    print(f"Great news. '{search_term}' is in the list.")
else:
    # Inform the user politely if the name cannot be located.
    print(f"Sorry, '{search_term}' isn't in the list.")