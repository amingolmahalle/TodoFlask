from flask import Blueprint, request
from models import db

sub = Blueprint('hello_api', __name__, url_prefix='/api/people')


@sub.route('/getAll')
def get_all():
    return db.query.all()


@sub.route('/getById/<int:id>')
def get_by_id():
    return db.query.get(id)


@sub.route('/add', methods=['POST'])
def add():
    request_data = request.json if request.is_json else request.form

    fullname = request_data['fullname']
    mobile = request_data['mobile']
    birth_date = request_data['birth_date']
    email = request_data['email']
    status = request_data['status']

    new_person = db(id, fullname, mobile, birth_date, email, status)

    db.add(new_person)

    try:
        db.session.commit()
    except:
        db.session.rollback()


@sub.route('/edit/<int:id>', methods=['PUT'])
def edit(id):
    request_data = request.json if request.is_json else request.form

    fullname = request_data['fullname']
    mobile = request_data['mobile']
    birth_date = request_data['birth_date']
    email = request_data['email']
    status = request_data['status']

    person = db.query.get(id)

    person.fullname = fullname
    person.mobile = mobile
    person.birth_date = birth_date
    person.email = email
    person.status = status

    try:
        db.session.commit()
    except:
        db.session.rollback()


@sub.route('/delete/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    person = db.query.get(id)

    db.session.delete(person)

    try:
        db.session.commit()
    except:
        db.session.rollback()
