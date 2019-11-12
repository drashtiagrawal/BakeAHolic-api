from flask import Flask
from flask import request
import json
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

items = {"Bread" : "50",
		 "Black Forest Cake" : "250"}

shoppingCart = {}

@app.route('/v1/items', methods=['GET'])
def funItems():
	if request.method == 'GET':		
		return json.dumps(items)

@app.route('/v1/addItem', methods=['POST'])
def addItems():
	if request.method == 'POST':
		print(request.get_json())
		data = request.get_json()
		shoppingCart[data['itemName']] = data['number']
		# print(shoppingCart)
		return 'Data Posted'

@app.route('/v1/cart', methods=['GET'])
def showCart():
	if request.method == 'GET':		
		return json.dumps(shoppingCart)

@app.route('/v1/cart', methods=['DELETE'])
def clearCart():
	if request.method == 'DELETE':
		cart = shoppingCart.copy()
		shoppingCart.clear()		
		return json.dumps(cart)

if __name__ == '__main__':
	app.run(debug = True)

