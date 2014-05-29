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


class Crop(object):

    @staticmethod
    def querify(data):
        """ split data for queries format """

        laptops = None
        learners = None
        activities = None
        instances = None
        launches = None
        gnome_launches = None
        sessions = None
        connectivity = None

        # dijkstra... forgive me!
        laptops = [data[0]]
        learners = [[data[0][0]] + data[1]]

        for activity in data[2].keys():
            if activities is None:
                activities = []
            activities.append([activity])

            for instance in data[2][activity]:
                if instances is None:
                    instances = []
                instances.append(instance[:-1] + [activity] + learners[0])

                for launch, spent_time in instance[-1]:
                    if launches is None:
                        launches = []
                    launches.append([launch, spent_time] +
                                    [instance[0]] + learners[0])

        for timestamp, spent_time, app_name in data[3]:
            if gnome_launches is None:
                gnome_launches = []
            gnome_launches.append([timestamp, spent_time, app_name] + learners[0])

        for timestamp, spent_time, is_sugar in data[4]:
            if sessions is None:
                sessions = []
            sessions.append([timestamp, spent_time, is_sugar] + learners[0])

        for timestamp, ap, sl, br, ret, freq, rxm, txm, rxd, txd in data[5]:
            if connectivity is None:
                connectivity = []
            connectivity.append([timestamp, ap, sl, br, ret, freq, rxm, txm, rxd, txd] + learners[0])

        return laptops, learners, activities, instances, launches, gnome_launches, sessions, connectivity
