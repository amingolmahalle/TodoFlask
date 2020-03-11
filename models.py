from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


class Person(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(30), nullable=False)
    mobile = db.Column(db.String(11), unique=True, nullable=False)
    birthDate = db.Column(db.DateTime)
    email = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=True)
    creationDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, mobile, birth_date, email, status):
        self.name = name
        self.mobile = mobile
        self.birthDate = birth_date
        self.email = email
        self.status = status
