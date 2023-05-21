from Products import products
from Cart import cart

def add_to_cart(product_id):
    print(product_id)
    # Find the product with the given id
    for product in products:
        if product['id'] == product_id:
            # Check if the product is already in the cart
            if product not in cart:
                cart.append(product)
                print("Product added to cart successfully.")
                return True
            else:
                print("Product already in the cart.")
                return False
    print("Product not found.")
    return False
