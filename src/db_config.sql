DROP TABLE IF EXISTS admin_accounts;
CREATE TABLE admin_accounts (
  user_id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
  username varchar(20) UNIQUE NOT NULL,
  password_hash varchar(32) NOT NULL,
  department TEXT NOT NULL,
  settings INTEGER
);
DROP TABLE IF EXISTS client_accounts;
CREATE TABLE client_accounts (
  user_id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
  email varchar(89) UNIQUE NOT NULL,
  username varchar(20) UNIQUE NOT NULL,
  password_hash varchar(32) NOT NULL,
  settings INTEGER
);
DROP TABLE IF EXISTS comments;
CREATE TABLE comments(
  id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
  title varchar(70) UNIQUE NOT NULL,
  content TEXT NOT NULL,
  author varchar(20) NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  settings integer
);
DROP TABLE IF EXISTS reported_user;
CREATE TABLE reported_user (
  id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
  title varchar(70) UNIQUE NOT NULL,
  details TEXT NOT NULL,
  author_id INTEGER NOT NULL,
  reported_user_id INTEGER NOT NULL,
  reported_message_id INTEGER NOT NULL
);
DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    preview BLOB,
    content TEXT NOT NULL,
    department TEXT NOT NULL
);
