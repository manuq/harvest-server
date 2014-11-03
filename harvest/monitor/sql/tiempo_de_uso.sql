SELECT x.year, x.week, spent_sugar, spent_gnome FROM (
  SELECT SEC_TO_TIME(SUM(spent_time) / COUNT(DISTINCT sessions.serial_number)) AS spent_sugar,
  YEAR(FROM_UNIXTIME(timestamp)) AS year,
  WEEK(FROM_UNIXTIME(timestamp)) AS week
  FROM sessions, laptops
  WHERE is_sugar = 1
  AND sessions.serial_number = laptops.serial_number
  AND spent_time > 0 and spent_time/60/60 < 24
  and YEAR(FROM_UNIXTIME(timestamp)) > 2013
  GROUP BY YEAR(FROM_UNIXTIME(timestamp)), WEEK(FROM_UNIXTIME(timestamp))
) x
LEFT JOIN (
  SELECT SEC_TO_TIME(SUM(spent_time) / COUNT(DISTINCT sessions.serial_number)) AS spent_gnome,
  YEAR(FROM_UNIXTIME(timestamp)) AS year,
  WEEK(FROM_UNIXTIME(timestamp)) AS week
  FROM sessions, laptops
  WHERE is_sugar = 0
  AND sessions.serial_number = laptops.serial_number
  AND spent_time > 0 and spent_time/60/60 < 24
  and YEAR(FROM_UNIXTIME(timestamp)) > 2013
  GROUP BY YEAR(FROM_UNIXTIME(timestamp)), WEEK(FROM_UNIXTIME(timestamp))
) y
ON x.week = y.week AND x.year = y.year;
