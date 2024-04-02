from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # You can now use the data from the request body
    # For example, print it to the console
    prediction = True
    return jsonify({"prediction":prediction})

if __name__ == '__main__':
    app.run(debug=True)