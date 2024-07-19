from product import Product

class Seller:
    def __init__(self):
        # Initialize the Seller with an empty inventory
        self.inventory = []

    def add_product(self, product):
        # Add a product to the inventory if it does not already exist
        for existing_product in self.inventory:
            if existing_product.product_id == product.product_id:
                print("============Product with the same ID already exists.============")
                return

        # Append the new product to the inventory
        self.inventory.append(product)
        print("\n============Product added successfully.============")

    def remove_product(self, product_id):
        # Remove a product from the inventory based on its product_id
        for product in self.inventory:
            if product.product_id == product_id:
                self.inventory.remove(product)
                print("\n============Product removed successfully.============")
                break
        else:
            print("\n============Product not found.============")

    def update_product(self, product_id, new_name, new_price, new_quantity):
        # Update the details of a product in the inventory
        product_found = False
        for product in self.inventory:
            if product.product_id == product_id:
                product_found = True
                product.name = new_name
                product.price = new_price
                product.quantity_available = new_quantity
                print("\n============Product updated successfully.============")
                break

        if not product_found:
            print("\n===========Product not found.============")

    def view_inventory(self):
        # Display the list of products in the inventory
        print("==============================================================\n \t\t\t === Products === \n")
        for product in self.inventory:
            print(f"ID: {product.product_id}\t Name: {product.name}\t Price: {product.price}\t Quantity: {product.quantity_available}")
        print("==============================================================")
