from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User

app = Flask(__name__)
CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
#     f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
# )
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.init_app(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()

@app.route('/')
def home():
    return "Welcome to micro lending backend"

@app.route('/api/user', methods=['POST'])
def get_user_by_mobile():
    data = request.json()
    mobileNumber = data.get('mobile')

    # user = User.query.filter_by(mobileNumber).first()
    # if not user:
    #     return jsonify({'error': 'User not found'}), 404

    if(mobileNumber == 9999999999):
        result = {
        'creditLimit': 1500000,
        'interestRate': 12,
        'tenure': 4,
        'status': 'partial'
    }
    elif(mobileNumber == 1111111111):
        result = {
        'creditLimit': 2500000,
        'interestRate': 8,
        'tenure': 6,
        'status': 'partial'
    }
    else:
        result = {
        'creditLimit': 0,
        'interestRate': None,
        'tenure': 0,
        'status': 'rejected'
        }
        
    # result = {
    #     'name': user.name,
    #     'mobileNumber': user.mobileNumber,
    #     'annualIncome': user.annualIncome,
    #     'creditLimit': user.creditLimit,
    #     'interestRate': user.interestRate,
    #     'tenure': user.tenure,
    #     'status': user.status
    # }
    return jsonify(result), 200

@app.route('/api/register', methods=['POST'])
def approve_or_not():
    data = request.get_json()
    name = data.get('fullName')
    mobileNumber = data.get('mobileNumber')
    annual_income_raw = data.get('annualIncome')
    
    try:
        annualIncome = int(annual_income_raw.replace(",", "").strip())
    except ValueError:
        return jsonify({'error': 'Annual income must be a number'}), 400
    
    
    if annualIncome < 150000:
        result = {'status': 'rejected', 'creditLimit': 0, 'interestRate': None, 'tenure': 0}
    elif annualIncome <= 300000:
        result = {'status': 'partial', 'creditLimit': 500000, 'interestRate': 18, 'tenure': 2}
    elif annualIncome <= 600000:
        result = {'status': 'partial', 'creditLimit': 1000000, 'interestRate': 15, 'tenure': 3}
    elif annualIncome <= 1000000:
        result = {'status': 'partial', 'creditLimit': 1500000, 'interestRate': 12, 'tenure': 4}
    elif annualIncome <= 1500000:
        result = {'status': 'partial', 'creditLimit': 2000000, 'interestRate': 10, 'tenure': 5}
    else:
        result = {'status': 'partial', 'creditLimit': 2500000, 'interestRate': 8, 'tenure': 6}

        
    # user = User(
    #     name=name,
    #     mobileNumber=mobileNumber,
    #     annualIncome=annualIncome,
    #     creditLimit=result['creditLimit'],
    #     interestRate=result['interestRate'],
    #     tenure=result['tenure'],
    #     status=result['status']
    # )
    # db.session.add(user)
    # db.session.commit()

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
