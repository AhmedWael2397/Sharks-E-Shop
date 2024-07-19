from seller import Seller
from customer import Customer
from product import Product

# Welcome message for the user
print("\n===== Welcome to the SHARKS E-Shop ======")

# Initialize Seller and Customer objects
seller = Seller()
customer = Customer()

while True:
    # Main menu for choosing between Seller, Customer, or Exit
    print("")
    choice = input("Enter your choice from: \n1. Seller\n2. Customer\n3. to Exit \n===> ")

    if choice == "1":
        # Seller Menu
        while True:
            print("\n1. View Product List\n2. Add Product\n3. Update Product\n4. Remove Product\n5. Exit to Main Menu")
            seller_choice = input("\n===> ")

            if seller_choice == "1":
                # View the list of products in the inventory
                seller.view_inventory()
                
            elif seller_choice == "2":
                # Add a new product to the inventory
                product_id = input("Enter product ID: ")
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity available: "))
                new_product = Product(product_id, name, price, quantity)
                seller.add_product(new_product)

            elif seller_choice == "3":
                # Update an existing product's details
                product_id = input("Enter product ID to update: ")
                new_name = input("Enter new name: ")
                new_price = float(input("Enter new price: "))
                new_quantity = int(input("Enter new quantity: "))
                seller.update_product(product_id, new_name, new_price, new_quantity)

            elif seller_choice == "4":
                # Remove a product from the inventory
                product_id = input("Enter product ID to remove: ")
                seller.remove_product(product_id)

            elif seller_choice == "5":
                # Exit to the main menu
                break

            else:
                # Invalid choice handling for Seller menu
                print("Invalid choice")

    elif choice == "2":
        # Customer Menu
        while True:
            print("\n1. View Products in Inventory\n2. Add to Cart\n3. Remove from Cart\n4. Check Cart Summary\n5. Exit to Main Menu")
            customer_choice = input("\n===> ")

            if customer_choice == "1":
                # Display products available in the inventory
                seller.view_inventory()

            elif customer_choice == "2":
                # Add a product to the cart
                product_id = input("Enter product ID to add: ")
                quantity = int(input("Enter quantity: "))
                # Find the product from the inventory
                product = None
                for prod in seller.inventory:
                    if prod.product_id == product_id:
                        product = prod
                        break
                if product:
                    customer.add_to_cart(product, quantity)
                else:
                    print("============ Product not found.============")

            elif customer_choice == "3":
                # Remove a product from the cart
                product_id = input("Enter product ID to remove from cart: ")
                customer.remove_from_cart(product_id)

            elif customer_choice == "4":
                # Check the cart summary and optionally finalize the purchase
                if not customer.cart:
                    print("============ Your cart is empty.============")
                else:
                    customer.generate_cart_summary()
                    finalize_purchase = input("Do you want to finalize the purchase? (yes/no): ")
                    if finalize_purchase.lower() == "yes":
                        # Customer details input
                        full_name = input("Enter your full name: ")
                        address = input("Enter your address: ")
                        payment_type = input("Enter payment type (Visa/Cash): ")

                        if payment_type.lower() == "visa":
                            card_number = input("Enter your 16-digit Visa card number: ")
                            if len(card_number) != 16 or not card_number.isdigit():
                                print("Invalid Visa card number. Please enter a valid 16-digit number.")
                                continue  # Restart the loop to enter payment type again

                        # Display order summary
                        print("\nOrder Summary:")
                        print(f"Customer: {full_name}")
                        print(f"Address: {address}")
                        print(f"Payment Type: {payment_type}")
                        if payment_type.lower() == "visa":
                            print(f"Visa Card Number: {card_number}")
                        print("Cart Summary:-")
                        customer.generate_cart_summary()

                        # Validation and option to edit details
                        confirm_purchase = input("Proceed with the purchase? (yes/no): ")
                        if confirm_purchase.lower() == "yes":
                            print("Purchase complete.")
                            # Clear the cart after successful purchase
                            customer.cart = []
                        else:
                            print("Purchase canceled. Please review your details and items in the cart.")
                    else:
                        print("Purchase not finalized.")

            elif customer_choice == "5":
                # Exit to the main menu
                break

            else:
                # Invalid choice handling for Customer menu
                print("============Invalid choice============")

    elif choice == "3":
        # Exit the application
        print("Bye bye! Thank you for using our shopping app \U0001F496")
        break

    else:
        # Invalid choice handling for main menu
        print("============Invalid choice============")
