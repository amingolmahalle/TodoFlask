from enum import Enum


class StatusCode(Enum):
    OK = 200
    Created = 201
    Accepted = 203
    Unauthorized = 401
    BadRequest = 400
