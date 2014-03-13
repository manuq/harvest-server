CREATE TABLE sessions (
    start_time INT(11) NOT NULL,
    spent_time INT(11),
    is_sugar BOOLEAN,
    serial_number VARCHAR(255),
    PRIMARY KEY (start_time, is_sugar, serial_number),
    FOREIGN KEY (serial_number) REFERENCES learners (serial_number)
);
