"""Group schemas."""
from marshmallow import Schema, fields

class GroupSchema(Schema):
    """Group schema."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    
    # Nested fields
    words = fields.Nested('WordSchema', many=True, exclude=('groups',))
    
    class Meta:
        ordered = True
