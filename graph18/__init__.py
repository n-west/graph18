#!/usr/bin/python2.7

'''
This is the graph18 package. The intention is to aid in working with graphs
that arise from the game series 18xx. Currently there's utilities for 
generating nodes that are cities or towns and the ability to plot with matching
hex colors.
'''

# Copyright 2014 Nathan West
# This file is part of 18graph.
# 
# 18graph is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# 18graph is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with 18graph.  If not, see <http://www.gnu.org/licenses/>.

from plot import graph_18xx, colors
from graph import Cities
from networkx import Graph


