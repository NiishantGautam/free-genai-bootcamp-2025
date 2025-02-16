"""Word model."""
from app import db

class Word(db.Model):
    """Word model."""
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True)
    french = db.Column(db.String(255), nullable=False)
    english = db.Column(db.String(255), nullable=False)
    parts = db.Column(db.JSON, nullable=True)

    # Relationships
    groups = db.relationship(
        'Group',
        secondary='word_groups',
        back_populates='words'
    )
    
    word_reviews = db.relationship(
        'WordReviewItem',
        back_populates='word',
        lazy='dynamic'
    )

    def __repr__(self):
        return f'<Word {self.french}>'
