# Backend Server Technical Specs

## Business Goals:
A language learning school wants to build a prototype of learning portal which will act as three things:
Inventory of possible vocabulary that can be learned
Act as a  Learning record store (LRS), providing correct and wrong score on practice vocabulary
A unified launchpad to launch different learning apps


## Technical Requirements:

- The backend will be built using Python and Flask.
- The database will be built using Flask-SQLAlchemy.
- The Backend will be deployed using Docker.
- The API will be built using Flask
- The API will always return JSON

## Database Schema:
The database will have the following tables:
- words - Stored Vocabulary words
   - id integer
   - French string
   - English string
   - parts - json
- word_groups - join table for words and groups, many to many relationship
  - id integer
  - word_id integer
  - group_id integer
- groups - thematic groups of words
  - id integer
  - name string
- study_sessions - records of study sessions groouping word_review_items  
  - id integer
  - group_id integer
  - created_at datetime
  - study_activity_id integer
- study_activities - a specific study activity, linking study sessions to group
 - id integer
 - study_session_id integer
 - group_id integer
 - created_at datetime
- word_reviews_items - a record of word practice, determining if the word was correct or not.
  word_id integer
  - study_session_id integer
  - correct boolean
  - created_at datetime

## API Endpoints:


- GET /api/dashboard/last_study_session
- GET /api/dashboard/study_progress
- GET /api/dashboard/quick_stats
- POST /api/study-activities/
   - required params: group_id, study_activity_id
- GET /api/words
   - pagination with 100 items per page
- GET /api/words/:id
- GET /api/groups
  - pagination with 10 items per page
- GET /api/groups/:id
- GET /api/groups/:id/words
- GET /api/groups/:id/study_sessions
- GET /api/study_sessions
  - pagination with 10 items per page
- GET /api/study_sessions/:id
- GET /api/study_sessions/:id/words
- POST /api/study_sessions/:id/reset_history
- POST /api/study_sessions/:id/full_reset
- POST /api/study_sessions/:id/words/:word_id/review
  - required params: correct