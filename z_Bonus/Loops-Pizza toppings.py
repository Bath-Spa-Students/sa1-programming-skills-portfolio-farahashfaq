#Create a loop that asks the user to input a number of pizza toppings until they input a value that indicates "quit." as they go into every topping.
#Print a note stating that you'll top their pizza with that item.

# Get the pizza toppings loop going.
print("And now for the pizza topping. Enter 'finish' to end the session.")

while True:
  topping = input("Enter toppings:").strip().lower()

  if topping == 'quit':
    print("We appreciate your purchase! Having your topping ready.")
    break
  else:
      print(f"will be adding {topping} to the pizza.")