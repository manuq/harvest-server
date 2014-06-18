import MySQLdb

class Database():
    QUERY_USO_SEMANAL = "SELECT YEAR(FROM_UNIXTIME(timestamp)), "\
                        "WEEK(FROM_UNIXTIME(timestamp)), "\
                        "SEC_TO_TIME(SUM(spent_time) / COUNT(DISTINCT sessions.serial_number)) "\
                        "FROM sessions, laptops "\
                        "WHERE sessions.serial_number = laptops.serial_number "\
                        "GROUP BY YEAR(FROM_UNIXTIME(timestamp)), WEEK(FROM_UNIXTIME(timestamp));"

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
