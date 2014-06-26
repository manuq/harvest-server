import json
from tornado.web import RequestHandler, HTTPError


class HomeHandler(RequestHandler):
    def get(self):
        self.render('home.html')

class JsonHandler(RequestHandler):
    def initialize(self, database):
        self._database = database

    def get(self, query):
        if query == 'tiempo_de_uso':
            data = self._database.get_uso_semanal()
            self.write(json.dumps(data))
        elif query == 'uso_sugar_gnome':
            data = self._database.get_uso_sugar_gnome()
            self.write(json.dumps(data))
        elif query == 'ranking_actividades':
            data = self._database.get_ranking_acts()
            self.write(json.dumps(data))
        elif query == 'ranking_aplicaciones':
            data = self._database.get_ranking_apps()
            self.write(json.dumps(data))
        else:
            raise HTTPError(404)
