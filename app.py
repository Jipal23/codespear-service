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
    annual_income_raw = data.get('annualIncome')
    
    try:
        annual_income = int(annual_income_raw.replace(",", "").strip())
    except ValueError:
        return jsonify({'error': 'Annual income must be a number'}), 400
    
    if annual_income < 150000:
        response = {
            'status': False,
            'credit_limit': 0,
            'interest_rate': None,
            'tenure': 0
        }
    elif annual_income <= 300000:
        response = {
            'status': True,
            'creditLimit': 500000,
            'interestRate': 18,
            'tenure': 2
        }
    elif annual_income <= 600000:
        response = {
            'status': True,
            'creditLimit': 1000000,
            'interestRate': 15,
            'tenure': 3
        }
    elif annual_income <= 1000000:
        response = {
            'status': True,
            'creditLimit': 1500000,
            'interestRate': 12,
            'tenure': 4
        }
    elif annual_income <= 1500000:
        response = {
            'status': True,
            'creditLimit': 2000000,
            'interestRate': 10,
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
