from flask import Blueprint

sub = Blueprint('hello_api', __name__, url_prefix='/api/people')


@sub.route('/getAll')
def get_all():
    return 'show get all people list'
