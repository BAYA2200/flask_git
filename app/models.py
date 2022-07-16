from . import db, bcrypt

from flask_login import UserMixin

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.String(30))
    value = db.Column(db.Integer(), nullable=False)
    status = db.Column(db.String(30))
    init = db.Column(db.String(30))
    subject = db.Column(db.String(30))
