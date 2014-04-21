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

# Note: a standard 1830 train actually could be inherited from
# the plus-train in variants, but that feels weird to do so
# instead each train type will just have its own class.
# The most important thing in train classes is the route searches

import networkx as nx

class Train(object):
    '''
    Base Train class that follows standard 1830 rules
    '''
    def __init__(self, capacity):
        '''
        Train(capacity)

        Define a train based on how many towns and cities
        it can be run through. This follows the standard
        1830 ruleset 

        Parameters:
            capacity -  cities and towns that can be run through
        '''
        self.capacity = capacity

    def dfs_accessible_nodes(self, graph, start, capacity):
        '''
        A recursive depth-first search of a graph for a sub-graph 
        that this train can traverse.

        Parameters:
            graph - the graph being searched for routes
            start - the starting node of the search

        Note:
            For high depths this will use lots of memory because
            each iteration makes its own copy of the graph (although
            graphs shrink for each depth). If that becomes an issue
            we can remove disjoint sections on each iteration
        '''
        neighbors = graph.neighbors(start)
        accessible_nodes = [start] + neighbors
        ng = graph.copy()
        ng.remove_node(start)
        for neighbor in neighbors:
          # if it's possible to go through this city/town then continue
          # traversing the depth
          if capacity > 1 and \
                 (neighbor.capacity - neighbor.owners.__len__() > 0 or \
                 neighbor.owners[0] == null_company):
            accessible_nodes += self.dfs_accessible_nodes(ng, neighbor, capacity-1)

        return accessible_nodes


class PlusTrain(object):
    def __init__(self, capacity):
        '''
        Train(capacity)

        Define a plus train based on how many towns and cities
        it can be run through. This follows the rulset where
        an n+n train can run through n cities and n towns
        which appears in many 1830 variants.

        Parameters:
            capacity - cities and towns that can be run through

        Note:
            This does not follow the 18oe plus-style train that
            can pass through any towns it wishes.
        '''
        self.city_capacity = capacity
        self.town_capacity = capacity
       

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


    def get_perspective(self, graph, narrow=False):
        '''
        Return and store a sub-graph from the perspective of given
        company perspective(company[, narrow=False])

        The graph from the perspective of the company will stop at
        nodes the company cannot cross due to tokens blocking them.
        If narrow is true then the perspective ends on nodes that
        the company cannot reach if an owned train cannot go that 
        far.

        This will work by
         1. Creating a list of nodes where we have tokens
         2. With the best trains find accessible nodes
         3. Return a subgraph based on list of accesible nodes
        '''
        # Step 1
        my_graph = graph.copy()
        token_nodes = [n for n in my_graph.nodes() if n.owners.__contains__(self)]

        # Step 2
        if narrow:
            best_train = Train(0)
            for train in self.trains:
                if train.capacity > best_train.capacity:
                    best_train = train
            print "best train has capacity %i" % best_train.capacity
            train_dfs = lambda start: best_train.dfs_accessible_nodes(my_graph, start, best_train.capacity-1)
            accessible_nodes = map(train_dfs, token_nodes)
        else:
            imag_train = Train(9999)
            train_dfs = lambda start: imag_train.dfs_accessible_nodes(my_graph, start, 9999)
            accessible_nodes = map(train_dfs, token_nodes)

        # Step 3
        self.graph_perspective = my_graph.subgraph(accessible_nodes[0])
        return accessible_nodes[0]

    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return self.name == other.name
        
        
null_company = Company('null')
prr = Company('Pennsylvannia RailRoad')
nyc = Company('New York Central')
bo = Company('Baltimore & Ohio')
erie = Company('Erie')
nynh = Company('New York & New Haven')
cp = Company('Canadian Pacific')
bm = Company('Boston & Maine')
co = Company('Chesapeake & Ohio')

