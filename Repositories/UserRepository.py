from Models.Domain.User import db, User
from Models.Domain.Address import Address
from Data.DataProviders.SqlDataProvider import SqlDataProvider


def add(user):
    db.session.add(user)


def add_range(users):
    db.session.add(users)


def delete(user):
    db.session.delete(user)


def get_by_id_with_query(userId):
    command = f'''SELECT
                        u.id AS user_id,
                        u.code,
                        u.fullname,
                        u.mobile_number,
                        u.birth_date,
                        u.email,
                        u.status,
                        u.creation_date,
                        u.modified_date,
                        a.id AS address_id,
                        a.country_name,
                        a.city_name,
                        a.postal_code,
                        a.more_address
                 FROM
                        user AS u INNER JOIN 
                        address as a ON u.id = a.user_id
                 WHERE
                        u.id ={userId}           
              '''

    return SqlDataProvider().execute_query_command(command)


def get_all_by_pagination(page, per_page):
    return User.query \
        .order_by(User.creation_date.desc()) \
        .paginate(page, per_page, error_out=False) \
        .items


def get_all():
    return User.query.join(Address).all()
    # return db.session.query(User, Address).join(Address).all()


def get_by_id(id):
    return User.query.get(id)


def get_by_mobile(mobile):
    return User.query.filter_by(mobile_number=mobile).one()


def commit():
    db.session.commit()


def rollback():
    db.session.rollback()
