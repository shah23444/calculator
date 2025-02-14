from datetime import datetime
from app import db

class CalculationHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expression = db.Column(db.String(255), nullable=False)
    result = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Calculation {self.expression} = {self.result}>'
