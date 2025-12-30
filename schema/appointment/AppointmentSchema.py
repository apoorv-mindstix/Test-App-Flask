from marshmallow import Schema, fields

class AppointmentSchema(Schema):
    doc_id = fields.Int(load_only=True)
    date = fields.Str(required=True)
    start_time = fields.Str(required=True)
    end_time = fields.Str(required=True)