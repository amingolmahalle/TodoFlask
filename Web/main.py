from flask import Flask
from flask_cors import CORS
import Controllers.UserController as userController
from Models.ConfigModel import db, ma
from Web.RequestWrapper.Middleware import Middleware
from Web.program import program
if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app)
    app.wsgi_app = Middleware(app.wsgi_app)

    settings = program.load_configs()

    app.config["SECRET_KEY"] = settings["secretKey"]
    app.config["SQLALCHEMY_DATABASE_URI"] = settings["databaseConnection"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(userController.sub)

    app.run(host='0.0.0.0', port=5050, debug=True)
