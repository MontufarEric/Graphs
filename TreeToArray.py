
import nxviz as nv
import matplotlib.pyplot as plt
import numpy as np
from prim import *
from GraphToFile import*

nodelist = [('1', {'label': 'inf'}),
            ('2', {'label': 'inf'}),
            ('3', {'label': 'inf'}),
            ('4', {'label': 'inf'}),
            ('5', {'label': 'inf'}),
            ('6', {'label': 'inf'}),
            ('7', {'label': 'inf'}),
            ('8', {'label': 'inf'}),
            ]
edgelist =  [('1', '2', {'weight': 0.1}),
             ('1', '3', {'weight': 0.2}),
             ('3', '5', {'weight': 0.6}),
             ('3', '4', {'weight': 0.8}),
             ('4', '6', {'weight': 1.0}),
             ('4', '7', {'weight': 1.0}),
             ('4', '8', {'weight': 1.0}),
             ]

Tree = nx.Graph()
Tree.add_nodes_from(nodelist)
Tree.add_edges_from(edgelist)

GraphToFile(Tree,'arbol original 1.gv')
S=[]
T = Tree.copy();

#######################################################################################################################
def treeToArray(T,n1,S):
    if (len(S)== len(Tree.nodes)-2):
        return S
    else:
        try:
            if (len(T.adj[n1])==1):
                x = sorted(list(T.adj[n1]))
                S.append(x[0])
                T.remove_node(n1)
                n1= '1'
                return treeToArray(T,n1,S)

            else:
                n1 = str(int(n1)+1)
                return treeToArray(T, n1, S)
        except KeyError:
            n1 = str(int(n1) + 1)
            return treeToArray(T, n1, S)



###########################################################################################################################
S= treeToArray(T,'1',S)
print("S= ",S)


def ArrayToTree(S):

    I= [n+1 for n in range(len(S)+2)]
    listEdges = []
    while(len(S) != 0):

        for n in I:
            flag = n in S
            if(flag == False):
                ind = I.index(n)
                listEdges.append([str(S[0]), str(n), {'weight': 0}])
                del I[ind]
                del S[0]
                break

    listEdges.append([str(I[0]),str(I[1]), {'weight': 0}])
    return(listEdges)

####################################################################################################################


list= ArrayToTree(S)

Ntree = nx.Graph()
Ntree.add_edges_from(list)

GraphToFile(Ntree,'arbol recuperado 1.gv')
print("I= ",Ntree.nodes)
print("Edges= ",Tree.edges)
