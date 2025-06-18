from flask import Flask, request, jsonify
import os
import logging
import sys

app = Flask(__name__)

# Force logs to go to stdout so Azure App Service can collect them
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
app.logger.setLevel(logging.INFO)

@app.route('/')
def home():
    return "Flask Login Monitor App is running"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'password123':
        app.logger.info(f"Successful login attempt for user: {username}")
        return jsonify({"message": "Login successful!"}), 200
    else:
        app.logger.warning(f"Failed login attempt for user: {username}")
        return jsonify({"message": "Login failed!"}), 401

if __name__ == '__main__':
    # Azure expects the app to listen on 0.0.0.0 and dynamic port
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
