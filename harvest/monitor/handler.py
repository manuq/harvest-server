from tornado.web import RequestHandler


class Handler(RequestHandler):
    def initialize(self, database):
        self._database = database

    def get(self):
        data = self._database.get_uso_semanal()
        # for row in data:
        #     self.write("<p>Tiempo de uso: {0}</p>".format(row[0]))
        self.render('tiempo_de_uso.html', data = data)
