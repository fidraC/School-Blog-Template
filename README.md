# YCISCQ-Website

## Features
1. Login feature for STT members and teachers
2. Interactive comment system for news articles
3. Possible revision section for secondary students 
4. Informations about upcoming events 
5. GUI developed in python + html (Chris has set up the design already) 
6. Informations about student leader bodies 

## Task manager
@Chris
- Work on Navbar
- Then work on login (One file is enough. I will customize later for client and admin)

@Me
- Work on news article posting backend: Upload markdown file, title, description, etc.
- Do some frontend templates if Chris doesn't begin working (So that proper testing of the backend can be done)
- Continue updating database to fit requirements

@Done
- Admin login backend
- Not much else...
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

SQLite database table: `article_comments`
- ID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
- TITLE varchar(70) UNIQUE NOT NULL,
- CONTENT TEXT NOT NULL,
- AUTHOR varchar(30) NOT NULL,
- CREATION_DATE real NOT NULL,
- SETTINGS integer

## Possible revision section for secondary students
***Saving for last as it is the most difficult. (File handling should be easy, however, ensuring that the files are not malicious and preventing spam in extremely annoying and difficult.)***
