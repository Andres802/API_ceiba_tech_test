DROP DATABASE IF EXISTS pruebaceiba;
CREATE DATABASE IF NOT EXISTS pruebaceiba;
CREATE USER IF NOT EXISTS 'ceiba'@'localhost' IDENTIFIED BY 'ceiba';
GRANT ALL PRIVILEGES ON `pruebaceiba`.* TO 'ceiba'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'ceiba'@'localhost';
FLUSH PRIVILEGES;