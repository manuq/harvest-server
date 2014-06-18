import MySQLdb

class Database():
    QUERY_USO_SEMANAL = "SELECT YEAR(FROM_UNIXTIME(timestamp)), WEEK(FROM_UNIXTIME(timestamp)), AVG(spent_time) "\
                        "FROM sessions "\
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
                'spent_time': int(row[2]),
            })

        return result
