import json
from tornado.web import RequestHandler, HTTPError


class HomeHandler(RequestHandler):
    def get(self):
        self.render('home.html')

class JsonHandler(RequestHandler):
    def initialize(self, database):
        self._database = database

    def get(self, query):
        method_name = 'get_' + query
        if not hasattr(self._database, method_name):
            raise HTTPError(404)

        data = getattr(self._database, method_name)()
        self.write(json.dumps(data))
