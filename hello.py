from flask import Blueprint

sub = Blueprint('hello_api', __name__, url_prefix='/api/hello')


@sub.route('/name')
def say_hello():
    return 'hello world'
