from marshmallow import Schema, fields


class UserLoginResponse(Schema):

    message = fields.Str()
    name = fields.Str()
    token = fields.Str()