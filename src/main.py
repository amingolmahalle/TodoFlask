from flask import Flask
from flask_cors import CORS
from Domain.Entity.Common.SharedModel import db
from Domain.Schema.SharedSchema import ma
from Web.RequestWrapper.Middleware import Middleware
from Web.Controllers.UserController import app as user_controller
from Web.Configs.AppSettings import SECRET_KEY, APP_PORT, DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME, DB_PORT
from Web.Configs.ArgumentsConfig import get_args
import os

if __name__ == '__main__':
    application = Flask(__name__)
    CORS(application)
    application.wsgi_app = Middleware(application.wsgi_app)

    application.config["SECRET_KEY"] = SECRET_KEY
    application.config[
        "SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    application.config["SQLALCHEMY_ECHO"] = True
    port = APP_PORT

    db.init_app(application)
    ma.init_app(application)

    with application.app_context():
        db.create_all()

    user_controller.register_blueprint(application, url_prefix=f'/api/v1/user')

    args = get_args()
    PORT = int(os.environ.get('PORT', port))

    if args.debug:
        application.run(host='0.0.0.0', port=PORT, debug=True)
    else:
        application.run(host='0.0.0.0', port=PORT, debug=False)
