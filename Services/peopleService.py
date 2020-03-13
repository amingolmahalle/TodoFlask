from flask import Blueprint

sub = Blueprint('hello_api', __name__, url_prefix='/api/people')


@sub.route('/getAll')
def get_all():
    return 'show get all people list'


@sub.route('/getById/<int:id>')
def get_by_id():
    return 'show get all people list'


@sub.route('/add', methods=['POST'])
def add():
    return 'show get all people list'


@sub.route('/edit', methods=['PUT'])
def edit():
    return 'show get all people list'


@sub.route('/delete/<int:id>', methods=['DELETE'])
def delete_by_id():
    return 'show get all people list'
