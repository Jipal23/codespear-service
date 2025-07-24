from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    "postgresql://postgres:codespear%40micro-lending@34.134.167.26:5432/micro_lending"
)

db.init_app(app)

@app.route('/')
def home():
    return "Welcome to micro lending backend"

@app.route('/api/user', methods=['POST'])
def get_user_by_mobile():
    data = request.form
    mobile_number = data.get('mobile')

    user = User.query.filter_by(mobile_number).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # try:
    #     mobileNumber = int(mobileNumber)
    # except ValueError:
    #     return jsonify({'error': 'Invalid mobile number'}), 400

    # if(mobileNumber == 9999999999):
    #     result = {
    #     'creditLimit': 1500000,
    #     'interestRate': 12,
    #     'tenure': 4,
    #     'status': 'partial'
    # }
    # elif(mobileNumber == 1111111111):
    #     result = {
    #     'creditLimit': 2500000,
    #     'interestRate': 8,
    #     'tenure': 6,
    #     'status': 'partial'
    # }
    # else:
    #     result = {
    #     'creditLimit': 0,
    #     'interestRate': None,
    #     'tenure': 0,
    #     'status': 'rejected'
    #     }
        
    result = {
        'name': user.name,
        'mobile_number': user.mobile_number,
        'annual_income': user.annual_income,
        'credit_limit': user.credit_limit,
        'interest_rate': user.interest_rate,
        'tenure': user.tenure,
        'status': user.status
    }
    return jsonify(result), 200

@app.route('/api/register', methods=['POST'])
def approve_or_not():
    data = request.get_json()
    name = data.get('fullName')
    mobile_number = data.get('mobileNo')
    annual_income_raw = data.get('annualIncome')
    
    try:
        annual_income = int(annual_income_raw.replace(",", "").strip())
    except ValueError:
        return jsonify({'error': 'Annual income must be a number'}), 400
    
    
    if annual_income < 150000:
        result = {'status': 'rejected', 'creditLimit': 0, 'interestRate': None, 'tenure': 0}
    elif annual_income <= 300000:
        result = {'status': 'partial', 'creditLimit': 500000, 'interestRate': 18, 'tenure': 2}
    elif annual_income <= 600000:
        result = {'status': 'partial', 'creditLimit': 1000000, 'interestRate': 15, 'tenure': 3}
    elif annual_income <= 1000000:
        result = {'status': 'partial', 'creditLimit': 1500000, 'interestRate': 12, 'tenure': 4}
    elif annual_income <= 1500000:
        result = {'status': 'partial', 'creditLimit': 2000000, 'interestRate': 10, 'tenure': 5}
    else:
        result = {'status': 'partial', 'creditLimit': 2500000, 'interestRate': 8, 'tenure': 6}

        
    user = User(
        name=name,
        mobile_number=mobile_number,
        annual_income=annual_income,
        credit_limit=result['creditLimit'],
        interest_rate=result['interestRate'],
        tenure=result['tenure'],
        status=result['status']
    )
    db.session.add(user)
    db.session.commit()

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
