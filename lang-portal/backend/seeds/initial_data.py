"""Initial seed data for the database."""
from app import db
from app.models.word import Word
from app.models.group import Group
from app.models.study_activity import StudyActivity

def seed_data():
    """Seed initial data."""
    # Create groups
    basic_greetings = Group(
        name='Basic Greetings',
        description='Essential French greetings for beginners'
    )
    numbers = Group(
        name='Numbers',
        description='Basic French numbers from 1-20'
    )
    
    db.session.add_all([basic_greetings, numbers])
    db.session.commit()
    
    # Create words
    greetings_words = [
        Word(
            french='Bonjour',
            english='Hello',
            parts={'part_of_speech': 'interjection'}
        ),
        Word(
            french='Au revoir',
            english='Goodbye',
            parts={'part_of_speech': 'interjection'}
        ),
        Word(
            french='S\'il vous plaît',
            english='Please',
            parts={'part_of_speech': 'interjection'}
        ),
        Word(
            french='Merci',
            english='Thank you',
            parts={'part_of_speech': 'interjection'}
        )
    ]
    
    numbers_words = [
        Word(
            french='Un',
            english='One',
            parts={'part_of_speech': 'number'}
        ),
        Word(
            french='Deux',
            english='Two',
            parts={'part_of_speech': 'number'}
        ),
        Word(
            french='Trois',
            english='Three',
            parts={'part_of_speech': 'number'}
        )
    ]
    
    # Add words to groups
    basic_greetings.words.extend(greetings_words)
    numbers.words.extend(numbers_words)
    
    db.session.add_all(greetings_words + numbers_words)
    db.session.commit()
    
    # Create study activities
    activities = [
        StudyActivity(
            name='Vocabulary Quiz',
            description='Test your knowledge of French words',
            group=basic_greetings
        ),
        StudyActivity(
            name='Number Practice',
            description='Practice French numbers',
            group=numbers
        )
    ]
    
    db.session.add_all(activities)
    db.session.commit()
