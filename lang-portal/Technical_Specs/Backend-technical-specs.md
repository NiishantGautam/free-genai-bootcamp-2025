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




### Dashboard Endpoints

#### GET /api/dashboard/last_study_session
Returns information about the user's most recent study session.

Response:
```json
{
  "id": "uuid",
  "started_at": "2025-02-13T21:00:00Z",
  "completed_at": "2025-02-13T21:30:00Z",
  "group_id": "456",
  "group_name": "Basic Greetings"
  

}
```

#### GET /api/dashboard/study_progress
Returns the user's overall study progress statistics.
Please note that the frontend will determine progress bar based on the 
total words studied and total available words 

Response:
```json
{
  "total_words_studied": 3,
  "total_available_words": 100,
}
```

#### GET /api/dashboard/quick_stats
Returns quick overview of statistics
Response:
```json
{
 "success_rate": 75,
 "total_study_sessions": 5,
 "total_active_groups": 3,
 "study_streak": 4
}
```

### Study Activities Endpoints

#### GET /api/study-activities/:id
Returns details of a specific study activity.

Response:
```json
{
  "id": "1",
  "name": "Vocabulary Quiz",
  "description": "Test your knowledge of basic words",
  "thumbnail_url": "https://example.com/thumbnail.png"
}
```

#### GET /api/study-activities/:id/study_sessions
Returns all study sessions for a specific activity.

Response:
```json
{
  "sessions": [
    {
      "id": "123",
      "activity_name": "Vocabulary Quiz",
      "group_name": "Basic Greetings",
      "started_at": "2025-02-13T20:00:00Z",
      "completed_at": "2025-02-13T20:15:00Z",
      "score": 85,
      "words_reviewed": 20
    }
  ],
  "pagination": {
    "total_items": 50,
    "per_page": 100,
    "current_page": 1,
    "item_per_page": 20
  }
}
```

#### POST /api/study-activities
Create a new study activity.

Request:
```json
{
  "group_id": "uuid",
  "study_activity_id": "uuid"
}
```

Response:
```json
{
  "id": "uuid",
  "created_at": "2025-02-13T21:07:53Z",
  "status": "created",
  "group_id": "uuid",
  "study_activity_id": "uuid"
}
```

### Words Endpoints

#### GET /api/words
Returns a paginated list of words.

Response:
```json
{
  "words": [
    {
      "id": "uuid",
      "word": "example",
      "definition": "a representative form or pattern",
      "part_of_speech": "noun",
      "difficulty_level": "beginner",
      "examples": ["This is an example sentence."]
    }
  ],
  "pagination": {
    "total": 1000,
    "per_page": 100,
    "current_page": 1,
    "total_pages": 10
  }
}
```

#### GET /api/words/:id
Returns details of a specific word.

Response:
```json
{
  "id": "uuid",
  "word": "example",
  "definition": "a representative form or pattern",
  "part_of_speech": "noun",
  "difficulty_level": "beginner",
  "examples": ["This is an example sentence."],
  "synonyms": ["sample", "specimen"],
  "antonyms": [],
  "study_progress": {
    "times_reviewed": 10,
    "accuracy": 0.8,
    "last_reviewed": "2025-02-13T20:00:00Z"
  }
}
```

### Groups Endpoints

#### GET /api/groups
Returns a paginated list of word groups.

Response:
```json
{
  "groups": [
    {
      "id": "uuid",
      "name": "Basic Vocabulary",
      "description": "Essential words for beginners",
      "word_count": 100,
      "difficulty_level": "beginner",
      "created_at": "2025-02-01T00:00:00Z"
    }
  ],
  "pagination": {
    "total": 50,
    "per_page": 10,
    "current_page": 1,
    "total_pages": 5
  }
}
```

#### GET /api/groups/:id
Returns details of a specific group.

Response:
```json
{
  "id": "uuid",
  "name": "Basic Vocabulary",
  "description": "Essential words for beginners",
  "word_count": 100,
  "difficulty_level": "beginner",
  "created_at": "2025-02-01T00:00:00Z",
  "last_studied": "2025-02-13T20:00:00Z",
  "progress": {
    "words_mastered": 75,
    "average_accuracy": 0.85
  }
}
```

#### GET /api/groups/:id/words
Returns words belonging to a specific group.

Response:
```json
{
  "group_id": "uuid",
  "group_name": "Basic Vocabulary",
  "words": [
    {
      "id": "uuid",
      "word": "example",
      "definition": "a representative form or pattern",
      "mastery_level": 0.8
    }
  ],
  "pagination": {
    "total": 100,
    "per_page": 100,
    "current_page": 1,
    "total_pages": 1
  }
}
```

#### GET /api/groups/:id/study_sessions
Returns study sessions for a specific group.

Response:
```json
{
  "group_id": "uuid",
  "sessions": [
    {
      "id": "uuid",
      "started_at": "2025-02-13T20:00:00Z",
      "completed_at": "2025-02-13T20:30:00Z",
      "words_reviewed": 50,
      "accuracy": 0.85
    }
  ],
  "pagination": {
    "total": 20,
    "per_page": 100,
    "current_page": 1,
    "total_pages": 1
  }
}
```

### Study Sessions Endpoints

#### GET /api/study_sessions
Returns a paginated list of study sessions.

Response:
```json
{
  "sessions": [
    {
      "id": "uuid",
      "group": {
        "id": "uuid",
        "name": "Basic Vocabulary"
      },
      "started_at": "2025-02-13T20:00:00Z",
      "completed_at": "2025-02-13T20:30:00Z",
      "words_reviewed": 50,
      "accuracy": 0.85
    }
  ],
  "pagination": {
    "total": 500,
    "per_page": 100,
    "current_page": 1,
    "total_pages": 5
  }
}
```

#### GET /api/study_sessions/:id
Returns details of a specific study session.

Response:
```json
{
  "id": "uuid",
  "group": {
    "id": "uuid",
    "name": "Basic Vocabulary"
  },
  "started_at": "2025-02-13T20:00:00Z",
  "completed_at": "2025-02-13T20:30:00Z",
  "words_reviewed": 50,
  "accuracy": 0.85,
  "duration": 1800,
  "performance_breakdown": {
    "perfect": 40,
    "good": 5,
    "needs_review": 5
  }
}
```

#### GET /api/study_sessions/:id/words
Returns words reviewed in a specific study session.

Response:
```json
{
  "session_id": "uuid",
  "words": [
    {
      "id": "uuid",
      "word": "example",
      "reviewed_at": "2025-02-13T20:15:00Z",
      "correct": true,
      "response_time": 2.5 // in seconds
    }
  ],
  "pagination": {
    "total": 50,
    "per_page": 100,
    "current_page": 1,
    "total_pages": 1
  }
}
```

#### POST /api/study_sessions/:id/reset_history
Reset the study history for a session.

Response:
```json
{
  "status": "success",
  "message": "Study session history has been reset",
  "reset_at": "2025-02-13T21:07:53Z"
}
```

#### POST /api/study_sessions/:id/full_reset
Completely reset a study session.

Response:
```json
{
  "status": "success",
  "message": "Study session has been fully reset",
  "reset_at": "2025-02-13T21:07:53Z"
}
```

#### POST /api/study_sessions/:id/words/:word_id/review
Submit a review for a word in a study session.

Request:
```json
{
  "correct": true
}
```

Response:
```json
{
  "status": "success",
  "word_id": "uuid",
  "new_mastery_level": 0.85,
  "streak": 5,
  "next_review_due": "2025-02-14T21:07:53Z"
}
```



## Invoke Tasks
Lets list out the tasks that we need for our lang portal.

### Intialize Database
This task will initialize the Flask-SQLAlchemy database called words.db

### Migrate Database
This task will migrate the database to the latest version.

Migrations should be written in Python using the Flask-Migrate package.
Migrations live in the `migrations` directory.
The files should look like this:
```sql
0001_initial_migration.sql
0002_create_words_table.sql
```

### Seed Data
This task will import json files and transform them into target data for our database.

All seed files live in the `seed` directory.
All seed files should be loaded. 

In our task we should have a DSL to specify which seed files should be loaded and in what order.


