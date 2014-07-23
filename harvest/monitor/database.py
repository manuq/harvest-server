import MySQLdb

class Database():
    # QUERY_USO_SEMANAL = "SELECT YEAR(FROM_UNIXTIME(timestamp)), "\
    #                     "WEEK(FROM_UNIXTIME(timestamp)), "\
    #                     "SEC_TO_TIME(SUM(spent_time) / COUNT(DISTINCT sessions.serial_number)) "\
    #                     "FROM sessions, laptops "\
    #                     "WHERE sessions.serial_number = laptops.serial_number "\
    #                     "GROUP BY YEAR(FROM_UNIXTIME(timestamp)), WEEK(FROM_UNIXTIME(timestamp));"

    QUERY_USO_SEMANAL = "SELECT x.year, x.week, spent_sugar, spent_gnome FROM ( "\
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

    QUERY_SUGAR_GNOME = "SELECT SUM(spent_time), is_sugar FROM sessions GROUP BY is_sugar;"

    QUERY_RANKING_ACTS = "SELECT SUM(spent_time), "\
                         "bundle_id "\
                         "FROM launches "\
                         "WHERE spent_time IS NOT NULL "\
                         "GROUP BY bundle_id "\
                         "ORDER BY SUM(spent_time) DESC "\
                         "LIMIT 10;"

    QUERY_RANKING_APPS = "SELECT SUM(spent_time), "\
                         "app_name "\
                         "FROM gnome_launches "\
                         "WHERE spent_time IS NOT NULL "\
                         "GROUP BY app_name "\
                         "ORDER BY SUM(spent_time) DESC "\
                         "LIMIT 10;"

    def __init__(self, host, port, username, password, database):
        self._connection = MySQLdb.connect(host=host,
                                           port=port,
                                           user=username,
                                           passwd=password,
                                           db=database)

    def get_uso_semanal(self):
        self._connection.ping(True)
        cursor = self._connection.cursor()
        cursor.execute(self.QUERY_USO_SEMANAL)

        def total_seconds(time):
            if time is None:
                return 0
            return time.total_seconds()

        result = []
        for row in cursor.fetchall():
            result.append({
                'year': row[0],
                'week': row[1],
                'spent_sugar': total_seconds(row[2]),
                'spent_gnome': total_seconds(row[3]),
            })

        return result

    def get_uso_sugar_gnome(self):
        self._connection.ping(True)
        cursor = self._connection.cursor()
        cursor.execute(self.QUERY_SUGAR_GNOME)

        def get_session(is_sugar):
            if is_sugar:
                return "Sugar"
            else:
                return "GNOME"

        result = []
        for row in cursor.fetchall():
            value = 0
            if row[0] is not None:
                value = int(row[0])
            result.append({
                'value': value,
                'session': get_session(row[1]),
            })

        return result

    def get_ranking_acts(self):
        self._connection.ping(True)
        cursor = self._connection.cursor()
        cursor.execute(self.QUERY_RANKING_ACTS)

        def name_from_bundle(bundle_id):
            return bundle_id.split('.')[-1]

        result = []
        for row in cursor.fetchall():
            result.append({
                'spent_time': int(row[0]),
                'bundle_id': name_from_bundle(row[1]),
            })

        return result

    def get_ranking_apps(self):
        self._connection.ping(True)
        cursor = self._connection.cursor()
        cursor.execute(self.QUERY_RANKING_APPS)

        result = []
        for row in cursor.fetchall():
            result.append({
                'spent_time': int(row[0]),
                'app_name': row[1],
            })

        return result
