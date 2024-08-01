from flask import Flask, jsonify

app = Flask(__name__)

product = [
	{"id": 1, "name": "Product 1", "price:": 100}
	{"id": 2, "name": "Product 2", "price:": 100}
]

@app.route('/product', methods=['GET'])
def get_product():
	return jsonify(product)

if __name__ == '__main__':
	app.run(port=5001, host='0.0.0.0')

