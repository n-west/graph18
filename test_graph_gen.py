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
    '''
    basically just test all of the features
    '''

    two_train = graph18.Train(2)
    two_plus_train = graph18.Train(2)
    three_train = graph18.Train(3)
    three_plus_train = graph18.Train(3)

    prr = graph18.Company('Pennsylvannia RailRoad', [two_train])
    nyc = graph18.Company('New York Central', [two_train, two_train])
    bo = graph18.Company('Baltimore & Ohio', [two_train])
    nynh = graph18.nynh

    bo.add_train(three_train)
    nynh.add_train(two_train)


    G = graph18.Graph()
    nodes = dict()
    nodes['a'] = graph18.City(pos=(0,0), value=10, color=graph18.colors.y, stop_type='city', capacity=1)
    nodes['b'] = graph18.City(pos=(0,1), value=30, color=graph18.colors.y, stop_type='city', capacity=1, owners=[prr])
    nodes['c'] = graph18.City(pos=(0,2), value=20, color=graph18.colors.g, stop_type='city', capacity=1, owners=[bo])
    nodes['d'] = graph18.City(pos=(0,3), value=10, color=graph18.colors.y, stop_type='town', capacity=1)
    nodes['e'] = graph18.City(pos=(2,1), value=20, color=graph18.colors.b, stop_type='city', capacity=1, owners=[nynh])
    nodes['f'] = graph18.City(pos=(2,2), value=10, color=graph18.colors.y, stop_type='town', capacity=1)
    nodes['g'] = graph18.City(pos=(2,3), value=40, color=graph18.colors.y, stop_type='city', capacity=2)

    G.add_rail(nodes['a'], nodes['b'])
    G.add_rail(nodes['b'], nodes['b'])
    G.add_rail(nodes['a'], nodes['c'])
    G.add_rail(nodes['a'], nodes['d'])
    G.add_rail(nodes['e'], nodes['f'])
    G.add_rail(nodes['d'], nodes['g'])
    G.add_rail(nodes['e'], nodes['g'])
    G.add_rail(nodes['d'], nodes['b'])
    G.add_rail(nodes['c'], nodes['e'])

    graph18.graph_18xx(G)

    bo.get_perspective(G)
    graph18.graph_18xx(bo.graph_perspective)

    bo.get_perspective(G, True)
    graph18.graph_18xx(bo.graph_perspective)


if __name__ == '__main__':
    main()
    #try:
    #    main()
    #except KeyboardInterrupt as e:
    #    raise e

