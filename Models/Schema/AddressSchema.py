from Models.Schema.SharedSchema import ma, fields
from Models.Domain.Address import Address


# Address Schema
class AddressSchema(ma.Schema):
    class Meta:
        model = Address
    id = fields.Integer(required=True)
    country_name = fields.String(required=True)
    city_name = fields.String(required=True)
    postal_code = fields.String(required=True)
    more_address = fields.String()
    creation_date = fields.DateTime(required=True)
    modified_date = fields.DateTime()
    user_id = fields.Integer(required=True)
    include_fk = True


# Init Schema
addresses_schema = AddressSchema(many=True)
