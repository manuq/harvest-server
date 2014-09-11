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
  harvest_version VARCHAR(255),
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
  enabled TINYINT(1) DEFAULT 1,
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
  enabled TINYINT(1) DEFAULT 1,
  PRIMARY KEY (app_name)
);

CREATE TABLE tilo (
  uuid VARCHAR(255) NOT NULL,
  fecha_act DATE NOT NULL,
  serial_number VARCHAR(255) NOT NULL ,
  departamento VARCHAR(45) NULL ,
  tipo_institucion VARCHAR(45) NULL ,
  codigo_institucion VARCHAR(45) NULL ,
  perfil VARCHAR(45) NULL ,
  grado INT NULL ,
  fecha_nac DATE NULL ,
  modelo_equipo VARCHAR(45) NULL ,
  PRIMARY KEY (uuid, fecha_act)
);

CREATE TABLE logs_tilo (
  fecha INT(11) NOT NULL,
  uuid VARCHAR(255) NOT NULL,
  msj_error VARCHAR(255) NOT NULL,
  PRIMARY KEY (fecha, uuid) 
);	

CREATE USER 'harvest'@'%' IDENTIFIED BY 'harvest';
GRANT ALL PRIVILEGES ON harvest . * TO 'harvest'@'%';
