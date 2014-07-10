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

import MySQLdb

from .error import StoreError
from .crop import Crop


class DataStore(object):

    QUERY_LAPTOP = 'INSERT INTO laptops '\
                   '(serial_number, uuid, model, update_version, build, updated, collected, codigo_tilo, stored) '\
                   'values (%s, %s, %s, %s, %s, %s, %s, %s, UNIX_TIMESTAMP(now())) '\
                   'ON DUPLICATE KEY UPDATE '\
                   'uuid = VALUES(uuid), '\
                   'model = VALUES(model), '\
                   'update_version = VALUES(update_version), '\
                   'build = VALUES(build), '\
                   'updated = VALUES(updated), '\
                   'collected = VALUES(collected), '\
		   'codigo_tilo = VALUES(codigo_tilo), '\
                   'stored = values(stored)'

    QUERY_LEARNER = 'INSERT INTO learners '\
                    '(serial_number, birthdate, gender) '\
                    'values (%s, %s, %s) '\
                    'ON DUPLICATE KEY UPDATE '\
                    'birthdate = VALUES(birthdate), '\
                    'gender = VALUES(gender)'

    QUERY_ACTIVITY = 'INSERT INTO activities '\
                     '(bundle_id) '\
                     'values (%s) '\
                     'ON DUPLICATE KEY UPDATE '\
                     'bundle_id = VALUES(bundle_id)'

    QUERY_LAUNCH = 'INSERT INTO launches '\
                   '(timestamp, spent_time, launches_number, bundle_id, serial_number, birthdate, gender) '\
                   'values (%s, %s, %s, %s, %s, %s, %s) '\
                   'ON DUPLICATE KEY UPDATE '\
                   'timestamp = VALUES(timestamp), '\
                   'spent_time = VALUES(spent_time), '\
                   'launches_number = VALUES(launches_number), '\
                   'bundle_id = VALUES(bundle_id), '\
                   'serial_number = VALUES(serial_number), '\
                   'birthdate = VALUES(birthdate), '\
                   'gender = VALUES(gender)'

    QUERY_GNOME_LAUNCH = 'INSERT INTO gnome_launches '\
                         '(timestamp, spent_time, launches_number, app_name, serial_number, birthdate, gender) '\
                         'values (%s, %s, %s, %s, %s, %s, %s) '\
                         'ON DUPLICATE KEY UPDATE '\
                         'timestamp = VALUES(timestamp), '\
                         'spent_time = VALUES(spent_time), '\
                         'launches_number = VALUES(launches_number), '\
                         'app_name = VALUES(app_name), '\
                         'serial_number = VALUES(serial_number), '\
                         'birthdate = VALUES(birthdate), '\
                         'gender = VALUES(gender)'

    QUERY_SESSION = 'INSERT INTO sessions '\
                    '(timestamp, spent_time, is_sugar, serial_number, birthdate, gender) '\
                    'values (%s, %s, %s, %s, %s, %s) '\
                    'ON DUPLICATE KEY UPDATE '\
                    'timestamp = VALUES(timestamp), '\
                    'spent_time = VALUES(spent_time), '\
                    'is_sugar = VALUES(is_sugar), '\
                    'serial_number = VALUES(serial_number), '\
                    'birthdate = VALUES(birthdate), '\
                    'gender = VALUES(gender)'

    def __init__(self, host, port, username, password, database):
        self._connection = MySQLdb.connect(host=host,
                                           port=port,
                                           user=username,
                                           passwd=password,
                                           db=database)

    def store(self, data):
        """ extracts metadata and inserts to the database """
        laptops, learners, activities, launches, gnome_launches, sessions = Crop.querify(data)

        self._connection.ping(True)
        try:
            self._connection.begin()
            cursor = self._connection.cursor()
            if laptops is not None:
                cursor.executemany(self.QUERY_LAPTOP, laptops)
            if learners is not None:
                cursor.executemany(self.QUERY_LEARNER, learners)
            if activities is not None:
                cursor.executemany(self.QUERY_ACTIVITY, activities)
            if launches is not None:
                cursor.executemany(self.QUERY_LAUNCH, launches)
            if gnome_launches is not None:
                cursor.executemany(self.QUERY_GNOME_LAUNCH, gnome_launches)
            if sessions is not None:
                cursor.executemany(self.QUERY_SESSION, sessions)
            self._connection.commit()
        except Exception as err:
            print err
            self._connection.rollback()
            raise StoreError
        finally:
            cursor.close()

    def __del__(self):
        if hasattr(self, '_connection') and self._connection is not None:
            self._connection.close()
