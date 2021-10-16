# YCISCQ-Website

## Features
1. Login feature for STT members and teachers
2. Interactive comment system for news articles
3. Possible revision section for secondary students 
4. Informations about upcoming events 
5. GUI developed in python + html (have set up the design already) 
6. Informations about student leader bodies 

## Login feature for STT members and teachers
Requirements: 
- Database table for accounts
- Permission system for:
  - Creating and editing entries for
    - News articles
    - Upcoming events
SQLite databse table: `accounts`
- USER_ID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
- USERNAME varchar(20) UNIQUE NOT NULL,
- PASSWORD_HASH varchar(32) NOT NULL,
- SETTINGS INTEGER

*Hashing algorithm: md5*

*SETTINGS: Each digit will represent true or false for one configuration. To be determined...*
