from Domain.Schema.SharedSchema import ma, fields
from Domain.Entity.UserAggregate.Address import Address


# Address Schema
class AddressSchema(ma.Schema):
    class Meta:
        model = Address
    # id = fields.Integer(required=True)
    country_name = fields.String()
    city_name = fields.String()
    postal_code = fields.String()
    more_address = fields.String()
    creation_date = fields.DateTime()
    modified_date = fields.DateTime()
    # user_id = fields.Integer()
    include_fk = True


# Init Schema
addresses_schema = AddressSchema(many=True)
