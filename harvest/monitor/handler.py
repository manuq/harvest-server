import json
from tornado.web import RequestHandler, HTTPError


class HomeHandler(RequestHandler):
    def get(self):
        self.render('home.html')

class JsonHandler(RequestHandler):
    def initialize(self, database):
        self._database = database

    def get(self, query):
        if self._database.is_not_valid(query):
            raise HTTPError(404)

        content = self._database.get(query, output='json')
        self.write(content)

class CSVHandler(RequestHandler):
    def initialize(self, database):
        self._database = database

    def get(self, query):
        if self._database.is_not_valid(query):
            raise HTTPError(404)

        content = self._database.get(query, output='csv')
        self.write(content)
