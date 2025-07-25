from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User
import joblib
import pandas as pd
from utility_functions import calculate_credit_limit, calculate_tenure, calculate_interest_rate

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
    
    model = joblib.load('credit_score_model.pkl')
    encoders = joblib.load('encoders.pkl')
    feature_columns = joblib.load('feature_columns.pkl')
    
    input = {
        'annual_income':int(data.get('annualIncome').replace(",", "").strip()),
        'employment_status':data.get('employmentStatus'),
        'reason_for_loan':data.get('reason'),
        'dependent_count': int(data.get('dependents').replace(",", "").strip()),
        'bank_transactions': int(data.get('bankCredit').replace(",", "").strip()),
        'last_utility_bill_amount': int(data.get('gasBillAmountMonthly').replace(",", "").strip()),
        'last_mobile_recharge_amount': int(data.get('propertyBillAmountMonthly').replace(",", "").strip()),
        'vehicle_owner': data.get('isVehicle'),
        'realty_ownership': data.get('isShop'),
        'date_of_birth': data.get('dateOfBirth'),
        'dependents': int(data.get('dependents').replace(",", "").strip())
    }
    
    input_df = pd.DataFrame([input])
    # input['date_of_birth'] = pd.to_datetime(input_df['date_of_birth'])
    input_df['date_of_birth'] = pd.to_datetime(input_df['date_of_birth'], errors='coerce')
    input_df['age'] = 2025 - input_df['date_of_birth'].dt.year
    input_df.drop(columns=['date_of_birth'], inplace=True)
    
    # for col in encoders:
    #     input_df[col] = encoders[col].transform(input_df[col])

    for col in encoders:
        known_classes = set(encoders[col].classes_)
        input_df[col] = input_df[col].apply(
            lambda x: encoders[col].transform([x])[0] if x in known_classes else -1
        )


    input_df = input_df[feature_columns]

    credit_score = model.predict(input_df)[0]
    
    if credit_score >= 60:
        credit_limit = calculate_credit_limit(annual_income,credit_score)
        tenure = calculate_tenure(credit_score)
        interest_rate = calculate_interest_rate(credit_score)
            
        result = {
            'status':'partial',
            'credit_limit':round(credit_limit, 2),
            'tenure':tenure,
            'interest_rate':round(interest_rate, 2)
        }
    else:
        result = {
            'status':'rejected',
            'credit_limit':0,
            'tenure':0,
            'interest_rate':None
        }
        
    user = User(
        name=name,
        mobile_number=mobile_number,
        annual_income=annual_income,
        credit_limit=result['credit_limit'],
        interest_rate=result['interest_rate'],
        tenure=result['tenure'],
        status=result['status']
    )
    db.session.add(user)
    db.session.commit()

    return jsonify(result), 200

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=8080, debug=False)
