CREATE TABLE connectivity (
    timestamp INT(11) NOT NULL,
    access_point_common VARCHAR(255),
    signal_level_median FLOAT(11, 2),
    bit_rate_median FLOAT(11, 2),
    retries_added INT(11),
    frequency FLOAT(11, 2),
    rx_median FLOAT(11, 2),
    tx_median FLOAT(11, 2),
    rx_added INT(11),
    tx_added INT(11),
    serial_number VARCHAR(255),
    birthdate INT(11) NOT NULL,
    gender VARCHAR(6) NOT NULL,
    PRIMARY KEY (timestamp, serial_number, birthdate, gender),
    FOREIGN KEY (serial_number, birthdate, gender) REFERENCES learners (serial_number, birthdate, gender)
);
