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

from companies import null_company

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mpcolors
import numpy as np
import textwrap


class Colors():
    '''
    Colors is a container class to ease dealing with plotting colors
    '''
    y = yellow = 0
    g = green = 3
    b = brown = 6
    grey = gray = 9
    max_color = 10
colors = Colors()

def draw_18xx(G, company=null_company, node_list=[], title='', scale=50.0):
    '''
    draw_1830(G[, scale=50.0])
    Description:
    Plots an 1830 graph of connected cities. Nodes are
    colored yellow/green/brown/gray based on their corresponding
    game color. The shade/highlighting can be altered by giving
    a node_list. More shading can be given by providing a Company
    such that the nodes with a token of that company are further
    highlighted. This allows a good game view from the perspective
    of that company.

    Parameters:
    G - networkx graph
    company - a Company instance. The nodes with tokens 
                of this company are highlighted
    node_list - list of nodes to be highlighted
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
        color_val = node.color
        if node.stop_type == 'town':
            town_nodes.append(node)
            town_weights.append(node.value*scale)
            if node_list.__contains__(node):
                color_val += 1
            town_colors.append(color_val)
        elif node.stop_type == 'city':
            city_nodes.append(node)
            city_weights.append(node.value*scale)
            if node_list.__contains__(node):
                color_val += 1
            if node.owners.__contains__(company) and company != null_company:
                color_val += 1
            city_colors.append(color_val)

    # define the y/g/b color map
    #cmap = mpcolors.ListedColormap(['yellow', 'green', 'brown', 'gray'])
    #                                 light    regular    dark
    cmap = mpcolors.ListedColormap(['#FFFFB2','#FFFF00','#AAAA00',  # yellow
                                    '#99FF99','#00FF00','#008000',  # green
                                    '#A38566','#855C33','#663300',  # brown
                                    '#B2B2B2','#808080','#4C4C4C']) # gray

    # for now use a spring layout
    pos = nx.spring_layout(G)
    # plotting the nodes
    nx.draw_networkx_nodes(G, pos, nodelist=city_nodes, node_size=city_weights, node_shape='o', node_color=city_colors, 
                    cmap=cmap, vmin=0, vmax=12)
    nx.draw_networkx_nodes(G, pos, nodelist=town_nodes, node_size=town_weights, node_shape='s', node_color=town_colors, 
                    cmap=cmap, vmin=0, vmax=12)
    # label the nodes with city/town value
    nx.draw_networkx_labels(G, pos, labels)
    # plotting the edges
    nx.draw_networkx_edges(G, pos)

    wrapped_title = textwrap.wrap(title, 45)
    formatted_title = '\n'.join(wrapped_title)
    plt.title(formatted_title)
    if node_list != [] and company != null_company:
        cb = plt.colorbar()
        cb.set_ticks(np.arange(0.5,12.5,1))
        cb.ax.set_yticklabels(['not reachable', 'reachable', 'token']*4)

    plt.show()

