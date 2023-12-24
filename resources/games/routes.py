from flask.views import MethodView
from flask import request
from uuid import uuid4

from schemas import GamesSchema
from db import games, users
from . import bp

@bp.route('/<games_id>')
class Games(MethodView):
    @bp.response(200, GamesSchema(many=True))
    def get(self):
        return {'posts': list(games.values())}

    @bp.response(200, GamesSchema)
    def post(self):
        user_id = post_data['user_id']
        if user_id in users:
            games[uuid4()] = post_data
            return {'message': "Post Created"}, 201
        return {'message': "Invalid User"}, 401

    @bp.arguments(GamesSchema)
    def put(self, post_id):
        try:
            post = games[post_id]
            if post_data['user_id'] == post['user_id']:
                post['body'] = post_data['body']
                return {'message': 'Post Updated'}, 202
            return {'message': "Unauthorized"}, 401
        except KeyError:
            return {'message': "Invalid Post"}, 400

    def delete(self, post_id):
        try:
            del games[post_id]
            return {"message": "Post Deleted"}, 202
        except KeyError:
            return {'message': "Invalid Post"}, 400

class PostList(MethodView):
    @bp.response(200, GamesSchema(many=True))
    def get(self):
        return list(posts.values())

    @bp.arguments(GamesSchema)
    def post(self, post_data):
        user_id = post_data['user_id']
        if user_id in users:
            posts[uuid4()] = post_data
            return {'message': "Post Created"}, 201
        return {'message': "Invalid User"}, 401