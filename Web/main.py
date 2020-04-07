from flask import Flask
from flask_cors import CORS
from Domain.Entity.Common.SharedModel import db
from Domain.Schema.SharedSchema import ma
from Web.RequestWrapper.Middleware import Middleware
from Web.program import program
from Web.Controllers.UserController import app as user_controller
import Web.Configs.ArgumentsConfig as argumentsConfig

import os

if __name__ == '__main__':
    application = Flask(__name__)
    CORS(application)
    application.wsgi_app = Middleware(application.wsgi_app)

    settings = program.load_configs()

    application.config["SECRET_KEY"] = settings["secretKey"]
    application.config["SQLALCHEMY_DATABASE_URI"] = settings["dbConnection"]
    application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    application.config["SQLALCHEMY_ECHO"] = True
    port = settings["port"]

    swagger_url = settings['swaggerUrl']
    swagger_api_url = settings['swaggerApiUrl']

    db.init_app(application)
    ma.init_app(application)

    with application.app_context():
        db.create_all()

    user_controller.register_blueprint(application, url_prefix=f'/api/v1/user')

    args = argumentsConfig.get_args()
    PORT = int(os.environ.get('PORT', port))

    if args.debug:
        application.run(host='0.0.0.0', port=PORT, debug=True)
    else:
        application.run(host='0.0.0.0', port=PORT, debug=False)
