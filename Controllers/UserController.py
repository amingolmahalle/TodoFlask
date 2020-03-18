from flask import Blueprint, request, jsonify
from Models.User import User, user_schema, users_schema
import Services.UserService as userService
import uuid

sub = Blueprint('todo_api', __name__, url_prefix='/api/users')


@sub.route('/getAll', methods=["GET"])
def get_all():
    response = userService.get_all()
    result = users_schema.dump(response)

    return jsonify(result)


@sub.route('/getById/<int:id>', methods=["GET"])
def get_by_id(id):
    response = userService.get_by_id(id)
    result = user_schema.dump(response)

    return jsonify(result)


@sub.route('/getByMobile/<string:mobile>')
def get_by_mobile(mobile):
    response = userService.get_by_mobile(mobile)
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

    userService.add(new_user)

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

    edit_user = User(None, fullname, mobile_number, birth_date, email, status, None)

    current_user = userService.edit(id, edit_user)

    return user_schema.jsonify(current_user)


@sub.route('/delete/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    userService.delete_by_id(id)

    return 'OK!'
