select DATE(FROM_UNIXTIME(s.timestamp)), s.spent_time/60, t.* from sessions s, tilo t where t.serial_number = s.serial_number;
