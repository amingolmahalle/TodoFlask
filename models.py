from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Person(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, db.Sequence('seq_reg_id', start=1, increment=1), primary_key=True)
    code = db.Column(db.String(36), unique=True, nullable=False)
    fullName = db.Column(db.String(30), index=True, nullable=False)
    mobile = db.Column(db.String(11), unique=True, nullable=False)
    birthDate = db.Column(db.DateTime)
    email = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=True)
    creationDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, code, fullname, mobile, birth_date, email, status):
        self.code = code
        self.fullname = fullname
        self.mobile = mobile
        self.birth_date = birth_date
        self.email = email
        self.status = status
