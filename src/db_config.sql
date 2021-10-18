DROP TABLE IF EXISTS admin_accounts;
CREATE TABLE admin_accounts (
  user_id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
  username varchar(20) UNIQUE NOT NULL,
  password_hash varchar(32) NOT NULL,
  settings INTEGER
);
DROP TABLE IF EXISTS client_accounts;
CREATE TABLE admin_accounts (
  user_id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
  username varchar(20) UNIQUE NOT NULL,
  password_hash varchar(32) NOT NULL,
  settings INTEGER
);
DROP TABLE IF EXISTS article;
CREATE TABLE article (
  id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
  title varchar(70) UNIQUE NOT NULL,
  description TEXT NOT NULL,
  content BLOB NOT NULL,
  author varchar(20) NOT NULL,
  creation_date real NOT NULL,
  settings integer
);
DROP TABLE IF EXISTS article_comments;
CREATE TABLE article_comments (
  id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
  title varchar(70) UNIQUE NOT NULL,
  content TEXT NOT NULL,
  author varchar(20) NOT NULL,
  creation_date real NOT NULL,
  settings integer
);
DROP TABLE IF EXISTS reports;
CREATE TABLE reports (
  id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
  title varchar(70) UNIQUE NOT NULL,
  details TEXT NOT NULL,
  author_id INTEGER NOT NULL,
  reported_user_id INTEGER NOT NULL,
  reported_message_id INTEGER NOT NULL
)
