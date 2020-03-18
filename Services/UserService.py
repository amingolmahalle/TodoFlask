from flask import Blueprint, request, jsonify
from Models.user import User, user_schema, users_schema
import Repositories.UserRepository as userRepository
import Utils.datetime as dt
import uuid

sub = Blueprint('todo_api', __name__, url_prefix='/api/users')


@sub.route('/getAll')
def get_all():
    response = userRepository.get_all()
    result = users_schema.dump(response)

    return jsonify(result)


@sub.route('/getById/<int:id>')
def get_by_id(id):
    response = userRepository.get_by_id(id)
    result = user_schema.dump(response)

    return jsonify(result)


@sub.route('/getByMobile/<string:mobile>')
def get_by_mobile(mobile):
    response = userRepository.get_by_mobile(mobile)
    result = user_schema.dump(response)

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

    new_user = User(code, fullname, mobile_number, birth_date, email, status, modified_date)

    userRepository.add(new_user)
    userRepository.commit()

    return user_schema.jsonify(new_user)


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

    current_user = userRepository.get_by_id(id)

    current_user.fullname = fullname
    current_user.mobile_number = mobile_number
    current_user.birth_date = birth_date
    current_user.email = email
    current_user.status = status if status is not None else current_user.status
    current_user.modified_date = dt.datetime_now_utc()

    userRepository.commit()

    return user_schema.jsonify(current_user)


@sub.route('/delete/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    user = userRepository.get_by_id(id)

    userRepository.delete(user)

    userRepository.commit()

    return 'OK!'
