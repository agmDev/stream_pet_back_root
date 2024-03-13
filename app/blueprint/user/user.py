from flask import Blueprint, jsonify, abort, request
from app.models.user_model import User
from app.models import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/<string:email_input>', methods=['GET'])
def get_user(email_input):
    user = User.query.filter_by(email = email_input).first()
    if user == None:
        abort(404)
    return jsonify(user.email)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(data['email'])

    if db.session.query(User.id).filter_by(email = data['email']).first() is not None:
        return ('user already exist', 409)
    db.session.add(user)
    db.session.commit()
    return ('', 204)