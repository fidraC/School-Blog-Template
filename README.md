# School Blog Template
By: Antonio Cheong

Serves as the basis for my CAS project at YCISCQ-Student-Tech-Team/YCISCQ-Website. This will be a personal project without the vision being clouded by multiple collaborators. I hope to one day expand this project to the scale of ManageBac...

## Features
1. Administration and moderation ✅ (/admin)
2. Interactive comment system for news articles ✅ (/isso)
3. Possible revision section for secondary students (/revision)
4. Informations about upcoming events ✅ (/posts)
5. Front end client interface ✅ (/) 
6. Informations about student leader bodies ✅ (/about)

## Task manager
- Email verification on signup
- Possible revision section for secondary students (This section of the project will be made independent from the core website and can be enabled/disabled from the config file)
  - Database...
    - TITLE, CREATED, AUTHOR, DESCRIPTION, COST, FILEPATH (ZIP files only)
  - Use markdown editor for description...
  - Limit file upload sizes...
  - PATHS
    - /revision/new
    - /revision/index
    - /revision/page/post_id

How to incentivize students to use this feature?
- Point system?
- Merits?
- $$$?
Perhaps: 
```
Creators: Students who post notes and other content
Consumers: Students who download content from the Creators
```
Creators can set 'prices' to their content, meaning that the consumers must pay that amount in points to download the content. The creators will therefore receive that amount of points when consumers download their content.
Each new user begins with 5 points
If enough people begin using this feature, allow people to purchase 'points' with real money?????????? (I'll keep dreaming of profiting off of this... Just a dream)


@Done
- Posting and displaying posts
- Authentication
- Commenting
- Darkmode / Lightmode themes
- Inline markdown editor
- Make modular
  - Use JSON config file for departments and admins
  - Make school name in navbar also configurable through config file
  - Use markdown for index pages and allow admin to edit through admin interface directly
- Create new organization and fork this repo for offical YCISCQ website
- Information on student leader bodies

