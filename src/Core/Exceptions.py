import traceback

from flask import Flask, jsonify


def register_exceptions(app: Flask):
    @app.errorhandler(Exception)
    def handle_invalid_usage(error: Exception):
        data = dict(message=error.__str__())

        if 'validation' in error.__dict__:
            data['validation'] = error.__dict__.get('validation')
        else:
            data['validation'] = dict()

        data['traceback'] = traceback.format_exc()
        response = jsonify(data)

        if 'status_code' in error.__dict__:
            response.status_code = error.__dict__.get('status_code')
        else:
            response.status_code = 500

        return response
