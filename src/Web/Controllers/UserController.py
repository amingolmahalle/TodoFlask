from flask import make_response, request, jsonify
from Service.Commands.AddUser.AddUserService import AddUserService
from Service.Commands.EditUser.EditUserService import EditUserService
from Service.Commands.DeleteUser.DeleteUserService import DeleteUserService
from Service.Queries.GetAllUser.GetAllUserService import GetAllUserService
from Service.Queries.GetAllUserByPagination.GetAllUserByPaginationService import GetAllUserByPaginationService
from Service.Queries.GetUserById.GetUserByIdService import GetUserByIdService
from Service.Queries.GetUserByIdWithQuery.GetUserByIdWithQueryService import GetUserByIdWithQueryService
from Service.Queries.GetUserByMobile.GetUserByMobileService import GetUserByMobileService
from Domain.Service.Commands.AddUser.AddUserRequest import AddUserRequest
from Domain.Service.Commands.EditUser.EditUserRequest import EditUserRequest
from Domain.Service.Queries.GetUserByMobile.GetUserByMobileRequest import GetUserByMobileRequest
from Domain.Service.Queries.GetAllUserByPagination.GetAllUserByPaginationRequest import GetAllUserByPaginationRequest
from Domain.Service.Queries.GetUserById.GetUserByIdRequest import GetUserByIdRequest
from Domain.Service.Queries.GetUserByIdWithQuery.GetUserByIdWithQueryRequest import GetUserByIdWithQueryRequest
from Domain.Service.Commands.DeleteUser.DeleteUserRequest import DeleteUserRequest
from Domain.Schema.UserSchema import user_schema, users_schema
from Web.ResponseWrapper.StatusCode import StatusCode
from Core.Swagger import Swagger
from Core.Redis.Redis import Redis
from Utils.String import check_mobile
import random

app = Swagger('User')


@app.route(
    '/SendOtp/<string:mobile>',
    methods=["post"],
    tags='login',
    summary='send otp for user'
)
def send_otp(mobile):
    if not check_mobile(mobile):
        raise Exception('invalid mobile number')

    key = f'otp::{mobile}'
    redis = Redis()
    ttl = redis.ttl(key)

    if ttl < 1:
        ttl = 120
        code = random.randrange(1111, 9999)
        redis.setex(key, ttl, code)

    return make_response(jsonify(f'otp code for {mobile} is {redis.get(key).decode("utf8")}.'), StatusCode.OK.value)


@app.route(
    '/getByIdWithQuery/<int:userId>',
    methods=["get"],
    tags='user'
)
def get_by_id_with_query(userId):
    map_request = GetUserByIdWithQueryRequest(userId)
    response = GetUserByIdWithQueryService().Execute(map_request)

    result = user_schema.dump(response)

    return jsonify(result)


@app.route(
    '/getAllByPagination',
    methods=["post"],
    tags='user'
)
def get_all_by_pagination():
    if not request.is_json:
        raise Exception('Request Invalid. Because json Format Incorrect.')

    request_data = request.get_json()

    page = request_data.get('page', 1)
    per_page = request_data.get('per_page', 10)

    map_request = GetAllUserByPaginationRequest(page, per_page)

    response = GetAllUserByPaginationService().Execute(map_request)

    result = users_schema.dump(response)

    return make_response(jsonify(result), StatusCode.OK.value)


@app.route(
    '/getAll',
    summary='retrieve users info',
    methods=["get"],
    tags='user'
)
def get_all():
    response = GetAllUserService().Execute()

    result = users_schema.dump(response)

    return make_response(jsonify(result), StatusCode.OK.value)


@app.route(
    '/getById/<int:userId>',
    methods=["get"],
    tags='user'
)
def get_by_id(userId):
    map_request = GetUserByIdRequest(userId)
    response = GetUserByIdService().Execute(map_request)

    result = user_schema.dump(response)

    return make_response(jsonify(result), StatusCode.OK.value)


@app.route(
    '/getByMobile/<string:mobile>',
    methods=["get"],
    tags='user'
)
def get_by_mobile(mobile):
    map_request = GetUserByMobileRequest(mobile)
    response = GetUserByMobileService().Execute(map_request)

    result = user_schema.dump(response)

    return make_response(jsonify(result), StatusCode.OK.value)


@app.route(
    '/add',
    methods=['get'],
    tags='user'
)
def add():
    if not request.is_json:
        raise Exception('Request Invalid. Because json Format Incorrect.')

    request_data = request.get_json()

    fullname = request_data.get('fullname')
    mobile_number = request_data.get('mobile_number')
    birth_date = request_data.get('birth_date')
    email = request_data.get('email')
    addresses = request_data.get('addresses')

    map_request = AddUserRequest(fullname, mobile_number, birth_date, email, addresses)

    AddUserService().Execute(map_request)

    return make_response(jsonify({}), StatusCode.OK.value)


@app.route(
    '/edit/<int:userId>',
    methods=['put'],
    tags='user'
)
def edit(userId):
    if not request.is_json:
        raise Exception('Request Invalid. Because json Format Incorrect.')

    request_data = request.get_json()

    id = userId
    fullname = request_data.get('fullname', None)
    mobile_number = request_data.get('mobile_number', None)
    birth_date = request_data.get('birth_date', None)
    email = request_data.get('email', None)
    status = request_data.get('status', None)
    addresses = request_data.get('addresses')

    edit_user = EditUserRequest(id, fullname, mobile_number, birth_date, email, status, addresses)

    EditUserService().Execute(edit_user)

    return make_response(jsonify({}), StatusCode.OK.value)


@app.route(
    '/delete/<int:userId>',
    methods=['delete'],
    tags='user'
)
def delete_by_id(userId):
    map_request = DeleteUserRequest(userId)

    DeleteUserService().Execute(map_request)

    return make_response(jsonify({}), StatusCode.OK.value)
