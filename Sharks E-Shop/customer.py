class Customer:
    def __init__(self):
        # Initialize an empty cart for the customer
        self.cart = []

    def add_to_cart(self, product, quantity):
        # Add a product to the cart if the quantity is available
        if quantity <= product.quantity_available:
            # Append a tuple of (product, quantity) to the cart
            self.cart.append((product, quantity))
            # Reduce the quantity available in the product
            product.quantity_available -= quantity
            print("\n============ Product added to cart successfully.============")
        else:
            print("\n============Insufficient quantity available. Product not added to cart.============")

    def remove_from_cart(self, product_id):
        # Remove a product from the cart based on its product_id
        for index, item in enumerate(self.cart):
            if item[0].product_id == product_id:
                current_quantity = item[1]
                print(f"Current quantity in cart: {current_quantity}")
                quantity_to_remove = int(input("Enter the quantity to remove: "))

                if quantity_to_remove > current_quantity:
                    print("Cannot remove more than what's in the cart.")
                elif quantity_to_remove == current_quantity:
                    # Remove the item completely from the cart
                    self.cart.pop(index)
                    print("\n============Product removed from cart successfully.============")
                else:
                    # Update the quantity of the item in the cart
                    self.cart[index] = (item[0], current_quantity - quantity_to_remove)
                    print(f"\n============{quantity_to_remove} units of product removed from cart successfully.============")
                break
        else:
            print("\n============Product not found in cart.============")

    def generate_cart_summary(self):
        # Generate and display a summary of items in the cart
        total_price = 0
        print("==============================================================\n \t\t\t === Cart Summary === \n")
        for item in self.cart:
            product, quantity = item
            total_price += product.price * quantity
            print(f"Product: {product.name}\t Quantity: {quantity}\t Price: {product.price * quantity}")
        print(f"Total Price: {total_price}")
        print("==============================================================")
