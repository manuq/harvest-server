import MySQLdb
import json
import csv
import StringIO
import queries


class Database():
    def __init__(self, host, port, username, password, database):
        self._connection = MySQLdb.connect(host=host,
                                           port=port,
                                           user=username,
                                           passwd=password,
                                           db=database)

        self._queries = queries.get_queries()

    def is_not_valid(self, query):
        return query not in self._queries.keys()

    def get(self, query, output='json'):
        self._connection.ping(True)
        cursor = self._connection.cursor()
        cursor.execute(self._queries[query])

        if output == 'json':
            method_name = '_json_' + query
            assert hasattr(self, method_name)
            data = getattr(self, method_name)(cursor)
            return json.dumps(data)

        elif output == 'csv':
            output = StringIO.StringIO()
            writer = csv.writer(output)
            writer.writerows(cursor.fetchall())
            return output.getvalue()

    def _json_tiempo_de_uso(self, cursor):
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

    def _json_uso_sugar_gnome(self, cursor):
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

    def _json_ranking_actividades(self, cursor):
        def name_from_bundle(bundle_id):
            return bundle_id.split('.')[-1]

        result = []
        for row in cursor.fetchall():
            result.append({
                'spent_time': int(row[0]),
                'bundle_id': name_from_bundle(row[1]),
            })

        return result

    def _json_ranking_aplicaciones(self, cursor):
        result = []
        for row in cursor.fetchall():
            result.append({
                'spent_time': int(row[0]),
                'app_name': row[1],
            })

        return result
