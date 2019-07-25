from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
from models.solution import Solution
app = Flask(__name__)

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


@app.before_first_request
def create_database_tables():
    db.create_all()

@app.route('/queens', methods = ['GET'])
def get_n_queens_solutions():
    queens_quantity = int(request.args.get('n', 8))
    solution = Solution(4, '[1,2,3,4]')
    solution.save()
    return f'how many queens? {queens_quantity}'


POSTGRES_URL = get_env_variable('POSTGRES_URL')
POSTGRES_USER = get_env_variable('POSTGRES_USER')
POSTGRES_PASS = get_env_variable('POSTGRES_PASS')
POSTGRES_DB = get_env_variable('POSTGRES_DB')

DB_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_URL}/{POSTGRES_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', debug=False)
