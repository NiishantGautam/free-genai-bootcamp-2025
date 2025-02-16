"""Word schemas."""
from marshmallow import Schema, fields

class WordSchema(Schema):
    """Word schema."""
    id = fields.Int(dump_only=True)
    french = fields.Str(required=True)
    english = fields.Str(required=True)
    parts = fields.Dict(keys=fields.Str(), values=fields.Raw(), required=False)
    
    # Nested fields
    groups = fields.Nested('GroupSchema', many=True, exclude=('words',))
    
    class Meta:
        ordered = True
