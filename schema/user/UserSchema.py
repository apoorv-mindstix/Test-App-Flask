from marshmallow import Schema, fields, validate

# for parsing the request body sent by client using the register endpoint
class RegisterSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6))
    role = fields.String(
        required=False, validate=validate.OneOf(["admin", "doctor", "member"])
    )

# for parsing the request body sent by client using the login endpoint.
class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)