from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://mohityadav3552:HqnaHCf_3E3Td3Q@cluster0.mfadw7s.mongodb.net/test"  # replace 'test' with your database name
mongo = PyMongo(app)


from Products import insert_initial_products

@app.route('/Products')
def get_Products():
    products = mongo.db.products.find()
    response = []
    for product in products:
        product['_id'] = str(product['_id'])
        response.append(product)
    return jsonify(response)

@app.route('/Products/<name>')
def get_a_single_product_(name):
    product = mongo.db.products.find_one({"name": name})
    if product:
        product['_id'] = str(product['_id'])
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found."}), 404

@app.route('/Products', methods=['POST'])
def add_product():
    name = request.json.get('name')
    price = request.json.get('price')
    if name and price:
        id = mongo.db.products.find().count() + 1
        product = {"_id": id, "name": name, "price": price}
        mongo.db.products.insert_one(product)
        return jsonify({"message": "Product created successfully."}), 201
    else:
        return jsonify({"error": "Invalid data."}), 400

@app.route('/Products/<name>', methods=['PUT'])
def update_product_price(name):
    new_price = request.json.get('price')
    if new_price:
        mongo.db.products.update_one(
            {"name": name},
            {"$set": {"price": new_price}}
        )
        return jsonify({"message": "Product price updated successfully."})
    else:
        return jsonify({"error": "Product not found or invalid price."}), 400



# Cart

@app.route('/cart/add/<int:product_id>', methods=['POST'])
def add_product_to_cart(product_id):
    product = mongo.db.products.find_one({"_id": product_id})
    if product:
        cart_item = mongo.db.cart.find_one({"_id": product_id})
        if cart_item:
            return jsonify({"error": "Product already in the cart."}), 400
        else:
            mongo.db.cart.insert_one(product)
            return jsonify({"message": "Product added to cart successfully."})
    else:
        return jsonify({"error": "Product not found."}), 400

@app.route('/cart', methods=['GET'])
def view_cart():
    cart_items = list(mongo.db.cart.find())
    if cart_items:
        for item in cart_items:
            item['_id'] = str(item['_id'])
        total_price = sum(item['price'] for item in cart_items)
        return jsonify({"cart": cart_items, "total_price": total_price})
    else:
        return jsonify({"message": "The cart is empty."})


@app.route('/cart', methods=['DELETE'])
def clear_cart_item():
    mongo.db.cart.drop()
    return jsonify({"message": "Cart cleared successfully."})
