from flask import Flask, jsonify, request
from Create_Products import create_products
from GetAllProducts import get_all_products
from Update_product import Update_Product


app = Flask(__name__)

@app.route('/Products')
def get_Products():
    products = get_all_products()
    return jsonify(products)



@app.route('/Products', methods=['POST'])
def add_product():
    name = request.json.get('name')
    price = request.json.get('price')
    if name and price:
        create_products(name, price)
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

if __name__ == '__main__':
    app.run(debug=True)





