from Products import products
def get_a_single_product(name):
    for product in products:
        if product["name"] == name:
            print("Product found")
            return product
    print("Product not found")
    return products