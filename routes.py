from flask import render_template, jsonify, request
from app import db
from models import CalculationHistory

def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/history', methods=['GET'])
    def get_history():
        history = CalculationHistory.query.order_by(CalculationHistory.created_at.desc()).limit(10).all()
        return jsonify([{
            'expression': calc.expression,
            'result': calc.result,
            'created_at': calc.created_at.isoformat()
        } for calc in history])

    @app.route('/api/calculate', methods=['POST'])
    def save_calculation():
        data = request.get_json()
        calculation = CalculationHistory(
            expression=data['expression'],
            result=data['result']
        )
        db.session.add(calculation)
        db.session.commit()
        return jsonify({'status': 'success'})

    return app
