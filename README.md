
Graph18
======


    "No one can earn a million dollars honestly" 
         William Jennings Bryan


    I don't care half so much about making money as I do about making my
    point , and coming out ahead.
        Cornelius Vanderbilt

This will eventually be a route calculator for 18xx games. It provides
and interface to create graphs of 18xx cities that can be plotted (via
networkx and matplotlib) from a graph theoretic perspective.

An example:

A graph representing a (simple) 1830 board.

![Generic graph plotted with networkx](https://github.com/n-west/graph18/blob/master/resources/graph_generic.png "Generic 18xx Graph")

From the broad perspective of a hypothetical B&O the entire graph view changes

![Generic graph with perspective](https://github.com/n-west/graph18/blob/master/resources/graph_perspective.png "Generic 18xx Graph with perspective")

From that broad perspective we can make a subgraph for the B&O with endpoints where tokens make a hard stop.

![Broad perspective subgraph](https://github.com/n-west/graph18/blob/master/resources/subgraph_broad_perspective.png "Generic 18xx SubGraph with broad perspective")

Alternatively we can have a narrow perspective which limits the end-points to nodes we can reach with our current trains (a 2-train in this example).

![Narrow perspective subgraph](https://raw.githubusercontent.com/n-west/graph18/master/resources/subgraph_narrow_perspective.png "Generic 18xx SubGraph with narrow perspective")
