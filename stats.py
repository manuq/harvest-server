#!/usr/bin/env python

import os
import tornado.ioloop
import tornado.web
import harvest.stats.handler
import harvest.stats.database
import ConfigParser


script_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(script_path, 'etc/harvest.cfg')

config = ConfigParser.ConfigParser()
config.read(config_path)

database = harvest.stats.database.Database(
    config.get('datastore', 'host'),
    config.getint('datastore', 'port'),
    config.get('datastore', 'username'),
    config.get('datastore', 'password'),
    config.get('datastore', 'database'))

application = tornado.web.Application([
    (r"/", harvest.stats.handler.Handler,
     {'database': database}),
])

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
