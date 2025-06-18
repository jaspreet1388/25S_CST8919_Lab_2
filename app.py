from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Simulated check
    if username == 'admin' and password == 'password123':
        app.logger.info(f"Successful login for user: {username}")
        return jsonify({"message": "Login successful!"}), 200
    else:
        app.logger.warning(f"Failed login for user: {username}")
        return jsonify({"message": "Login failed!"}), 401

if __name__ == '__main__':
    app.run()

