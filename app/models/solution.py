from db import db
import datetime


class Solution(db.Model):
    __tablename__ = 'solution'
    id = db.Column(db.Integer, primary_key = True)
    n = db.Column(db.Integer, nullable = False)
    solution = db.Column(db.Text, unique = True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, n, solution):
        self.n = n
        self.solution = solution
    

    def save(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def find_by_n(cls, n):
        return cls.query.filter_by(n = n)
