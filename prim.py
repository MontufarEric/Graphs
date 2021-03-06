# Prim Algorithm using networkx

import networkx as nx


from pqdict import PQDict

def prim(G,start):
    """Function recives a graph and a starting node, and returns a MST"""
    stopN = G.number_of_nodes() - 1
    current = start
    closedSet = set()
    pq = PQDict(reverse = True)
    mst = []

    while len(mst) < stopN:
        # print " "
        # print "Current node :", current
        for node in G.neighbors(current):
            if node not in closedSet and current not in closedSet:
                # print "    neigbors: ", node
                if (current,node) not in pq and (node,current) not in pq:
                    w = G[current][node]['weight']

                    pq.additem((current,node), w)

        closedSet.add(current)

        tup, wght = pq.popitem()
        while(tup[1] in closedSet):
            tup, wght = pq.popitem()
        tup = (tup[0], tup[1], {'weight': wght})
        mst.append(tup)
        current = tup[1]

    return mst
    # pass
