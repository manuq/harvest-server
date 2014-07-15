#!/usr/bin/env python

# Copyright (c) 2013 Martin Abente Lahaye. - tch@sugarlabs.org
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

import os
import time
import signal
from functools import partial
from ConfigParser import ConfigParser

from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.web import Application
from tornado.netutil import bind_sockets
from tornado.options import define, options, parse_command_line
from harvest.handler import Handler
from harvest.data_store import DataStore


define("port", default=443)


def signal_handler(server, loop, signum, frame):
    loop.add_callback(partial(stop_server, server, loop))

def stop_server(server, loop):
    server.stop()
    loop.add_timeout(time.time() + 5.0, partial(stop_loop, loop))

def stop_loop(loop):
    loop.stop()

def main():
    parse_command_line()
    script_path = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_path, 'etc/harvest.cfg')

    config = ConfigParser()
    config.read(config_path)

    sockets = bind_sockets(options.port,
                           config.get('server', 'address'))

    datastore = DataStore(config.get('datastore', 'host'),
                          config.getint('datastore', 'port'),
                          config.get('datastore', 'username'),
                          config.get('datastore', 'password'),
                          config.get('datastore', 'database'))

    app = Application([(r"/rpc/store", Handler,
                       {'datastore': datastore,
                        'api_key': config.get('server', 'api_key')})])

    server = HTTPServer(app,
                        no_keep_alive=config.get('server', 'no_keep_alive'),
                        ssl_options={
                            'certfile': config.get('server', 'certfile'),
                            'keyfile': config.get('server', 'keyfile')})

    server.add_sockets(sockets)
    loop = IOLoop.instance()
    signal.signal(signal.SIGTERM, partial(signal_handler, server, loop))
    loop.start()


if __name__ == "__main__":
    main()
