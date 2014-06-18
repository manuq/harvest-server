#!/usr/bin/env python

import os
from ConfigParser import ConfigParser
import tornado.ioloop
import tornado.web
import tornado.httpserver
from harvest.monitor.handler import HomeHandler, JsonHandler
from harvest.monitor.database import Database


SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))


class Application(tornado.web.Application):
    def __init__(self):

        database = Database(
            config.get('datastore', 'host'),
            config.getint('datastore', 'port'),
            config.get('datastore', 'username'),
            config.get('datastore', 'password'),
            config.get('datastore', 'database'))

        handlers = [
            (r"/", HomeHandler),
            (r"/json/([^/]+)", JsonHandler, {'database': database}),
        ]

        settings = {
            'template_path': os.path.join(SCRIPT_PATH,
                                          'harvest/monitor/templates/'),
        }

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    config_path = os.path.join(SCRIPT_PATH, 'etc/harvest.cfg')
    config = ConfigParser()
    config.read(config_path)

    application = Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(80)
    tornado.ioloop.IOLoop.instance().start()
