from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Root route to confirm app is running
@app.route('/')
def home():
    return "Flask Login Monitor App is running"

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
    # Azure requires host 0.0.0.0 and dynamic port
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

