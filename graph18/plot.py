#!/usr/bin/python2.7

'''
This file provides utility functions specific to plotting 18xx   
graphs. Towns and cities are shaped differently and tiles can be 
colored appropriately. Note that only tiles with intersections,  
cities, or towns are worth plotting (or considering) in a graph  
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
import matplotlib.pyplot as plt
import matplotlib.colors as mpcolors
import numpy as np


class Colors():
    '''
    Colors is a container class to ease dealing with plotting colors
    '''
    y = yellow = 0
    g = green = 1
    b = brown = 2
    max_color = grey = gray = 3
colors = Colors()

def graph_18xx(G, scale=50.0):
    '''
    graph_1830(G[, scale=50.0])
    Description:
    Plots an 1830 graph of connected cities.

    Parameters:
    G - networkx graph
    scale - scale the size of nodes
    '''
    labels = dict()
    city_nodes = list()
    town_nodes = list()
    city_weights = list()
    town_weights = list()
    city_colors = list()
    town_colors = list()

    for node in G.nodes():
        labels[node] = node.value
        # it might be better to add an option to treat city
        # and town the same or treat them differently for vars.
        if node.stop_type == 'town':
            town_nodes.append(node)
            town_weights.append(node.value*scale)
            town_colors.append(node.color)
        elif node.stop_type == 'city':
            city_nodes.append(node)
            city_weights.append(node.value*scale)
            city_colors.append(node.color)
    print city_colors

    # define the y/g/b color map
    cmap = mpcolors.ListedColormap(['yellow', 'green', 'brown', 'gray'])

    # for now use a spring layout
    pos = nx.spring_layout(G)
    # plotting the nodes
    nx.draw_networkx_nodes(G, pos, nodelist=city_nodes, node_size=city_weights, node_shape='o', node_color=city_colors, 
                    cmap=cmap, vmin=0, vmax=colors.max_color)
    nx.draw_networkx_nodes(G, pos, nodelist=town_nodes, node_size=town_weights, node_shape='s', node_color=town_colors, 
                    cmap=cmap, vmin=0, vmax=colors.max_color)
    # label the nodes with city/town value
    nx.draw_networkx_labels(G, pos, labels)
    # plotting the edges
    nx.draw_networkx_edges(G, pos)

    plt.show()

