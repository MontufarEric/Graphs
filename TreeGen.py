#Generates a random tree of size n

import nxviz as nv
import matplotlib.pyplot as plt
import numpy as np
from prim import *
from GraphToFile import*


def TreeGen(n):
    nodelist = []
    edgelist = []
    nodelist.append([str(0), {'label': float('inf')}])

    for i in range(1,n):
        nodelist.append([str(i), {'label': float('inf')}])
        j = np.random.randint(0,len(nodelist))
        if j == i:
            j = np.random.randint(0,len(nodelist))

        print(j)
        edgelist.append([str(i),str(j), {'weight': np.random.randint(1,20)}])
        #print(i ,' space ',  j)
    return(nodelist, edgelist)



(N, E) = TreeGen(10)

T = nx.Graph()
T.add_nodes_from(N)
T.add_edges_from(E)

GraphToFile(T, 'arbolprueba3.gv')