from dataclasses import fields

from marshmallow import Schema, validate


class UserRegResponse(Schema):

    message = fields.Str()
