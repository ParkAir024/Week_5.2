from flask.views import MethodView
from flask_smorest import abort
from uuid import uuid4

from schemas import GamesSchema
from db import games, users
from . import bp

@bp.route('/<games_id>')
class Games(MethodView):

    @bp.response(200, GamesSchema)
    def get(self, games_id):
        game = games.get(games_id)
        if game:
            return game
        abort(400, message='Invalid Game')

    @bp.arguments(GamesSchema)
    @bp.response(201, GamesSchema)
    def post(self, post_data):
        user_id = post_data['user_id']
        if user_id in users:
            game_id = uuid4()
            games[game_id] = post_data
            return {'message': "Game Created", 'game_id': str(game_id)}, 201
        abort(401, message='Invalid User')

    @bp.arguments(GamesSchema)
    @bp.response(202, GamesSchema)
    def put(self, post_data, games_id):
        game = games.get(games_id)
        if game:
            if post_data['user_id'] == game['user_id']:
                game['body'] = post_data['body']
                return {'message': 'Game Updated'}, 202
            abort(401, message='Unauthorized')
        abort(400, message='Invalid Game')

    def delete(self, games_id):
        game = games.get(games_id)
        if game:
            del games[games_id]
            return {"message": "Game Deleted"}, 202
        abort(400, message='Invalid Game')

@bp.route('/')
class GamesList(MethodView):

    @bp.response(200, GamesSchema(many=True))
    def get(self):
        return list(games.values())

    @bp.arguments(GamesSchema)
    @bp.response(201, GamesSchema)
    def post(self, post_data):
        user_id = post_data['user_id']
        if user_id in users:
            game_id = uuid4()
            games[game_id] = post_data
            return {'message': "Game Created", 'game_id': str(game_id)}, 201
        abort(401, message='Invalid User')
