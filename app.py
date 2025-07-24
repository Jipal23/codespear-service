from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to micro lending backend"

@app.route('/api/register', methods=['POST'])
def approve_or_not():
    data = request.get_json()
    annual_income = data.get('annualIncome')
    
    if annual_income < 150000:
        response = {
            'status': 'rejected',
            'credit_limit': 0,
            'interest_rate': None,
            'tenure': 0
        }
    elif annual_income <= 300000:
        response = {
            'status': 'approved',
            'credit_limit': 500000,
            'interest_rate': 18,
            'tenure': 2
        }
    elif annual_income <= 600000:
        response = {
            'status': 'approved',
            'credit_limit': 1000000,
            'interest_rate': 15,
            'tenure': 3
        }
    elif annual_income <= 1000000:
        response = {
            'status': 'approved',
            'credit_limit': 1500000,
            'interest_rate': 12,
            'tenure': 4
        }
    elif annual_income <= 1500000:
        response = {
            'status': 'approved',
            'credit_limit': 2000000,
            'interest_rate': 10,
            'tenure': 5
        }
    else:
        response = {
            'status': 'approved',
            'credit_limit': 2500000,
            'interest_rate': 8,
            'tenure': 6
        }

    return jsonify(response), 200

# @app.route('/api/data', methods=['POST'])
# def receive_data():
#     data = request.get_json()
#     if not data:
#         return jsonify({"error": "No JSON received"}), 400
#     return jsonify({
#         "received": data,
#         "status": "success"
#     })

if __name__ == '__main__':
    app.run(debug=True)
