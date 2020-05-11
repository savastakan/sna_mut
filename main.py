import collections
import math
import networkx as nx
from networkx.algorithms import approximation
import matplotlib.pylab as plt
import mutation_testing
import sna
import util
import w_method


def run(state, inp_, out, file_name):
    util.create_fsm(state, inp_, out, file_name)
    g, g_data = util.create_graph(file_name)
    input_size = int(math.pow(2, inp_))
    # output_size = int(math.pow(2, out))
    test_suite_w = w_method.run(g, g_data, input_size)

    # test_suite_sna = sna_method.run(g, g_data, input_size)
    # kill_w_ = mutation_analysis.run(g_data, test_suite_w, output_size)
    # kill_sna_ = mutation_analysis.run(g_data, test_suite_sna, output_size)
    # return kill_w_, kill_sna_
    return test_suite_w


def plot(kill_w_inputs_, kill_sna_inputs_):
    x1, y1 = zip(*kill_w_inputs_)
    plt.plot(x1, y1, label="W-Method")

    x2, y2 = zip(*kill_sna_inputs_)
    plt.plot(x2, y2, label="SNA-Method")

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.legend()
    plt.show()


state_ = 4
input_ = 4
output_ = 1
file_name = 'test.kiss2'
repeated = 5
experiment = 10

start = 2
finish = 30

betweenness = []
normal = []
degree = []
eigenvector = []
closeness = []
clustering = []

for output_ in range(start, finish):
    util.create_fsm(state_, input_, output_, file_name)
    G, g_data = util.create_graph(file_name)
    input_size = int(math.pow(2, input_))
    test_suite = w_method.run(G, g_data, input_size)
    # ---------------edges----------------------
    betweenness_centrality_edges = sna.edge_betweenness_centrality(G, 0.1)
    # sna_load_edges = sna.edge_load_centrality(G, 0.2)
    # ---------------nodes----------------------
    degree_centrality_nodes = sna.degree_centrality(G, 0.5)
    betweenness_centrality_nodes = sna.betweenness_centrality(G, 0.5)
    eigenvector_centrality_nodes = sna.eigenvector_centrality(G, 0.5)
    closeness_centrality_nodes = sna.closeness_centrality(G, 0.5)
    clustering_coefficient_nodes = sna.clustering(G, 0.5)
    # g_sna_harmonic = sna.harmonic_centrality(G, 0.4)
    # g_load_centrality = sna.load_centrality(G, 0.4)
    # g_sna_edge_square = sna.square_clustering(G, 0.4)
    # g_sna_average_neighbor_degree = sna.average_neighbor_degree(G, 0.4)
    output_size = int(math.pow(2, output_))

    kill = mutation_testing.run(G, g_data, test_suite, G.nodes(), G.edges(), input_size, output_size)
    kill_degree = mutation_testing.run(G, g_data, test_suite, degree_centrality_nodes, betweenness_centrality_edges,
                                       input_size, output_size)
    kill_betweenness = mutation_testing.run(G, g_data, test_suite, betweenness_centrality_nodes,
                                            betweenness_centrality_edges, input_size, output_size)
    kill_eigenvector = mutation_testing.run(G, g_data, test_suite, eigenvector_centrality_nodes,
                                            betweenness_centrality_edges, input_size, output_size)
    kill_closeness = mutation_testing.run(G, g_data, test_suite, closeness_centrality_nodes,
                                          betweenness_centrality_edges, input_size, output_size)
    kill_clustering = mutation_testing.run(G, g_data, test_suite, clustering_coefficient_nodes,

                                           betweenness_centrality_edges, input_size, output_size)

    result_normal = kill / (len(G.nodes()) + len(G.edges))
    print('kill: ', kill, 'nodes: ', len(G.nodes()), 'edges: ',
          len(G.edges()), 'result: ', result_normal)
    normal.append(result_normal)

    result_betweenness = kill_betweenness / (len(betweenness_centrality_nodes) + len(betweenness_centrality_edges))
    print('kill_betweenness: ', kill_betweenness, 'nodes: ', len(betweenness_centrality_nodes), 'edges: ',
          len(betweenness_centrality_edges), 'result: ', result_betweenness)
    betweenness.append(result_betweenness)

    result_degree = kill_degree / (len(degree_centrality_nodes) + len(betweenness_centrality_edges))
    print('kill_degree: ', kill_degree, 'nodes: ', len(degree_centrality_nodes), 'edges: ',
          len(betweenness_centrality_edges), 'result: ', result_degree)
    degree.append(result_degree)

    result_eigenvector = kill_eigenvector / (len(eigenvector_centrality_nodes) + len(betweenness_centrality_edges))
    print('kill_eigenvector: ', kill_eigenvector, 'nodes: ', len(eigenvector_centrality_nodes), 'edges: ',
          len(betweenness_centrality_edges), 'result:', result_eigenvector)
    eigenvector.append(result_eigenvector)

    result_closeness = kill_closeness / (len(closeness_centrality_nodes) + len(betweenness_centrality_edges))
    print('kill_closeness: ', kill_closeness, 'nodes: ', len(closeness_centrality_nodes), 'edges: ',
          len(betweenness_centrality_edges), 'result: ', result_closeness)
    closeness.append(result_closeness)

    result_clustering = kill_clustering / (len(clustering_coefficient_nodes) + len(betweenness_centrality_edges))
    print('kill_clustering: ', kill_clustering, 'nodes: ', len(clustering_coefficient_nodes), 'edges: ',
          len(betweenness_centrality_edges), 'result: ', result_clustering)
    clustering.append(result_clustering)

print('normal')
index = start
for n in normal:
    print("(", index, ",", n, ")")
    index += 1

print('betweenness')
index = start
for b in betweenness:
    print("(", index, ",", b, ")")
    index += 1

print('degree')
index = start
for d in degree:
    print("(", index, ",", d, ")")
    index += 1

print('eigenvector')
index = start
for e in eigenvector:
    print("(", index, ",", e, ")")
    index += 1

print('closeness')
index = start
for c in closeness:
    print("(", index, ",", c, ")")
    index += 1

print('clustering')
index = start
for c in clustering:
    print("(", index, ",", c, ")")
    index += 1
