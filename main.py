from flask import Flask
import Services.UserService as userServices
from models import db, ma

if __name__ == '__main__':
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://develop:Aa123456!@localhost:3306/my_db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(userServices.sub)
    app.run(host='0.0.0.0', port=5050, debug=True)
