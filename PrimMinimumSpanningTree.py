#!/usr/bin/env python3

from collections import defaultdict
import sys
import time

def load_data(file_name):
    #Read in the edge data.

    f = open(file_name,'r')
    vertex_count, edge_count = f.readline().strip().split()
    vertex_count, edge_count = int(vertex_count), int(edge_count)
    
    edges = defaultdict(list)
    for _ in range(edge_count):
        t, h, w = f.readline().strip().split() #tail, head and weight are identified
        t, h, w = int(t)-1, int(h)-1, int(w)
        edges[t].append((h,w))
        edges[h].append((t,w))
    f.close()
    return edges, edge_count, vertex_count

def run_Prim(edges, edge_count, vertex_count):
    #Use Prim's greedy algorithm, starting from a random node, to compute the minimum spanning tree.

    #edges is a dictionary which associates each tail with a tuple of head and weight
    #vs is a set of visited nodes

    vs = set()
    vs.add(0)

    total_cost = 0
    while len(vs) < vertex_count:
        min_weight = sys.maxsize
        min_node = None
        for node in vs:
            for edge in edges[node]:
                if (edge[1]<min_weight) and (edge[0] not in vs):
                    min_node = edge[0]
                    min_weight = edge[1]
        vs.add(min_node)
        total_cost += min_weight
    return total_cost


if __name__ == "__main__":
    start = time.time()
    file_name =  'primdata.txt'
    edges, edge_count, vertex_count = load_data(file_name)

    total_cost = run_Prim(edges, edge_count, vertex_count)
    print(total_cost)
    
    end = time.time()
    print(end - start)

