from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Person(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, db.Sequence('seq_reg_id', start=1, increment=1), primary_key=True)
    code = db.Column(db.String(36), unique=True, nullable=False)
    fullname = db.Column(db.String(30), index=True, nullable=False)
    mobile_number = db.Column(db.String(11), unique=True, nullable=False)
    birth_date = db.Column(db.DateTime)
    email = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=True)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_date = db.Column(db.DateTime, nullable=True)

    def __init__(self, code, fullname, mobile_number, birth_date, email, status, modified_date):
        self.code = code
        self.fullname = fullname
        self.mobile_number = mobile_number
        self.birth_date = birth_date
        self.email = email
        self.status = status
        self.modified_date = modified_date


# Person Schema
class PersonSchema(ma.Schema):
    class Meta:
        fields = ('id', 'code', 'fullname', 'mobile_number', 'birth_date',
                  'email', 'status', 'creation_date', 'modified_date')


# Init Schema
person_schema = PersonSchema()
people_schema = PersonSchema(many=True)
