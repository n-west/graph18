#!/usr/bin/python2.7

'''
This provides helper classes that assist with generating graphs
that are useful for working with 18xx problems.
'''

# Copyright 2014 Nathan West
# This file is part of graph18.
# 
# graph18 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# graph18 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with graph18.  If not, see <http://www.gnu.org/licenses/>.


import networkx as nx

class Cities(object):
    '''
    This class contains all of the information required to calculate
    revenue for a city. It is the primary graph node.
    '''
    def __init__(self, value, color=0, stop_type='city', capacity=1, owners=['']):
        '''
        Parameters:
            value: the revenue when passing through the city
            color: color of the tile. defaults to yellow
            stop_type: 'town', or 'city' used for trains with +# ability
            capacity: number of station markers possible
            owners: list of companies with station markes persent. (owners.__len__() <= capacity)
        '''
        self.owners = ['']
        assert isinstance(owners, (list, tuple)), \
            "%r is not an iterable object like list or tuple" % owner
        map(self.add_owner, owners)

        self.set_stop_type(stop_type)

        assert capacity > 0, "%r is not a number above 0. Should be int"

        # this better be a number
        self.set_value(value)

        self.set_color(color)

    def set_value(self, value):
        self.value = value

    def set_stop_type(self, stop_type):
        assert (stop_type == 'city' or stop_type == 'town'), \
            "%r is not a city or town" % stop_type
        self.stop_type = stop_type

    # there's a color helper class in plot.py but this class doesn't care about it
    def set_color(self, color):
        self.color = color

    def add_owner(self, owner):
        assert isinstance(owner, basestring), \
            "%r is not a string" % owner

        if self.owners[0] == '':
            self.owners.pop(0)
        self.owners.append(owner)


