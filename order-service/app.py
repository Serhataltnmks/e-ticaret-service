from flask import Flask, jsonify

app = Flask(__name__)

orders = [
        {"id": 1, "product_id": 1, "quantity:": 2}
        {"id": 2, "product_id": 2, "quantity:": 1}
]

@app.route('/orders', methods=['GET'])
def get_orders():
        return jsonify(orders)

if __name__ == '__main__':
        app.run(port=5002, host='0.0.0.0')

