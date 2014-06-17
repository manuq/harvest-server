import MySQLdb

class Database():
    QUERY_USO_SEMANAL = "SELECT TIME_FORMAT(SEC_TO_TIME(AVG(spent_time)),'%Hh %im') "\
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
        return cursor.fetchall()
