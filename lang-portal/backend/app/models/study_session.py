"""StudySession and WordReviewItem models."""
from app import db

class StudySession(db.Model):
    """StudySession model."""
    __tablename__ = 'study_sessions'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    study_activity_id = db.Column(
        db.Integer,
        db.ForeignKey('study_activities.id'),
        nullable=False
    )
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    completed_at = db.Column(db.DateTime, nullable=True)

    # Relationships
    group = db.relationship('Group', back_populates='study_sessions')
    study_activity = db.relationship('StudyActivity', back_populates='study_sessions')
    word_reviews = db.relationship(
        'WordReviewItem',
        back_populates='study_session',
        lazy='dynamic'
    )

    def __repr__(self):
        return f'<StudySession {self.id}>'


class WordReviewItem(db.Model):
    """WordReviewItem model."""
    __tablename__ = 'word_review_items'

    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'), nullable=False)
    study_session_id = db.Column(
        db.Integer,
        db.ForeignKey('study_sessions.id'),
        nullable=False
    )
    correct = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Relationships
    word = db.relationship('Word', back_populates='word_reviews')
    study_session = db.relationship('StudySession', back_populates='word_reviews')

    def __repr__(self):
        return f'<WordReviewItem {self.id}>'
