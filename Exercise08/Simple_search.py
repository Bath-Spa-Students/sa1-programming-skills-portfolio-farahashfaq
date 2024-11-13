##make a list of strings which contains names
Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#In the above string list, write the string you wish to search for.
Search_name = input("Enter name:").strip()

# Flag to monitor if the name appears in the search
found = False

# Check if the user's input matches each name in the list by looping over them.
for name in Names:
    # To make sure the search is case-insensitive, convert both names to lowercase.

    if name.lower() == Search_name.lower():
        # Set 'found' to True and notify the user if a match is discovered.
        found = True
        print(f"perfect'{Search_name}' is present in the list.")

        break  # Since we discovered the name, end the loop early.
# Inform the user if the loop ends and the name was not found.

if not found:
    print(f"sadly, '{Search_name}' is not in the list.")
