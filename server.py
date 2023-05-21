from flask import Flask, jsonify, request
from Create_Products import create_products
from GetAllProducts import get_all_products
from Update_product import Update_Product
from Getting_A_single_Product import get_a_single_product
from Cart import cart
from Products import products


app = Flask(__name__)

@app.route('/Products')
def get_Products():
    products = get_all_products()
    return jsonify(products)

@app.route('/Products/<name>')
def get_a_single_product_(name):
    product = get_a_single_product(name)
    return jsonify(product)

@app.route('/Products', methods=['POST'])
def add_product():
    name = request.json.get('name')
    price = request.json.get('price')
    cartLen=products.__len__()
    id=cartLen+1
    if name and price:
        create_products( id,name, price)
        return jsonify({"message": "Product created successfully."}), 201
    else:
        return jsonify({"error": "Invalid data."}), 400

@app.route('/Products/<name>', methods=['PUT'])
def update_product_price(name):
    new_price = request.json.get('price')
    success = Update_Product(name, new_price)
    if success:
        return jsonify({"message": "Product price updated successfully."})
    else:
        return jsonify({"error": "Product not found."}), 404



#  Next Day Task


from AddToCart import add_to_cart 
from GetCart import get_cart
from ClearCart import clear_cart

@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to our API!"})

# Cart APIs

@app.route('/cart/add/<int:product_id>', methods=['POST'])
def add_product_to_cart(product_id):
    success = add_to_cart(product_id)
    if success:
        return jsonify({"message": "Product added to cart successfully."})
    else:
        return jsonify({"error": "Product not found or already in the cart."}), 400

@app.route('/cart', methods=['GET'])
def view_cart():
    cart, total_price = get_cart()
    if cart:
        return jsonify({"cart": cart, "total_price": total_price})
    else:
        return jsonify({"message": "The cart is empty."})

@app.route('/cart', methods=['DELETE'])
def clear_cart_item():
    clear_cart()
    return jsonify({"message": "Cart cleared successfully."})




#  Next Day Task  ( 2 ) Adding orders from cart 


if __name__ == '__main__':
    app.run(debug=True)