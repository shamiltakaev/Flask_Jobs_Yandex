from flask import make_response, Blueprint, jsonify

bp = Blueprint("errors", __name__)

@bp.app_errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@bp.app_errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)
