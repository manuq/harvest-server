CREATE TABLE gnome_launches (
    timestamp INT(11) NOT NULL,
    spent_time INT(11),
    app_name VARCHAR(255),
    serial_number VARCHAR(255),
    birthdate INT(11) NOT NULL,
    gender VARCHAR(6) NOT NULL,
    PRIMARY KEY (timestamp, serial_number, birthdate, gender),
    FOREIGN KEY (serial_number, birthdate, gender) REFERENCES learners (serial_number, birthdate, gender)
);
