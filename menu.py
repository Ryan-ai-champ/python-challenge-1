# Menu dictionary remains unchanged
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99,
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99,
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49,
        },
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99,
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49,
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49,
        },
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49,
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49,
    },
}

# 1. Set up the order list
order_list = []

# Launch the store
print("Welcome to the variety food truck!")

place_order = True
while place_order:
    print("\nFrom which menu would you like to order?")
    i = 1
    menu_items = {}

    # Display main menu categories
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    menu_category = input("Type menu number: ")

    if menu_category.isdigit() and int(menu_category) in menu_items.keys():
        menu_category_name = menu_items[int(menu_category)]
        print(f"\nYou selected {menu_category_name}.")
        print(f"\nWhat {menu_category_name} item would you like to order?")

        i = 1
        menu_items = {}
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")
        for key, value in menu[menu_category_name].items():
            if isinstance(value, dict):
                for key2, value2 in value.items():
                    item_name = f"{key} - {key2}"
                    menu_items[i] = {"Item name": item_name, "Price": value2}
                    print(f"{i}      | {item_name:24} | ${value2:.2f}")
                    i += 1
            else:
                menu_items[i] = {"Item name": key, "Price": value}
                print(f"{i}      | {key:24} | ${value:.2f}")
                i += 1

        menu_item_number = input("\nType the item number you want to order: ")
        if menu_item_number.isdigit() and int(menu_item_number) in menu_items.keys():
            selected_item = menu_items[int(menu_item_number)]
            quantity = input(
                f"How many of {selected_item['Item name']} would you like? (Default is 1): "
            )
            if not quantity.isdigit():
                quantity = 1
            else:
                quantity = int(quantity)

            order_list.append(
                {
                    "Item name": selected_item["Item name"],
                    "Price": selected_item["Price"],
                    "Quantity": quantity,
                }
            )
            print(
                f"Added {quantity} x {selected_item['Item name']} to your order."
            )
        else:
            print("Invalid item number.")

    else:
        print("Invalid menu option.")

    while True:
        keep_ordering = input("Would you like to keep ordering? (Y/N): ").strip().lower()
        if keep_ordering == "y":
            break
        elif keep_ordering == "n":
            place_order = False
            break
        else:
            print("Please enter Y or N.")

# Print the final order
print("\nThis is what we are preparing for you:\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
total_cost = 0
for order in order_list:
    item_name = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]
    total_cost += price * quantity
    print(f"{item_name:24} | ${price:6.2f} | {quantity}")

print("--------------------------|--------|----------")
print(f"Total cost:               | ${total_cost:.2f}")
print("Thank you for your order!")

