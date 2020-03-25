from Models.Schema.SharedSchema import ma, fields
from Models.Domain.User import User
from Models.Schema.AddressSchema import addresses_schema


# User Schema
class UserSchema(ma.Schema):
    class Meta:
        model = User
    id = fields.Integer(required=True)
    code = fields.String(required=True)
    fullname = fields.String(required=True)
    mobile_number = fields.String(required=True)
    birth_date = fields.DateTime()
    email = fields.String(required=True)
    status = fields.Boolean(required=True)
    creation_date = fields.DateTime(required=True)
    modified_date = fields.DateTime()
    addresses = fields.Nested(addresses_schema)


# Init Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)
