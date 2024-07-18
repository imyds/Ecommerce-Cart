# Ecommerce-Cart
A basic e-commerce system using Python and SQLite. Users can view available products, add items to their cart, view cart details, and checkout. This project demonstrates fundamental concepts of database management and user interaction, making it ideal for beginners to learn Python-SQLite integration in building simple applications.

# Simple E-commerce System

This is a basic e-commerce system implemented in Python using SQLite. It allows users to view available products, add products to their cart, view the cart, and checkout.

## Features

- View available products
- Add products to the cart
- View the cart with total cost
- Checkout and clear the cart

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/simple-ecommerce-system.git
    cd simple-ecommerce-system
    ```

2. No additional packages are required; the project uses Python's built-in `sqlite3` module.

### Usage

1. Run the script:

    ```sh
    python ecommerce_system.py
    ```

2. Follow the on-screen instructions to interact with the e-commerce system.

## Code Overview

The main functionality is contained in the `EcommerceSystem` class:

- `__init__`: Initializes the SQLite database and creates tables for products and cart.
- `add_sample_products`: Adds sample products to the database.
- `display_available_products`: Displays available products.
- `add_to_cart`: Adds a specified quantity of a product to the user's cart.
- `view_cart`: Displays the contents of the user's cart and the total cost.
- `checkout`: Finalizes the purchase and clears the cart.
- `simulate_user_interaction`: Simulates user interaction with the e-commerce system.

### Example Usage

The example below demonstrates how to use the `EcommerceSystem` class:

```python
ecommerce = EcommerceSystem()
ecommerce.simulate_user_interaction()
print("Done")

Sample Output
Welcome to our e-commerce system!
Available products:
1. Laptop - ₹999.99
2. Mouse - ₹29.99
3. Keyboard - ₹59.99
Enter the product ID you want to purchase (0 to checkout): 1
Enter the quantity: 1
Added 1 Laptop to cart.
Enter the product ID you want to purchase (0 to checkout): 2
Enter the quantity: 2
Added 2 Mouse to cart.
Enter the product ID you want to purchase (0 to checkout): 0

Checking out:
Checkout successful!

Cart contents:
Laptop: 1 x ₹999.99 = ₹999.99
Mouse: 2 x ₹29.99 = ₹59.98
Total: ₹1059.97

Happy Shopping!
Done

