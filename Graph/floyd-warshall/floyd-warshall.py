#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This function assumes that graph is a graph represented with an adjacent matrix where
# each position has either a int value (the weight of the path) or 2**64 to describe INF. 

def floyd_warshall(graph: list[list[int]]):
    graph_size = len(graph)
    for initial in range(0,graph_size) :
        for middle in range(0,graph_size) :
            for end in range(0,graph_size) :
                graph[initial][end] = min(graph[initial][end],
                                          graph[initial][middle] + graph[middle][end])
    return graph


if __name__ == '__main__':
    inf = 2 ** 64
    current_graph =[
        [0,1,inf,inf],
        [4,0,3,inf],
        [-1,inf,0,-2],
        [inf,2,2,0]
    ]
    apsp = floyd_warshall(current_graph)
    for row in apsp:
        print(' '.join(map(str,row)))