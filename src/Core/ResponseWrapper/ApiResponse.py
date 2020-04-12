from flask import jsonify, make_response
from Core.ResponseWrapper.StatusCode import StatusCode


class ValidationFailedException(Exception):
    def __init__(self, message: str, validation: dict):
        Exception.__init__(self)
        self.message = message
        self.status_code = StatusCode.BadRequest.value
        self.validation = validation

    def __str__(self):
        return self.message


def MakeResponse(data: any = None, status_code: StatusCode = StatusCode.OK):
    if isinstance(data, str):
        response = make_response(data)
    else:
        response = jsonify(data)

    response.headers['content-type'] = 'application/json'
    response.status_code = status_code.value

    return response
