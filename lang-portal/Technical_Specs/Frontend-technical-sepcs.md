# Frontend Technical Specs

## Pages

### Dashboard `/dashboard`

#### Purpose
The purpose of this page is to provide a summary of learning and act as the default page when user visits the web-app. 

#### Components
This page contains the following components:
    - Last study session:
        shows last activity used
        shows when last activity was used
        summarizes wrong vs correct from last activity
        has a link to the group

    - Study Progress
       - total words study eg. 3/124
          - across all study sessions show the total words studied out of all
          possible words in our database
          - display a mastery progress eg: 0%
    - Quick Stats
        - success rate eg: 75%
        - total study sessions eg: 5
        - total active groups eg: 3
        - study streak eg: 4 days

    - Start Studying Button
       - goes tot he study activities page

#### Needed API Endponts
We'll need the following API endPoints to power this page:

- GET /api/dashboard/last_stydy_session
- GET /api/dashboard/study_progress
- GET /api/dashboard/quick_stats


### Study Activities Index `/study-activities`

#### Purpose
The purpose of this page is to show a collection of study activites with a thumbnail and it's name, to either launch or view the study activity.

#### Components
This page contains the following components:
- Study Activit Card
    - show a thumbnail of the study activity
    - the name of the study activity
    - a lunch button to take us to the lunch page
    - the view page to view more information about past study sessions for this study activity
    

#### NEEDED API ENDPOINTS
We'll need the following API endPoints to power this page:

- GET /api/study-activities


### Study Activity Show `/study-activities/:id`

#### Purpose
The purpose of this page is to show more information about a study activity
and it's past stidy sessions

#### Components
This page contains the following components:
- Name of study activity
- Thumbnail of study activity
- Description of study activity
- Lunch button to launch the study activity
- Study Activities Paginated List
    - id
    -activity name
    - group name
    - start time
    - end time (infered by the last word_review_item submitted)
    - number of review items

#### Needed API Endpoints
We'll need the following API endPoints to power this page:
- GET /api/study-activities/:id
- GET /api/study-activities/:id/sessions

### Study Activities Lunch `/study-activities/:id/launch`

#### Purpose
The purpose of this page is to launch a study activity. 

#### Components
This page contains the following components:
- Name of study activity
- Lunch Form
   - select field for group
   - Launch now button

## Behavior
After the form is submiited a new tab opens with the study activity 
based on i'ts URL provided in the database. 

ALso the after form is submitted the page will redirect to the study session show page.

#### Needed API Endpoints
We'll need the following API endPoints to power this page:
- POST /api/study-activities/:id/launch
   -  group_id


### Words Index `/words`

#### Purpose
The purpose of this page is to show all words in our database

#### Components
This page contains the following components:
- Pagainated Word List
    - Columns
        - French
        - English
        - Correct Count
        - Wrong Count
    - Pagination with 100 items per page
    - Clcking the French word will take us to the word show page. 

#### Needed API Endpoints
We'll need the following API endPoints to power this page:

- GET /api/words


### Words Show `/words/:id`

#### Purpose
The purpose of this page is to show information about a specific word

#### Components
This page contains the following components:
- Word Information
    - French
    - English
    - Study Statistics
        - Correct Count
        - Wrong Count
    - Word Groups 
       - shown as a series of pills eg: tags
       - When group name is clicked it will take us to group show page.
    
#### Needed API Endpoints
We'll need the following API endPoints to power this page:
- GET /api/words/:id
  - to get the word information
 
 ### Word Groups Index `/groups`

 #### Purpose 
    The purpose of this page is to show a list of groups in our database.

 #### Components
    This page contains the following components:
    - Pagainated Group List
        - Columns
            - Group Name
            - # Words
        - Pagination with 10 items per page
        - Clicking the group name will take us to the group show page. 

#### Needed API Endpoints
We'll need the following API endPoints to power this page:
- GET /api/groups
  - to get a list of groups
- GET /api/groups/:id
  - to get the group information
  - to get the group words


### Groups Show `/groups/:id`

#### Purpose
The purpose of this page is to show information about a specific group

#### Components
This page contains the following components:
- Group Name
- Group Statistics
   - Total word Count
- Words in Group(Paginated list of words)
   - Should use the same component as the words index page.

- Study Sessions in Group(Paginated list of study sessions)
   - Should use the same component as the study activities index page.

    
#### Needed API Endpoints
We'll need the following API endPoints to power this page:
- GET /api/groups/:id (the name and group stats)
- GET /api/groups/:id/words (the list of words in the group)
- GET /api/groups/:id/study_sessions (the list of study sessions in the group)


## Study Sessions Index `/study-sessions`

#### Purpose
The purpose of this page is to show a list of study sessions in our database.

#### Components
This page contains the following components:
- Pagainated Study Session List
    - Columns
        - Id
        - Activity Name
        - Group Name
        - Start Time
        - End Time
        - Number of Review Items
    - Clicking the study activity name will take us to the study session show page. 

#### Needed API Endpoints
We'll need the following API endPoints to power this page:
- GET /api/study-sessions (the list of study sessions)

### Study Session Show `/study-sessions/:id`

#### Purpose
The purpose of this page is to show information about a specific study session

#### Components
This page contains the following components:
- Study Session Details:
    - Activity Name
    - Group Name
    - Start Time
    - End Time
    - Number of Review Items
- Words Review Items (Paginated list of words)
  - should use the same component as the words index page

#### Needed API Endpoints
We'll need the following API endPoints to power this page:
- GET /api/study-sessions/:id (the details of the study session)
- GET /api/study-sessions/:id/words


### Settings Page `/settings`

#### Purpose
The purpose of this page is to allow users to update their preferences or settings of their study portal. 

#### Components
This page contains the following components:
- Theme Selection. Eg: Light, Dark, System
- Language Selection. Eg: English, French, Spanish
- Reset History Button
   - This button will reset all study history. This will delete all study sessions and word review items.
- Full Reset Button
   - This will drop all tables and create new ones with the seed data.

#### Needed API Endpoints
We'll need the following API endPoints to power this page:
 - POST /api/study/reset_history
   - This will delete all study sessions and word review items.
 - POST /api/study/reset
   - This will drop all tables and create new ones with the seed data.