from werkzeug.wrappers import Request


class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        gateway = request.headers.get('request-gateway', None)

        if not request.path.__contains__('/swagger/') and (gateway is None or not gateway):
            raise Exception('empty header detected [request-gateway]')

        return self.app(environ, start_response)
