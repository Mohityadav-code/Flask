from Products import products

def create_products(id, name, price):
    product = {
        "id": id,
        "name": name,
        "price": price
    }
    products.append(product)
    print("Product added successfully")
    return products
