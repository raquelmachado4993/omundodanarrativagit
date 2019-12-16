import pygraphviz as pgv

G=pgv.AGraph()
G=pgv.AGraph(strict=False,directed=True)
G=pgv.AGraph('graph {1 - 2}')
G.add_node('a')
G.add_edge('b','c')
G.graph_attr['label']='Name of graph'
G.node_attr['shape']='circle'
G.edge_attr['color']='red'
s=G.string()
G.write("file.dot")
G.draw('file.png')
G.draw('file.ps',prog='circo')


