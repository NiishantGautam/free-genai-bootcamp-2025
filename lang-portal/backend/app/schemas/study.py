"""Study schemas."""
from marshmallow import Schema, fields

class StudyActivitySchema(Schema):
    """StudyActivity schema."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    thumbnail_url = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    group_id = fields.Int(required=True)
    
    class Meta:
        ordered = True

class WordReviewItemSchema(Schema):
    """WordReviewItem schema."""
    id = fields.Int(dump_only=True)
    word_id = fields.Int(required=True)
    study_session_id = fields.Int(required=True)
    correct = fields.Bool(required=True)
    created_at = fields.DateTime(dump_only=True)
    
    # Nested fields
    word = fields.Nested('WordSchema', exclude=('groups',))
    
    class Meta:
        ordered = True

class StudySessionSchema(Schema):
    """StudySession schema."""
    id = fields.Int(dump_only=True)
    group_id = fields.Int(required=True)
    study_activity_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    completed_at = fields.DateTime()
    
    # Nested fields
    group = fields.Nested('GroupSchema', exclude=('words',))
    study_activity = fields.Nested(StudyActivitySchema)
    word_reviews = fields.Nested(WordReviewItemSchema, many=True)
    
    class Meta:
        ordered = True
