"""Study views."""
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.models.study_activity import StudyActivity
from app.models.study_session import StudySession, WordReviewItem
from app.schemas.study import (
    StudyActivitySchema,
    StudySessionSchema,
    WordReviewItemSchema
)

blp = Blueprint(
    'study',
    __name__,
    url_prefix='/api/study-activities',
    description='Operations on study activities'
)

@blp.route('/')
class StudyActivities(MethodView):
    
    @blp.response(200, StudyActivitySchema(many=True))
    @blp.paginate()
    def get(self):
        """List study activities."""
        return StudyActivity.query

    @blp.arguments(StudyActivitySchema)
    @blp.response(201, StudyActivitySchema)
    def post(self, activity_data):
        """Create study activity."""
        activity = StudyActivity(**activity_data)
        
        try:
            db.session.add(activity)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
            
        return activity

@blp.route('/<int:activity_id>')
class StudyActivityById(MethodView):
    
    @blp.response(200, StudyActivitySchema)
    def get(self, activity_id):
        """Get study activity by ID."""
        activity = StudyActivity.query.get_or_404(activity_id)
        return activity

@blp.route('/<int:activity_id>/study-sessions')
class StudyActivitySessions(MethodView):
    
    @blp.response(200, StudySessionSchema(many=True))
    @blp.paginate()
    def get(self, activity_id):
        """Get study sessions for activity."""
        StudyActivity.query.get_or_404(activity_id)  # Ensure activity exists
        return StudySession.query.filter_by(study_activity_id=activity_id)

    @blp.arguments(StudySessionSchema)
    @blp.response(201, StudySessionSchema)
    def post(self, session_data, activity_id):
        """Create study session for activity."""
        session_data['study_activity_id'] = activity_id
        session = StudySession(**session_data)
        
        try:
            db.session.add(session)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
            
        return session

@blp.route('/<int:activity_id>/study-sessions/<int:session_id>/reviews')
class StudySessionReviews(MethodView):
    
    @blp.response(200, WordReviewItemSchema(many=True))
    @blp.paginate()
    def get(self, activity_id, session_id):
        """Get word reviews for session."""
        session = StudySession.query.get_or_404(session_id)
        if session.study_activity_id != activity_id:
            abort(404, message="Study session not found for this activity")
        return session.word_reviews

    @blp.arguments(WordReviewItemSchema)
    @blp.response(201, WordReviewItemSchema)
    def post(self, review_data, activity_id, session_id):
        """Create word review for session."""
        session = StudySession.query.get_or_404(session_id)
        if session.study_activity_id != activity_id:
            abort(404, message="Study session not found for this activity")
            
        review_data['study_session_id'] = session_id
        review = WordReviewItem(**review_data)
        
        try:
            db.session.add(review)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
            
        return review
