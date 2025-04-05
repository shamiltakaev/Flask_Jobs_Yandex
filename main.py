from flask import Flask
from flask_login import LoginManager
from flask_restful import Api

from data import db_session
from data.users import User
import data.jobs_resources as jobs_resources
import data.user_resources as user_resources

from blueprints.users_bp import bp as users_bp
from blueprints.jobs_bp import bp as jobs_bp
from blueprints.errors_bp import bp as errors_bp


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


api = Api(app)

api.add_resource(jobs_resources.JobsListResource, '/api/v2/jobs')
api.add_resource(jobs_resources.JobsResource, '/api/v2/jobs/<int:job_id>')

api.add_resource(user_resources.UsersListResource, '/api/v2/users')
api.add_resource(user_resources.UserResource, '/api/v2/users/<int:user_id>')


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


app.register_blueprint(users_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(errors_bp)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer_.db")
    app.run(debug=True)
