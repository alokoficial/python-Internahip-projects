inventory = {}

while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. View All Products")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Product
    if choice == '1':
        product = input("Enter product name: ").strip().lower()

        try:
            quantity = int(input("Enter quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative!")
            else:
                inventory[product] = quantity
                print("Product added successfully!")

        except ValueError:
            print("Please enter a valid number!")

    # Update Product
    elif choice == '2':
        product = input("Enter product name: ").strip().lower()

        if product in inventory:
            try:
                quantity = int(input("Enter new quantity: "))

                if quantity < 0:
                    print("Quantity cannot be negative!")
                else:
                    inventory[product] = quantity
                    print("Product updated successfully!")

            except ValueError:
                print("Please enter a valid number!")

        else:
            print("Product not found!")

    # Delete Product
    elif choice == '3':
        product = input("Enter product name: ").strip().lower()

        if product in inventory:
            del inventory[product]
            print("Product deleted successfully!")
        else:
            print("Product not found!")

    # Search Product
    elif choice == '4':
        product = input("Enter product name: ").strip().lower()

        if product in inventory:
            print(f"{product.capitalize()} Quantity: {inventory[product]}")
        else:
            print("Product not found!")

    # View All Products
    elif choice == '5':
        if inventory:
            print("\n===== All Products =====")

            for product, quantity in inventory.items():
                print(f"{product.capitalize()} -> {quantity}")

        else:
            print("Inventory is empty!")

    # Exit
    elif choice == '6':
        print("Exiting program...")
        break

    # Invalid Choice
    else:
        print("Invalid choice! Please select between 1 and 6.")
        