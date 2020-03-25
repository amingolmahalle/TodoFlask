from flask import Blueprint, request, jsonify
from Models.Domain.User import User
from Models.Schema.UserSchema import user_schema, users_schema
from Models.Domain.Address import Address
import Services.UserService as userService
import uuid

sub = Blueprint('todo_api', __name__, url_prefix='/api/users')


@sub.route('/getAll_by_query', methods=["GET"])
def get_all_by_query():
    response = userService.get_all_by_query()
    result = users_schema.dump(response)

    return jsonify(result)


@sub.route('/getAll_by_pagination', methods=["POST"])
def get_all_by_pagination():
    if not request.is_json:
        raise Exception('Request Invalid. Because json Format Incorrect.')

    request_data = request.get_json()

    page = request_data.get('page', 1)
    per_page = request_data.get('per_page', 10)

    response = userService.get_all_by_pagination(page, per_page)
    result = users_schema.dump(response)

    return jsonify(result)


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


@sub.route('/getByMobile/<string:mobile>', methods=["GET"])
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

    new_user = User(code, fullname, mobile_number, birth_date, email, status)

    for address in request_data.get('addresses'):
        country_name = address['country_name']
        city_name = address['city_name']
        postal_code = address['postal_code']
        more_address = address['more_address']

        new_address = Address(country_name, city_name, postal_code, more_address)
        new_user.addresses.append(new_address)

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
