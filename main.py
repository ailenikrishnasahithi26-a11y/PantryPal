# PantryPal - Simple Python Inventory Tracker
# Uses Dictionaries to store items (No JSON used)

# Main dictionary to store inventory
# Key = item name, Value = dictionary of details (quantity, price)
inventory = {}

# File handling: Load data from text file
def load_data():
    try:
        file = open("inventory.txt", "r")
        for line in file:
            line = line.strip()
            if line != "":
                # list created using split()
                parts = line.split(",")
                name = parts[0]
                quantity = int(parts[1])
                price = float(parts[2])
                
                # store in dictionary
                inventory[name] = {
                    "quantity": quantity,
                    "price": price
                }
        file.close()
        print("Data loaded successfully from inventory.txt")
    except FileNotFoundError:
        print("No file found. Starting with empty inventory dictionary.")
    except Exception as e:
        print("Error loading file:", e)

# File handling: Save data to text file
def save_data():
    try:
        file = open("inventory.txt", "w")
        for name in inventory:
            details = inventory[name]
            line = name + "," + str(details["quantity"]) + "," + str(details["price"]) + "\n"
            file.write(line)
        file.close()
        print("Data saved to inventory.txt successfully!")
    except Exception as e:
        print("Error saving file:", e)

# 1. Add item to dictionary (Create)
def add_item():
    print("\n--- Add Item ---")
    name = input("Enter item name: ").strip()

    if name == "":
        print("Item name cannot be empty!")
        return

    # Check if item exists in dictionary
    if name in inventory:
        print("Item already exists! Use update option to change quantity.")
        return

    # Exception handling for numbers
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
    except ValueError:
        print("Invalid input! Quantity and price must be numbers.")
        return

    # Store details in dictionary
    inventory[name] = {
        "quantity": quantity,
        "price": price
    }

    save_data()
    print("Item '" + name + "' added successfully!")

# 2. View all items from dictionary (Read)
def view_items():
    print("\n--- Current Inventory ---")
    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    # Loop through dictionary keys
    for name in inventory:
        item = inventory[name]
        qty = item["quantity"]
        price = item["price"]

        # Conditional statement to check low stock
        if qty <= 2:
            status = "Low Stock!"
        else:
            status = "In Stock"

        print("Item: " + name + " | Quantity: " + str(qty) + " | Price: Rs. " + str(price) + " | Status: " + status)

# 3. Update quantity in dictionary (Update)
def update_quantity():
    print("\n--- Update Quantity ---")
    name = input("Enter item name to update: ").strip()

    # Check if key exists in dictionary
    if name in inventory:
        try:
            new_qty = int(input("Enter new quantity: "))
            if new_qty >= 0:
                inventory[name]["quantity"] = new_qty
                save_data()
                print("Quantity updated successfully!")
            else:
                print("Quantity cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Item not found in inventory!")

# 4. Delete item from dictionary (Delete)
def delete_item():
    print("\n--- Delete Item ---")
    name = input("Enter item name to delete: ").strip()

    # Check if key is in dictionary
    if name in inventory:
        del inventory[name]
        save_data()
        print("Item '" + name + "' deleted successfully!")
    else:
        print("Item not found in inventory!")

# 5. Search for an item in dictionary
def search_item():
    print("\n--- Search Item ---")
    search_name = input("Enter name to search: ").strip().lower()

    found = False
    for name in inventory:
        if search_name in name.lower():
            item = inventory[name]
            print("Found: " + name + " | Quantity: " + str(item["quantity"]) + " | Price: Rs. " + str(item["price"]))
            found = True

    if not found:
        print("No matching item found.")

# 6. Show items needing restocking
def show_low_stock():
    print("\n--- Low Stock Items (Restock Alert) ---")
    count = 0
    for name in inventory:
        qty = inventory[name]["quantity"]
        # Condition check
        if qty <= 2:
            print("* " + name + " - Only " + str(qty) + " left!")
            count = count + 1

    if count == 0:
        print("All items have sufficient stock.")

# 7. Calculate total stock value
def show_total_value():
    print("\n--- Total Stock Value ---")
    total = 0.0
    for name in inventory:
        item = inventory[name]
        total = total + (item["quantity"] * item["price"])

    print("Total Items Count:", len(inventory))
    print("Total Stock Value: Rs.", total)

# Main menu loop
def main():
    load_data()

    while True:
        print("\n=== PANTRYPAL INVENTORY MENU ===")
        print("1. View All Items")
        print("2. Add Item")
        print("3. Update Quantity")
        print("4. Delete Item")
        print("5. Search Item")
        print("6. Show Low Stock Items")
        print("7. Calculate Total Stock Value")
        print("8. Exit")

        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            view_items()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_quantity()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            search_item()
        elif choice == "6":
            show_low_stock()
        elif choice == "7":
            show_total_value()
        elif choice == "8":
            print("Exiting PantryPal. Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1 to 8.")

if __name__ == "__main__":
    main()
