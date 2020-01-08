from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# init app
app = Flask(__name__)

# app.secret_key="hello"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://develop:Aa123456!@tcp(localhost:3306)/my_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    mobile = db.Column(db.String(11), unique=True, nullable=False)
    birth_date = db.Column(db.DateTime)
    email = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=True)

    def __init__(self, name, mobile, birth_date, email, status):
        self.name = name
        self.mobile = mobile
        self.birthDate = birth_date
        self.email = email
        self.status = status


# Apis
@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Hello World'})


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5050)
