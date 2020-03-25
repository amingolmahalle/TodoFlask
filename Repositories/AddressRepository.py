from Models.Domain.Address import db, Address


def add(addresses):
    db.session.add_all(addresses)


def delete(address):
    db.session.delete(address)


def get_by_id(id):
    return Address.query.get(id)


def commit():
    db.session.commit()


def rollback():
    db.session.rollback()
