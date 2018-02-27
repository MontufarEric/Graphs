import networkx as nx

def GraphToFile(G, filename):
    nx.Graph(G)
    saveFile = open(filename, 'w')
    txt = 'graph Prim_1 {'
    saveFile.write(txt)
    [saveFile.write('\n' + u + '--' + v + ' [Label = "' + str(G[u][v]['weight']) + '"];') for u, v, d in
     G.edges(data=True)]
    saveFile.write('\n }')
    saveFile.close()