#make a list of strings which contains names
Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#In the above string list, write the string you wish to search for.
Search_name = "Ian"

#Search for the name in the list given above.
if Search_name in Names :
    print("{Search_name} is on the list!")
else:
    print("{Search_name}is not on the list sadly.")