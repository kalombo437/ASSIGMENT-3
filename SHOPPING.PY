class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name  # Instance variable
        self.price = price  # Instance variable
        self.quantity_in_stock = quantity_in_stock  # Instance variable

    # Method to display product details
    def display_product_info(self):
        print(f"Product: {self.product_name}")
        print(f"Price: ${self.price}")
        print(f"Quantity in stock: {self.quantity_in_stock}\n")


class ShoppingCart:
    total_carts = 0  # Class variable to track the total number of carts

    def __init__(self):
        self.items = []  # Instance variable, list of tuples (product, quantity)
        ShoppingCart.total_carts += 1  # Increment total carts on creation

    # Method to add a product to the cart
    def add_to_cart(self, product, quantity):
        if quantity <= product.quantity_in_stock:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"Added {quantity} of {product.product_name} to the cart.")
        else:
            print(f"Insufficient stock for {product.product_name}. Only {product.quantity_in_stock} available.")

    # Method to remove a product from the cart
    def remove_from_cart(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]  # Restock the removed quantity
                print(f"Removed {item[1]} of {product.product_name} from the cart.")
                break
        else:
            print(f"{product.product_name} is not in the cart.")

    # Method to display the contents of the cart
    def display_cart(self):
        if not self.items:
            print("The cart is empty.\n")
        else:
            print("Cart Contents:")
            for item in self.items:
                product, quantity = item
                print(f"{quantity} x {product.product_name} - ${product.price} each")
            print()  # Newline for formatting

    # Method to calculate the total price of the cart
    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        return total


# Task 1: Create at least three Product objects with varying prices and quantities
product1 = Product("Laptop", 1000, 5)
product2 = Product("Headphones", 100, 10)
product3 = Product("Mouse", 25, 20)

# Task 2: Create two separate ShoppingCart instances and perform a series of operations
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Adding products to cart1
cart1.add_to_cart(product1, 1)  # Add 1 Laptop
cart1.add_to_cart(product2, 2)  # Add 2 Headphones
cart1.add_to_cart(product3, 3)  # Add 3 Mouse

# Adding products to cart2
cart2.add_to_cart(product1, 2)  # Add 2 Laptops
cart2.add_to_cart(product3, 1)  # Add 1 Mouse

# Removing a product from cart1
cart1.remove_from_cart(product2)  # Remove 2 Headphones from cart1

# Task 3: Display the contents of each cart and calculate the total amount due
print("\nCart 1:")
cart1.display_cart()
print(f"Total for Cart 1: ${cart1.calculate_total()}\n")

print("Cart 2:")
cart2.display_cart()
print(f"Total for Cart 2: ${cart2.calculate_total()}\n")

# Display remaining stock for each product
print("Remaining Stock:")
product1.display_product_info()
product2.display_product_info()
product3.display_product_info()

