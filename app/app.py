from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route('/queens', methods = ['GET'])
def get_n_queens_solutions():
    return 'Hello'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
