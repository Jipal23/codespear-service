from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    mobileNumber = db.Column(db.String(15), unique=True, nullable=False)
    annualIncome = db.Column(db.Integer, nullable=False)
    creditLimit = db.Column(db.Integer)
    interestRate = db.Column(db.Float)
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
