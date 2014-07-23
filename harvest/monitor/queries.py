import os

SQL_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sql')

_queries = {}

def _insert_sql(filename):
    query = os.path.splitext(filename)[0]
    _queries[query] = open(os.path.join(SQL_PATH, filename)).read()


for root, dirs, files in os.walk(SQL_PATH):
    for filename in files:
        _insert_sql(filename)


def get_queries():
    return _queries
