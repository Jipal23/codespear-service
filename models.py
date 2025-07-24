from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    mobile_number = db.Column(db.String(15), unique=True, nullable=False)
    annual_income = db.Column(db.Integer, nullable=False)
    credit_limit = db.Column(db.Integer)
    interest_rate = db.Column(db.Float)
    tenure = db.Column(db.Float)
    status = db.Column(db.String(20))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'mobileNumber':self.mobileNumber,
            'annualIncome': self.annualIncome,
            'creditLimit': self.creditLimit,
            'interestRate': self.interestRate,
            'tenure': self.tenure,
            'status': self.status
        }
