from flask import Flask
from flask_login import LoginManager

from data import db_session
from data.users import User

from blueprints.users_bp import bp as users_bp
from blueprints.jobs_bp import bp as jobs_bp
from blueprints.jobs_api_bp import bp as jobs_api_bp
from blueprints.errors_bp import bp as errors_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


app.register_blueprint(users_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(jobs_api_bp)
app.register_blueprint(errors_bp)


def main():
    db_session.global_init("db/mars_explorer_.db")
    app.run(debug=True)


if __name__ == '__main__':
    main()
