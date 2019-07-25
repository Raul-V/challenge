from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database
from models.solution import Solution
import os

app = Flask(__name__)

@app.before_first_request
def create_database_tables():
    #create_database(DB_URI)
    db.create_all()

@app.route('/queens', methods = ['GET'])
def get_n_queens_solutions():
    queens_quantity = int(request.args.get('n', 8))
    solution = Solution(4, '[1,2,3,4]')
    solution.save()
    return f'how many queens? {queens_quantity}'

if __name__ == '__main__':
    from db import db
    from config import config
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = config['DB_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.run(host='0.0.0.0', debug=False)
