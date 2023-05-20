from Products import Products

def Update_Product(name, price):
    for product in Products:
        if product["name"] == name:
            product["price"] = price
            print("Product updated successfully")
            return Products
    print("Product not found")
    return Products