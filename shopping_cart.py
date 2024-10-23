item = input("Enter Items in the cart: ")
price = float(input("Enter the price for the item: $"))
quantity = int(input("How many items you want: $"))

total = price * quantity

print(f"You have to pay ${total} in total for {item}")
