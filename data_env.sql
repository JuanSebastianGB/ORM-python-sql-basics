CREATE DATABASE IF NOT EXISTS orm_learning_db;
CREATE USER IF NOT EXISTS 'orm_learning_user' @'localhost' IDENTIFIED BY 'orm_learning_pwd';
GRANT ALL PRIVILEGES ON orm_learning_db.* TO 'orm_learning_user' @'localhost';
FLUSH PRIVILEGES;