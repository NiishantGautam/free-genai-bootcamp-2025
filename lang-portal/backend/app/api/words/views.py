"""Word views."""
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.models.word import Word
from app.schemas.word import WordSchema

blp = Blueprint(
    'words',
    __name__,
    url_prefix='/api/words',
    description='Operations on words'
)

@blp.route('/')
class Words(MethodView):
    
    @blp.response(200, WordSchema(many=True))
    @blp.paginate()
    def get(self):
        """List words."""
        return Word.query

    @blp.arguments(WordSchema)
    @blp.response(201, WordSchema)
    def post(self, word_data):
        """Add a word."""
        word = Word(**word_data)
        
        try:
            db.session.add(word)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
            
        return word

@blp.route('/<int:word_id>')
class WordById(MethodView):
    
    @blp.response(200, WordSchema)
    def get(self, word_id):
        """Get word by ID."""
        word = Word.query.get_or_404(word_id)
        return word

    @blp.arguments(WordSchema)
    @blp.response(200, WordSchema)
    def put(self, word_data, word_id):
        """Update word."""
        word = Word.query.get_or_404(word_id)
        
        for key, value in word_data.items():
            setattr(word, key, value)
            
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
            
        return word

    @blp.response(204)
    def delete(self, word_id):
        """Delete word."""
        word = Word.query.get_or_404(word_id)
        
        try:
            db.session.delete(word)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
