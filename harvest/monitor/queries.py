import os
from tornado.template import Template


SQL_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sql')


class Queries(object):
    def __init__(self):
        self._queries = {}

        for root, dirs, files in os.walk(SQL_PATH):
            for filename in files:
                self._insert_sql(filename)

    def _insert_sql(self, filename):
        query = os.path.splitext(filename)[0]
        self._queries[query] = open(os.path.join(SQL_PATH, filename)).read()

    def is_valid(self, query):
        return query in self._queries.keys()

    def get_content(self, query, arguments):
        if arguments:
            return Template(self._queries[query]).generate(**arguments)
        else:
            return self._queries[query]
