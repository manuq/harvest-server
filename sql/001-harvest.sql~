CREATE DATABASE harvest;

USE harvest;

CREATE TABLE laptops (
  serial_number VARCHAR(255),
  uuid VARCHAR(255),
  model VARCHAR(255),
  update_version VARCHAR(255),
  build VARCHAR(255),
  updated INT(11),
  collected INT(11),
  codigo_tilo INT(11),
  stored INT(11),
  PRIMARY KEY (serial_number)
);

CREATE TABLE learners (
  serial_number VARCHAR(255),
  birthdate INT(11),
  gender VARCHAR(6),
  PRIMARY KEY (serial_number, birthdate, gender),
  FOREIGN KEY (serial_number) REFERENCES laptops (serial_number)
);

CREATE TABLE activities (
  bundle_id VARCHAR(255),
  activity_name VARCHAR(255),
  PRIMARY KEY (bundle_id)
);

CREATE TABLE launches (
  timestamp INT(11),
  spent_time INT(11),
  launches_number INT(11),
  bundle_id VARCHAR(255),
  serial_number varchar(255),
  birthdate int(11),
  gender varchar(6),
  PRIMARY KEY (timestamp, bundle_id, serial_number, birthdate, gender),
  FOREIGN KEY (bundle_id) REFERENCES activities (bundle_id),
  FOREIGN KEY (serial_number, birthdate, gender) REFERENCES learners (serial_number, birthdate, gender)
);

CREATE TABLE gnome_launches (
  timestamp INT(11),
  spent_time INT(11),
  launches_number INT(11),
  app_name VARCHAR(255) NOT NULL,
  serial_number VARCHAR(255),
  birthdate INT(11),
  gender VARCHAR(6),
  PRIMARY KEY (timestamp, serial_number, birthdate, gender),
  FOREIGN KEY (serial_number, birthdate, gender) REFERENCES learners (serial_number, birthdate, gender)
);

CREATE TABLE sessions (
  timestamp INT(11),
  spent_time INT(11),
  is_sugar TINYINT(1),
  serial_number VARCHAR(255),
  birthdate INT(11),
  gender VARCHAR(6),
  PRIMARY KEY (timestamp, serial_number, birthdate, gender),
  FOREIGN KEY (serial_number, birthdate, gender) REFERENCES learners(serial_number, birthdate, gender)
);

CREATE TABLE gnome_alias (
  app_id VARCHAR(255) NOT NULL,
  app_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (app_name)
);

CREATE USER 'harvest'@'%' IDENTIFIED BY 'harvest';
GRANT ALL PRIVILEGES ON harvest . * TO 'harvest'@'%';
