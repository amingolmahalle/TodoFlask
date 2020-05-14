from flask import make_response, jsonify
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
from Core.Redis import Redis
import random

app = Swagger('User')


@app.route(
    '/SendOtp',
    methods=["post"],
    tags='login',
    summary='send otp for user',
    validations=dict(
        mobile_number='required string mobile'
    )
)
def send_otp(data):
    key = f'otp::{data.mobile_number}'
    redis = Redis()
    ttl = redis.ttl(key)

    if ttl < 1:
        ttl = 120
        code = random.randrange(1111, 9999)
        redis.setex(key, ttl, code)

    return make_response(jsonify(f'otp code for {data.mobile} is {redis.get(key).decode("utf8")}.'),
                         StatusCode.OK.value)


@app.route(
    '/getByIdWithQuery/<int:userId>',
    methods=["get"],
    tags='user',
    summary='get user by id with query',
)
def get_by_id_with_query(userId):
    map_request = GetUserByIdWithQueryRequest(userId)
    response = GetUserByIdWithQueryService().Execute(map_request)

    result = user_schema.dump(response)

    return jsonify(result)


@app.route(
    '/getAllByPagination',
    methods=["post"],
    tags='user',
    summary='get all data by pagination',
    validations=dict(
        page='int',
        per_page='int'
    )
)
def get_all_by_pagination(data):
    map_request = GetAllUserByPaginationRequest(data.page, data.per_page)

    response = GetAllUserByPaginationService().Execute(map_request)

    result = users_schema.dump(response)

    return make_response(jsonify(result), StatusCode.OK.value)


@app.route(
    '/getAll',
    methods=["get"],
    tags='user',
    summary='retrieve users info'
)
def get_all():
    response = GetAllUserService().Execute()

    result = users_schema.dump(response)

    return make_response(jsonify(result), StatusCode.OK.value)


@app.route(
    '/getById/<int:userId>',
    methods=["get"],
    tags='user',
    summary='get user by id'
)
def get_by_id(userId):
    map_request = GetUserByIdRequest(userId)
    response = GetUserByIdService().Execute(map_request)

    result = user_schema.dump(response)

    return make_response(jsonify(result), StatusCode.OK.value)


@app.route(
    '/getByMobile/<string:mobile>',
    methods=["get"],
    tags='user',
    summary='get user by mobile number'
)
def get_by_mobile(mobile):
    map_request = GetUserByMobileRequest(mobile)
    response = GetUserByMobileService().Execute(map_request)

    result = user_schema.dump(response)

    return make_response(jsonify(result), StatusCode.OK.value)


@app.route(
    '/add',
    methods=['post'],
    tags='user',
    summary='add new user',
    validations=dict(
        fullname='required string',
        mobile_number='required string mobile',
        birth_date='required datetime',
        email='required string email',
        addresses='list'
    )
)
def add(data):
    map_request = AddUserRequest(
        data.fullname,
        data.mobile_number,
        data.birth_date,
        data.email,
        data.addresses)

    AddUserService().Execute(map_request)

    return make_response(jsonify({}), StatusCode.OK.value)


@app.route(
    '/edit/<int:userId>',
    methods=['put'],
    tags='user',
    summary='edit user',
    validations=dict(
        fullname='string',
        mobile_number='string mobile',
        birth_date='datetime',
        email='string email',
        status='bool',
        addresses='list'
    )
)
def edit(userId, data):
    edit_user = EditUserRequest(
        userId,
        data.fullname,
        data.mobile_number,
        data.birth_date,
        data.email,
        data.status,
        data.addresses)

    EditUserService().Execute(edit_user)

    return make_response(jsonify({}), StatusCode.OK.value)


@app.route(
    '/delete/<int:userId>',
    methods=['delete'],
    tags='user',
    summary='delete user',
    validations=dict(
        userId='required int'
    )
)
def delete_by_id(userId):
    map_request = DeleteUserRequest(userId)

    DeleteUserService().Execute(map_request)

    return make_response(jsonify({}), StatusCode.OK.value)
