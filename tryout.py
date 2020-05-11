import util
import networkx as nx
from networkx.algorithms import approximation
from networkx.algorithms import connectivity
state_ = 15
input_ = 4
output_ = 1
file_name = 'test.kiss2'
repeated = 5
experiment = 10

util.create_fsm(state_, input_, output_, file_name)
G, g_data = util.create_graph(file_name)

print(nx.average_neighbor_degree(G))
print(approximation.max_clique(G))
print(nx.k_nearest_neighbors(G))
print(nx.min_edge_cover(G))