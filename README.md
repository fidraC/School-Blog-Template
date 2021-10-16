# YCISCQ-Website

## Features
1. Login feature for STT members and teachers
2. Interactive comment system for news articles
3. Possible revision section for secondary students 
4. Informations about upcoming events 
5. GUI developed in python + html (Chris has set up the design already) 
6. Informations about student leader bodies 

## Plan of action
1. Set up database for admin accounts and news articles
2. Create basic configurations and get request handling for python flask
3. Work on post requests and backend database management
4. Do front end html templates with bootstrap css (No javascript. Hate it)
5. etc...
## Login feature for STT members and teachers
Requirements: 
- Database table for accounts
- Permission system for:
  - Creating and editing entries for
    - News articles
    - Upcoming events
  - Banning users
  - Editing user data
  - Resetting passwords of other users
  - etc.
SQLite databse table: `admin_accounts`
- USER_ID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
- USERNAME varchar(20) UNIQUE NOT NULL,
- PASSWORD_HASH varchar(32) NOT NULL,
- SETTINGS INTEGER

*Hashing algorithm: md5*

*SETTINGS: Each digit will represent true or false for one permission. E.g. Digit 1 for permission to create and edit news articles, digit 2 for allowing user management, etc...*

## Interactive comment system for news articles
Requirements:
- Two database tables
  - article
  - comments
*Plagerized articles can be converted from pdf to markdown via online tools*


SQLite database table: `article`
- ID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
- TITLE varchar(70) UNIQUE NOT NULL,
- DESCRIPTION TEXT NOT NULL,
- CONTENT BLOB NOT NULL,
- AUTHOR varchar(30) NOT NULL,
- CREATION_DATE real NOT NULL,
- SETTINGS integer

*Lightbulb moment: Use python markdown for content. No longer have to do complex configurations for formatting 🤯*

SQLite database table: `comments`
- ID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
- TITLE varchar(70) UNIQUE NOT NULL,
- CONTENT TEXT NOT NULL,
- AUTHOR varchar(30) NOT NULL,
- CREATION_DATE real NOT NULL,
- SETTINGS integer

## Possible revision section for secondary students
***Saving for last as it is the most difficult. (File handling should be easy, however, ensuring that the files are not malicious and preventing spam in extremely annoying and difficult.)***
