from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    # Simulate a user database
    users = {
        "name" : "jude",
        "age" : 30,
        "email" : "jude144@gmail.com",
        "username": username
    }
    
    extra = request.args.get('extra', 'false').lower()
    if extra:
            users["extra"] = extra
    return jsonify(users), 200

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    # Simulate user creation
    user = {
        "username": data['username'],
        "name": data.get('name', 'Unknown'),
        "age": data.get('age', 0),
        "email": data.get('email', '')
    }
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(debug=True)

