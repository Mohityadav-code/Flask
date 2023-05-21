from Cart import cart

def get_cart():
    total_price = sum(product['price'] for product in cart)
    print("Cart: ", cart)
    print("Total price: ", total_price)
    return cart, total_price
