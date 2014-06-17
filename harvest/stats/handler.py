from tornado.web import RequestHandler

class Handler(RequestHandler):
    def initialize(self, database):
        self._database = database

    def get(self):
        result = self._database.get_uso_semanal()
        for row in result:
            self.write("<p>Tiempo de uso: {0}</p>".format(row[0]))
