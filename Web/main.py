from flask import Flask
from flask_cors import CORS
import Web.Controllers.UserController as UserController
from Domain.Entity.Common.SharedModel import db
from Domain.Schema.SharedSchema import ma
from Web.RequestWrapper.Middleware import Middleware
from Web.program import program
import Web.Configs.ArgumentsConfig as argumentsConfig
import os

if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app)
    app.wsgi_app = Middleware(app.wsgi_app)

    settings = program.load_configs()

    app.config["SECRET_KEY"] = settings["secretKey"]
    app.config["SQLALCHEMY_DATABASE_URI"] = settings["dbConnection"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True
    port = settings["port"]

    swagger_url = settings['swaggerUrl']
    swagger_api_url = settings['swaggerApiUrl']

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(UserController.sub)

    args = argumentsConfig.get_args()
    PORT = int(os.environ.get('PORT', port))

    if args.debug:
        app.run(host='0.0.0.0', port=PORT, debug=True)
    else:
        app.run(host='0.0.0.0', port=PORT, debug=False)
