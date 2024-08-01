from flask import Flask, jsonify

app = Flask(__name__)

users = [
	{"id": 1, "name": "User1", "email": "user1@example.com"}
	{"id": 2, "name": "User2", "email": "user2@example.com"}

]

@app.route('/users', methods=['GET'])
def get_users():
	return jsonify(users)

if __name__ == '__main__':
	app.run(port=5003, host='0.0.0.0')


