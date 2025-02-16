"""Dashboard views."""
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy import func

from app.models.study_session import StudySession, WordReviewItem
from app.models.word import Word
from app.schemas.study import StudySessionSchema

blp = Blueprint(
    'dashboard',
    __name__,
    url_prefix='/api/dashboard',
    description='Dashboard operations'
)

@blp.route('/last_study_session')
class LastStudySession(MethodView):
    
    @blp.response(200, StudySessionSchema)
    def get(self):
        """Get last study session."""
        return StudySession.query.order_by(
            StudySession.created_at.desc()
        ).first_or_404()

@blp.route('/study_progress')
class StudyProgress(MethodView):
    
    @blp.response(200)
    def get(self):
        """Get study progress."""
        total_words = Word.query.count()
        studied_words = db.session.query(
            func.count(func.distinct(WordReviewItem.word_id))
        ).scalar()
        
        return {
            'total_words_studied': studied_words,
            'total_available_words': total_words
        }

@blp.route('/quick_stats')
class QuickStats(MethodView):
    
    @blp.response(200)
    def get(self):
        """Get quick stats."""
        # Calculate success rate
        reviews = WordReviewItem.query
        total_reviews = reviews.count()
        correct_reviews = reviews.filter_by(correct=True).count()
        success_rate = (
            (correct_reviews / total_reviews * 100)
            if total_reviews > 0
            else 0
        )
        
        # Get total study sessions
        total_sessions = StudySession.query.count()
        
        # Get total active groups (groups with study sessions in last 30 days)
        active_groups = db.session.query(
            func.count(func.distinct(StudySession.group_id))
        ).filter(
            StudySession.created_at >= func.now() - func.interval('30 days')
        ).scalar()
        
        # Calculate study streak (consecutive days with study sessions)
        streak_query = """
            WITH RECURSIVE dates AS (
                SELECT date_trunc('day', now()) as day
                UNION ALL
                SELECT day - interval '1 day'
                FROM dates
                WHERE EXISTS (
                    SELECT 1
                    FROM study_sessions
                    WHERE date_trunc('day', created_at) = day - interval '1 day'
                )
                AND day > date_trunc('day', now()) - interval '30 days'
            )
            SELECT count(*)
            FROM dates
        """
        study_streak = db.session.execute(streak_query).scalar()
        
        return {
            'success_rate': round(success_rate, 1),
            'total_study_sessions': total_sessions,
            'total_active_groups': active_groups,
            'study_streak': study_streak
        }
