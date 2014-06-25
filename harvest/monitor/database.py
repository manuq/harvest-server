import MySQLdb

class Database():
    QUERY_USO_SEMANAL = "SELECT YEAR(FROM_UNIXTIME(timestamp)), "\
                        "WEEK(FROM_UNIXTIME(timestamp)), "\
                        "SEC_TO_TIME(SUM(spent_time) / COUNT(DISTINCT sessions.serial_number)) "\
                        "FROM sessions, laptops "\
                        "WHERE sessions.serial_number = laptops.serial_number "\
                        "GROUP BY YEAR(FROM_UNIXTIME(timestamp)), WEEK(FROM_UNIXTIME(timestamp));"

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

        result = []
        for row in cursor.fetchall():
            result.append({
                'year': row[0],
                'week': row[1],
                'spent_time': row[2].total_seconds(),
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
                'bundle_id': row[1],
            })

        return result
