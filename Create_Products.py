from Products import products

def create_products(name, price):
    product = {
        "name": name,
        "price": price
    }
    products.append(product)
    print("Product added successfully")
    return products
