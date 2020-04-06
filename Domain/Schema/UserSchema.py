from Domain.Schema.SharedSchema import ma, fields
from Domain.Entity.UserAggregate.User import User
from Domain.Schema.AddressSchema import addresses_schema


# User Schema
class UserSchema(ma.Schema):
    class Meta:
        model = User
    id = fields.Integer(required=True)
    code = fields.String()
    fullname = fields.String()
    mobile_number = fields.String()
    birth_date = fields.DateTime()
    email = fields.String()
    status = fields.Boolean()
    creation_date = fields.DateTime()
    modified_date = fields.DateTime()
    addresses = fields.Nested(addresses_schema)


# Init Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)
