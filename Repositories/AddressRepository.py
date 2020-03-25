from Models.Domain.Address import db, Address


def add(address):
    db.session.add(address)


def delete(address):
    db.session.delete(address)


def get_by_id(id):
    return Address.query.get(id)


def commit():
    db.session.commit()


def rollback():
    db.session.rollback()
