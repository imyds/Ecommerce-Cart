import sqlite3

# Initialize the database and create tables
class EcommerceSystem:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE products
                              (id INTEGER PRIMARY KEY, name TEXT, price REAL, quantity INTEGER)''')
        self.cursor.execute('''CREATE TABLE cart
                              (user_id INTEGER, product_id INTEGER, quantity INTEGER)''')
        self.conn.commit()
        self.add_sample_products()

    def add_sample_products(self):
        products = [
            ("Laptop", 999.99, 10),
            ("Mouse", 29.99, 50),
            ("Keyboard", 59.99, 30)
        ]
        self.cursor.executemany("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", products)
        self.conn.commit()

    def display_available_products(self):
        products = self.cursor.execute("SELECT id, name, price FROM products").fetchall()
        print("Available products:")
        for id, name, price in products:
            print(f"{id}. {name} - ₹{price:.2f}")

    def add_to_cart(self, user_id, product_id, quantity):
        product = self.cursor.execute("SELECT name, price, quantity FROM products WHERE id = ?", (product_id,)).fetchone()
        if not product:
            return "Product not found."
        name, price, stock_quantity = product
        if stock_quantity < quantity:
            return f"Insufficient stock. Only {stock_quantity} available."
        self.cursor.execute("INSERT INTO cart (user_id, product_id, quantity) VALUES (?, ?, ?)", (user_id, product_id, quantity))
        self.cursor.execute("UPDATE products SET quantity = quantity - ? WHERE id = ?", (quantity, product_id))
        self.conn.commit()
        return f"Added {quantity} {name} to cart."

    def view_cart(self, user_id):
        items = self.cursor.execute("""
            SELECT p.name, c.quantity, p.price
            FROM cart c
            JOIN products p ON c.product_id = p.id
            WHERE c.user_id = ?
        """, (user_id,)).fetchall()
        if not items:
            return "Cart is empty."
        total = sum(quantity * price for _, quantity, price in items)
        cart_contents = "Cart contents:\n"
        for name, quantity, price in items:
            cart_contents += f"{name}: {quantity} x ₹{price:.2f} = ₹{quantity * price:.2f}\n"
        cart_contents += f"Total: ₹{total:.2f}"
        return cart_contents

    def checkout(self, user_id):
        contents = self.view_cart(user_id)
        if "Cart is empty." in contents:
            return "Cannot checkout. Cart is empty."
        self.cursor.execute("DELETE FROM cart WHERE user_id = ?", (user_id,))
        self.conn.commit()
        return f"Checkout successful!\n\n{contents}\n\nHappy Shopping!"

    def simulate_user_interaction(self):
        user_id = 1
        print("Welcome to our e-commerce system!")
        while True:
            self.display_available_products()
            choice = input("Enter the product ID you want to purchase (0 to checkout): ")
            try:
                product_id = int(choice)
                if product_id == 0:
                    break
                quantity = int(input("Enter the quantity: "))
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                print(self.add_to_cart(user_id, product_id, quantity))
            except ValueError:
                print("Invalid input. Please enter a valid product ID.")

        print("\nChecking out:")
        print(self.checkout(user_id))

# Example usage:

ecommerce = EcommerceSystem()
ecommerce.simulate_user_interaction()
print("Done")
