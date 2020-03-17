from flask import Blueprint, request, jsonify
from main import db
from models import Person, person_schema, people_schema
import Utils.datetime as dt
import uuid

sub = Blueprint('todo_api', __name__, url_prefix='/api/people')


@sub.route('/getAll')
def get_all():
    response = Person.query.all()
    result = people_schema.dump(response)

    return jsonify(result)


@sub.route('/getById/<int:id>')
def get_by_id(id):
    response = Person.query.get(id)
    result = person_schema.dump(response)

    return jsonify(result)


@sub.route('/getByMobile/<string:mobile>')
def get_by_mobile(mobile):
    response = Person.query.filter_by(mobile_number=mobile).first()
    result = person_schema.dump(response)

    return jsonify(result)


@sub.route('/add', methods=['POST'])
def add():
    if not request.is_json:
        raise Exception('Request Invalid. Because json Format Incorrect.')

    request_data = request.get_json()

    code = str(uuid.uuid4())
    fullname = request_data.get('fullname')
    mobile_number = request_data.get('mobile_number')
    birth_date = request_data.get('birth_date')
    email = request_data.get('email')
    status = True
    modified_date = None

    new_person = Person(code, fullname, mobile_number, birth_date, email, status, modified_date)

    db.session.add(new_person)
    db.session.commit()

    return person_schema.jsonify(new_person)


@sub.route('/edit/<int:id>', methods=['PUT'])
def edit(id):
    if not request.is_json:
        raise Exception('Request Invalid. Because json Format Incorrect.')

    request_data = request.get_json()

    fullname = request_data.get('fullname', None)
    mobile_number = request_data.get('mobile_number', None)
    birth_date = request_data.get('birth_date', None)
    email = request_data.get('email', None)
    status = request_data.get('status', None)

    current_person = Person.query.get(id)

    current_person.fullname = fullname
    current_person.mobile_number = mobile_number
    current_person.birth_date = birth_date
    current_person.email = email
    current_person.status = status if status is not None else current_person.status
    current_person.modified_date = dt.datetime_now_utc()

    db.session.commit()

    return person_schema.jsonify(current_person)


@sub.route('/delete/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    person = Person.query.get(id)

    db.session.delete(person)

    db.session.commit()

    return 'OK!'
