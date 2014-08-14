import json
from tornado.web import RequestHandler, HTTPError, authenticated


class AuthHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("password")


class LoginHandler(AuthHandler):
    def initialize(self, password):
        self._password = password

    def get(self):
        self.render('login.html')

    def post(self):
        if self.get_argument("password") != self._password:
            self.redirect("/ingresar")
            return

        self.set_secure_cookie("password", self.get_argument("password"))
        self.redirect("/")

class HomeHandler(AuthHandler):
    @authenticated
    def get(self):
        self.render('home.html')

class EvaluacionMonitoreoHandler(AuthHandler):
    @authenticated
    def get(self):
        self.render('evaluacion_y_monitoreo.html')


class DataHandler(AuthHandler):
    def __init__(self, output, application, request, **kwargs):
        self._output = output
        super(DataHandler, self).__init__(application, request, **kwargs)

    def initialize(self, database):
        self._database = database

    def get(self, query):
        argument_names = ['grado']
        arguments = {}
        for name in argument_names:
            value = self.get_argument(name, None)
            if value is not None:
                arguments[name] = value

        if not self.current_user:
            raise HTTPError(401)

        if not self._database.is_valid(query):
            raise HTTPError(404)

        content = self._database.get(query, arguments, output=self._output)
        if content is None:
            raise HTTPError(404)

        self.write(content)


class JsonHandler(DataHandler):
    def __init__(self, application, request, **kwargs):
        super(JsonHandler, self).__init__('json', application, request,
                                          **kwargs)


class CSVHandler(DataHandler):
    def __init__(self, application, request, **kwargs):
        super(CSVHandler, self).__init__('csv', application, request, **kwargs)
