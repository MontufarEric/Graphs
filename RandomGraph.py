import networkx as nx
import nxviz as nv
import matplotlib.pyplot as plt
import numpy as np
from prim import *

"""
generador de grafos aleatorios empleando el metodo de Erdos y Renyi, donde n es el numero de nodos del grafo y p
la probabilidad de generar un enlace. 

Descomentar bloque de codigo y la linea nodelist , edgelist = randGraphGen(10, 0.25) de abajo para implementar prim en 
un grafo a aleatorio
"""


# def randGraphGen(n,p):
#
#     nodelist = []
#     edgelist = []
#
#     for i in range(n):
#         nodelist.append([str(i), {'label': float('inf')}])
#
#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 r = np.random.rand()
#                 if p >= r:
#                     edgelist.append([str(i), str(j), {'weigth': np.random.randint(1, 20)}])
#
#     return(nodelist,edgelist)
#
#
# nodelist, edgelist = randGraphGen(10, 0.25)


"""
Comentar el bloque de codigo de abajo si se desea probar el algoritmo con un grafo aleatorio. 
"""

nodelist = [('1', {'label': 'inf'}),
            ('2', {'label': 'inf'}),
            ('3', {'label': 'inf'}),
            ('4', {'label': 'inf'}),
            ('5', {'label': 'inf'}),
            ('6', {'label': 'inf'})
            ]
edgelist = [('1', '2', {'weight': 0.1}),
             ('1', '3', {'weight': 0.2}),
             ('2', '4', {'weight': 0.6}),
             ('3', '4', {'weight': 0.7}),
             ('5', '4', {'weight': 0.8}),
             ('5', '6', {'weight': 1.0}),
             ('5', '1', {'weight': 1.3}),
             ('6', '4', {'weight': 1.1}),
             ]

"""
Llamado al algoritmo de prim y graficado de los grafos
"""

#nodelist , edgelist = randGraphGen(10, 0.25)


G = nx.Graph()
G.add_nodes_from(nodelist)
G.add_edges_from(edgelist)

mst = prim(G,'1')



T = nx.Graph()
T.add_edges_from(mst)
print(T.edges(data=True))

p = nv.MatrixPlot(T)
p.cmap = plt.cm.get_cmap('Greens')

p.draw()
plt.show()

