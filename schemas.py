from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Str(dump_only = True)
    email = fields.Str(required = True)
    username = fields.Str(required = True)
    first_name = fields.Str()
    last_name = fields.Str()

class GamesSchema(Schema):
    id = fields.Str(dump_only = True)
    title = fields.Str(required=True)
    system = fields.Str(required=True)
    release_year = fields.Str(required=True)
    user_id = fields.Str(required=True)