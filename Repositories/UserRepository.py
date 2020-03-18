from Models.User import db, User


def add(user):
    db.session.add(user)


def delete(user):
    db.session.delete(user)


def get_all():
    return User.query.all()


def get_by_id(id):
    return User.query.get(id)


def get_by_mobile(mobile):
    return User.query.filter_by(mobile_number=mobile).first()


def commit():
    db.session.commit()


def rollback():
    db.session.rollback()
