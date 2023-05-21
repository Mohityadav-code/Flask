from Products import products

def Update_Product(name, price):
    for product in products:
        if product["name"] == name:
            product["price"] = price
            print("Product updated successfully")
            return products
    print("Product not found")
    return products