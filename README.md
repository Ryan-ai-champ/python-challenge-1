# python-challenge-1
python-challenge-1 for ai bootcamp
menu_items = {
    1: {"name": "Apple", "price": 0.49},
    2: {"name": "Tea - Thai iced", "price": 3.99},
    3: {"name": "Fried banana", "price": 4.49},
    4: {"name": "Burger", "price": 5.99}
}

order_list = []
place_order = True

# Function to print menu
def print_menu():
    print("Menu:")
    for key, value in menu_items.items():
        print(f"{key}. {value['name']} - ${value['price']}")

while place_order:
    print_menu()
    menu_selection = input("Please enter the menu item number you would like to order: ")

    # Validate if input is a number
    if not menu_selection.isdigit():
        print("Invalid input. Please enter a number corresponding to the menu item.")
        continue

    menu_selection = int(menu_selection)

    # Validate if selection is in the menu
    if menu_selection not in menu_items.keys():
        print("Invalid selection. Please select an item from the menu.")
        continue

    item_name = menu_items[menu_selection]["name"]
    price = menu_items[menu_selection]["price"]

    quantity = input(f"How many of {item_name} would you like? (Default is 1 if invalid): ")

    # Validate quantity
    if not quantity.isdigit():
        quantity = 1
    else:
        quantity = int(quantity)

    # Add order to the list
    order_list.append({"Item name": item_name, "Price": price, "Quantity": quantity})

    # Ask if they want to continue ordering
    while True:
        continue_ordering = input("Would you like to order anything else? (y/n): ").lower()
        match continue_ordering:
            case 'y':
                break
            case 'n':
                place_order = False
                print("Thank you for your order!")
                break
            case _:
                print("Invalid input. Please type 'y' for yes or 'n' for no.")

# Print receipt
print("\nReceipt:")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

for order in order_list:
    item_name = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]

    # Formatting spaces
    item_space = ' ' * (26 - len(item_name))
    price_space = ' ' * (8 - len(f"${price:.2f}"))

    # Print formatted line
    print(f"{item_name}{item_space}| ${price:.2f}{price_space}| {quantity}")

# Calculate total price
total_price = sum([order["Price"] * order["Quantity"] for order in order_list])
print("\nTotal Price: $" + f"{total_price:.2f}")
