from werkzeug.wrappers import Request  # Response, ResponseStream


class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        client_id = request.headers.get('client-id', None)

        if request.path != '/api/docs/' and (client_id is None or not client_id):
            raise Exception('empty header detected [client-id]')

        return self.app(environ, start_response)
