"""StudyActivity model."""
from app import db

class StudyActivity(db.Model):
    """StudyActivity model."""
    __tablename__ = 'study_activities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    thumbnail_url = db.Column(db.String(512), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)

    # Relationships
    group = db.relationship('Group', back_populates='study_activities')
    study_sessions = db.relationship(
        'StudySession',
        back_populates='study_activity',
        lazy='dynamic'
    )

    def __repr__(self):
        return f'<StudyActivity {self.name}>'
