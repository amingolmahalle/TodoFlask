from Domain.Entity.Common.SharedModel import db
from datetime import datetime


class Address(db.Model):
    __tablename__ = "address"
    id = db.Column(db.Integer,
                   primary_key=True)
    country_name = db.Column(db.String(50),
                             nullable=False)
    city_name = db.Column(db.String(50),
                          nullable=False)
    postal_code = db.Column(db.String(200),
                            nullable=False)
    more_address = db.Column(db.String(100))
    creation_date = db.Column(db.DateTime,
                              nullable=False,
                              default=datetime.utcnow)
    modified_date = db.Column(db.DateTime,
                              nullable=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('user.id', ondelete='CASCADE'),
                        nullable=False)

    def __init__(self,
                 country_name,
                 city_name,
                 postal_code,
                 more_address,
                 id=None,
                 user_id=None,
                 creation_date=None,
                 modified_date=None):
        self.id = id
        self.user_id = user_id
        self.country_name = country_name
        self.city_name = city_name
        self.postal_code = postal_code
        self.more_address = more_address
        self.creation_date = creation_date
        self.modified_date = modified_date
