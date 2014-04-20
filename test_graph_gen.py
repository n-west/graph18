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

#######################################################################
#                             README                                  #
#                             ######                                  #
# This file is QA for the python module graph18. It's used as an      #
# interactive test of graph generation and plotting. It can also be   #
# used as a reference for using the library.                          #
#######################################################################

import graph18

def main():
    G = generate_graph()
    graph18.graph_18xx(G)


def generate_graph():
    '''
    This is just an example usage that generates a graph
    '''

    two_train = graph18.Train(2)
    two_plus_train = graph18.Train(0,2,2)
    three_train = graph18.Train(3)
    three_plus_train = graph18.Train(0,3,3)

    prr = graph18.Company('Pennsylvannia RailRoad', [two_train])
    nyc = graph18.Company('New York Central', [two_plus_train, two_train])
    bo = graph18.Company('Baltimore & Ohio')
    nynh = graph18.nynh

    bo.add_train(three_train)
    nynh.add_train(two_train)


    G = graph18.Graph()
    nodes = dict()
    nodes['a'] = graph18.City(value=10, color=graph18.colors.y, stop_type='city', capacity=1)
    nodes['b'] = graph18.City(value=30, color=graph18.colors.y, stop_type='city', capacity=1, owners=[prr])
    nodes['c'] = graph18.City(value=20, color=graph18.colors.g, stop_type='city', capacity=1, owners=[bo])
    nodes['d'] = graph18.City(value=10, color=graph18.colors.y, stop_type='town', capacity=1)
    nodes['e'] = graph18.City(value=20, color=graph18.colors.y, stop_type='city', capacity=1, owners=[nyc])
    nodes['f'] = graph18.City(value=10, color=graph18.colors.y, stop_type='town', capacity=1)
    nodes['g'] = graph18.City(value=40, color=graph18.colors.y, stop_type='city', capacity=2)

    G.add_rail(nodes['a'], nodes['b'])
    G.add_rail(nodes['b'], nodes['b'])
    G.add_rail(nodes['a'], nodes['c'])
    G.add_rail(nodes['a'], nodes['d'])
    G.add_rail(nodes['e'], nodes['f'])
    G.add_rail(nodes['d'], nodes['g'])
    G.add_rail(nodes['e'], nodes['g'])
    G.add_rail(nodes['d'], nodes['b'])
    G.add_rail(nodes['c'], nodes['e'])
    return G


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        raise "User halted"

