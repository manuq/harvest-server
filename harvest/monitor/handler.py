import json
from tornado.web import RequestHandler, HTTPError


class HomeHandler(RequestHandler):
    def get(self):
        self.render('home.html')

class EvaluacionMonitoreoHandler(RequestHandler):
    def get(self):
        self.render('evaluacion_y_monitoreo.html')


class DataHandler(RequestHandler):
    def __init__(self, output, application, request, **kwargs):
        self._output = output
        super(DataHandler, self).__init__(application, request, **kwargs)

    def initialize(self, database):
        self._database = database

    def get(self, query):
        if self._database.is_not_valid(query):
            raise HTTPError(404)

        content = self._database.get(query, output=self._output)
        self.write(content)


class JsonHandler(DataHandler):
    def __init__(self, application, request, **kwargs):
        super(JsonHandler, self).__init__('json', application, request,
                                          **kwargs)


class CSVHandler(DataHandler):
    def __init__(self, application, request, **kwargs):
        super(CSVHandler, self).__init__('csv', application, request, **kwargs)
