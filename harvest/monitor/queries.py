_queries = {}

_queries['tiempo_de_uso'] = \
    "SELECT x.year, x.week, spent_sugar, spent_gnome FROM ( "\
    "  SELECT SEC_TO_TIME(SUM(spent_time) / COUNT(DISTINCT sessions.serial_number)) AS spent_sugar, "\
    "  YEAR(FROM_UNIXTIME(timestamp)) AS year, "\
    "  WEEK(FROM_UNIXTIME(timestamp)) AS week "\
    "  FROM sessions, laptops "\
    "  WHERE is_sugar = 1 "\
    "  AND sessions.serial_number = laptops.serial_number "\
    "  GROUP BY YEAR(FROM_UNIXTIME(timestamp)), WEEK(FROM_UNIXTIME(timestamp)) "\
    ") x "\
    "LEFT JOIN ( "\
    "  SELECT SEC_TO_TIME(SUM(spent_time) / COUNT(DISTINCT sessions.serial_number)) AS spent_gnome, "\
    "  YEAR(FROM_UNIXTIME(timestamp)) AS year, "\
    "  WEEK(FROM_UNIXTIME(timestamp)) AS week "\
    "  FROM sessions, laptops "\
    "  WHERE is_sugar = 0 "\
    "  AND sessions.serial_number = laptops.serial_number "\
    "  GROUP BY YEAR(FROM_UNIXTIME(timestamp)), WEEK(FROM_UNIXTIME(timestamp)) "\
    ") y "\
    "ON x.week = y.week AND x.year = y.year;"

_queries['uso_sugar_gnome'] = \
    "SELECT SUM(spent_time), is_sugar FROM sessions GROUP BY is_sugar;"

_queries['ranking_actividades'] = \
    "SELECT SUM(spent_time), "\
    "bundle_id "\
    "FROM launches "\
    "WHERE spent_time IS NOT NULL "\
    "GROUP BY bundle_id "\
    "ORDER BY SUM(spent_time) DESC "\
    "LIMIT 10;"

_queries['ranking_aplicaciones'] = \
    "SELECT SUM(spent_time), "\
    "app_name "\
    "FROM gnome_launches "\
    "WHERE spent_time IS NOT NULL "\
    "GROUP BY app_name "\
    "ORDER BY SUM(spent_time) DESC "\
    "LIMIT 10;"


def get_queries():
    return _queries
