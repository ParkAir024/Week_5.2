from flask.views import MethodView
from flask import request
from uuid import uuid4

from . import bp
from db import users

from schemas import UserSchema

@bp.route('/user/<user_id>')
class UserView(MethodView):
    @bp.response(200, UserSchema(many=True))
    def get(self):
        return { 'users': list(users.values()) }, 200

    @bp.response(200, UserSchema)
    def get_user(self, user_id):
        try:
            return { 'user': users[user_id] } 
        except KeyError:
            return {'message': 'Invalid user'}, 400

    @bp.arguments(UserSchema)
    def post(self, user_data):
        user_id = uuid4()
        users[user_id] = user_data
        return { 'message': f'{user_data["username"]} created' }, 201

    def put(self, user_id):
        try:
            user = users[user_id]
            user |= user_data
            return { 'message': f'{user["username"]} updated'}, 202
        except KeyError:
            return {'message': "Invalid User"}, 400

    def delete(self, user_id):
        try:
            del users[user_id]
            return { 'message': f'User Deleted' }, 202
        except KeyError:
            return {'message': "Invalid username"}, 400
                        
@bp.route('/user')
class UserList(MethodView):

    @bp.response(200, UserSchema(many=True))
    def get(self):
        return list(users.values())
  
    @bp.arguments(UserSchema)
    def post(self, user_data):
        users[uuid4()] = user_data
        return { 'message' : f'{user_data["username"]} created' }, 201
