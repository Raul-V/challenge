from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from services.nqueens_service import NQueenService
app = Flask(__name__)

@app.before_first_request
def create_database_tables():
    db.create_all()


@app.route('/queens', methods = ['GET'])
def get_n_queens_solutions():

    query_parameter = request.args.get('n', '8')
    _queens_quantity_validation(query_parameter)

    queens_quantity = int(query_parameter)
    nqueen_service = NQueenService(queens_quantity)
    solutions = nqueen_service.calculate_solutions()

    return jsonify(solutions), 200


if __name__ == '__main__':
    from db import db
    from config import config
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = config['DB_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.run(host='0.0.0.0', debug=False)
