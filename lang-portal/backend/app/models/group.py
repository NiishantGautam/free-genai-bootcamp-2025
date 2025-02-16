"""Group model."""
from app import db

# Junction table for many-to-many relationship between words and groups
word_groups = db.Table(
    'word_groups',
    db.Column('word_id', db.Integer, db.ForeignKey('words.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
)

class Group(db.Model):
    """Group model."""
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )

    # Relationships
    words = db.relationship(
        'Word',
        secondary=word_groups,
        back_populates='groups'
    )
    study_sessions = db.relationship(
        'StudySession',
        back_populates='group',
        lazy='dynamic'
    )
    study_activities = db.relationship(
        'StudyActivity',
        back_populates='group',
        lazy='dynamic'
    )

    def __repr__(self):
        return f'<Group {self.name}>'
