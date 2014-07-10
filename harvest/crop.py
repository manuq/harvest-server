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

# Chequear codigos reales
codigos_tilo = {
    "XO-1": 813,
    "XO-1.5-high-school": 818,
    "XO-1.5-lite": 819,
    "XO-1.75": 820,
    "XO-1.75HS": 820,
    "XO-4-Touch": 888,
}

class Crop(object):

    @staticmethod
    def querify(data):
        """ split data for queries format """

        laptops = None
        learners = None
        activities = None
        launches = None
        gnome_launches = None
        sessions = None

        # dijkstra... forgive me!
        model = data[0][2]
        codigo = codigos_tilo.get(model)
        laptops = [data[0] + [codigo]]

        learners = [[data[0][0]] + data[1]]

        if data[2]:
            activities = []
            launches = []

        for activity, data_list in data[2].items():
            activities.append([activity])
            for launch_data in data_list:
                launches.append(launch_data + [activity] + learners[0])

        if data[3]:
            gnome_launches = []

        for gnome_launch_data in data[3]:
            gnome_launches.append(gnome_launch_data + learners[0])

        if data[4]:
            sessions = []

        for timestamp, spent_time, is_sugar in data[4]:
            sessions.append([timestamp, spent_time, is_sugar] + learners[0])

        return laptops, learners, activities, launches, gnome_launches, sessions
