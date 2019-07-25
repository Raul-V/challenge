from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.solution import Solution
from strategies.backtracking_nqueen import BacktrackingNQueensSolver

app = Flask(__name__)

@app.before_first_request
def create_database_tables():
    db.create_all()


@app.route('/queens', methods = ['GET'])
def get_n_queens_solutions():

    query_parameter = request.args.get('n', '8')
    _queens_quantity_validation(query_parameter)

    queens_quantity = int(query_parameter)

    db_solutions = _find_calculated_solutions(queens_quantity)
    if db_solutions:
        return jsonify(db_solutions), 200

    return jsonify(_calculate_solutions(queens_quantity)), 200


def _queens_quantity_validation(n):
    if not n.isdigit():
        raise Exception(f'Parameter n must be an integer number, found {n}')
    queens_quantity = int(n)
    if queens_quantity < 4:
        raise Exception(f'Parameter n must greater than 3, found {n}')


def _find_calculated_solutions(n):
    database_solutions = Solution.find_by_n(n)
    if database_solutions:
        database_solutions = [s.solution.split(',') for s in database_solutions]
        return [int(i) for i in database_solutions]
    return


def _calculate_solutions(n):
    queens_solver = BacktrackingNQueensSolver(n)
    all_solutions = queens_solver.find_all_solutions()

    for sol in all_solutions:
        database_solution = Solution(n, str(sol).strip('[]'))
        database_solution.save()


if __name__ == '__main__':
    from db import db
    from config import config
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = config['DB_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.run(host='0.0.0.0', debug=False)
