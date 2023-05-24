# products = [
#     {
#         "id": 1,
#         "name": "thumsup",
#         "price": 30
#     },
#     {
#         "id": 2,
#         "name": "Coke",
#         "price": 40
#     },
#     {
#         "id": 3,
#         "name": "Pepsi",
#         "price": 35
#     },
#     {
#         "id": 4,
#         "name": "Sprite",
#         "price": 35
#     },
#     {
#         "id": 5,
#         "name": "Fanta",
#         "price": 30
#     }
# ]



# #products will be in a seperate file
# #create product(name, price)
# #getting all the products
# #getting a single product(name)
# #updating a product(name)
# #app.py file where you 
# # are going to acll all theese functions and print them


from app import mongo

def insert_initial_products():
    products = [
        {
            "_id": 1,
            "name": "thumsup",
            "price": 30
        },
        {
            "_id": 2,
            "name": "Coke",
            "price": 40
        },
        {
            "_id": 3,
            "name": "Pepsi",
            "price": 35
        },
        {
            "_id": 4,
            "name": "Sprite",
            "price": 35
        },
        {
            "_id": 5,
            "name": "Fanta",
            "price": 30
        }
    ]

    # Ensure the collection is empty before inserting
    mongo.db.products.drop()

    # Inserting products into MongoDB
    mongo.db.products.insert_many(products)

insert_initial_products()
