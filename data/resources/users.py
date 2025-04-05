from flask import jsonify
from flask_restful import Resource, abort, reqparse
from data import db_session
from data.users import User

user_parser = reqparse.RequestParser()
user_parser.add_argument('name', required=True)
user_parser.add_argument('surname', required=True)
user_parser.add_argument('age', required=True, type=int)
user_parser.add_argument('position', required=True)
user_parser.add_argument('speciality', required=True)
user_parser.add_argument('address', required=True)
user_parser.add_argument('email', required=True)
user_parser.add_argument('hashed_password', required=True)


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UserResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(only=('name', 'surname', 'age', 'address',
                                                   'email', 'position', 'speciality',
                                                   'hashed_password'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(only=('name', 'surname', 'age', 'address',
                                                     'email', 'position', 'speciality',
                                                     'hashed_password')) for item in users]})

    def post(self):
        args = user_parser.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            address=args['address'],
            email=args['email'],
            position=args['position'],
            speciality=args['speciality'],
        )
        user.set_password(args["hashed_password"])
        try:
            session.add(user)
            session.commit()
        except Exception as e:
            if (str(e.orig) == "UNIQUE constraint failed: users.email"):
                return jsonify(f"Пользователь с {user.email} уже существует")
        return jsonify({'id': user.id})
