#!/usr/bin/python2.7

'''
This file defines the companies available in 18xx games and provides
an interface class to let the user define new companies.
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


class Train(object):
    '''
    Defines train attributes that can be held by a company
    '''
    def __init__(self, all_cap, city_cap=0, town_cap=0, ndouble=0):
        '''
        Trains(all_cap[, city_cap=0, town_cap=0])

        Define a train based on how many towns and cities
        it can be run through. The idea here is to keep
        this generic enough to be used for sveral expansions
        that all have slightly different train routes.
        
        Parameters:
            all_cap - for standard trains this is the number
                so that they can go through all_cap towns
                and cities. This should be 0 for "plus"
                trains.
            city_cap - for "plus" trains or OE-style standard
                trains this is the number of cities it can run
                through. The assumption for OE-style trains
                is that it's always better to run through cities
                rather than towns
            town_cap - for "plus" trains this indicates how many
                towns can be run through without deducting from
                how many cities can be run
            ndouble - number of cities that can be doubled
        '''
        self.all_cap = all_cap
        self.city_cap = city_cap
        self.town_cap = town_cap
        self.ndouble = ndouble
        

class Company(object):
    '''
    This is a container for a company that primarily
    defines the trains that are held by said company

    note for future: in theory this could track cash
    and spare tokens to assist with laying new tokens,
    but at some point that makes this not an aid but
    an AI that's actually playing part of the game 
    rather than the player making decisions. For now 
    at least we just calculate the best route currently
    available.
    '''
    def __init__(self, name, trains=[]):
        '''
        Company(name[, trains=[])
        
        Parameters:
            name - a string with name of company
            trains - a list of Train objects
        '''
        self.name = name
        self.trains = trains

    def add_train(self, train):
        '''
        add_train(Train)

        Use this when a company acquires a new train.
        '''
        self.trains.append(train)
        
null_company = Company('null')
prr = Company('Pennsylvannia RailRoad')
nyc = Company('New York Central')
bo = Company('Baltimore & Ohio')
erie = Company('Erie')
nynh = Company('New York & New Haven')
cp = Company('Canadian Pacific')
bm = Company('Boston & Maine')
co = Company('Chesapeake & Ohio')

