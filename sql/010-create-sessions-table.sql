CREATE TABLE sessions (
    timestamp INT(11) NOT NULL,
    spent_time INT(11),
    is_sugar BOOLEAN,
    serial_number VARCHAR(255),
    birthdate INT(11) NOT NULL,
    gender VARCHAR(6) NOT NULL,
    PRIMARY KEY (timestamp, serial_number, birthdate, gender),
    FOREIGN KEY (serial_number, birthdate, gender) REFERENCES learners (serial_number, birthdate, gender)
);
