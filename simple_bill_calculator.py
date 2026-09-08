
# Ask the user for the price and quantity of the item
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

# Calculate the total bill
total = price * quantity

# Print a friendly summary using an f-string formatted to 2 decimal places
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
