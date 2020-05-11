import collections

import networkx as nx
import util
import w_method


def get_important_nodes(g):
    important_nodes = []

    degree_centrality = nx.degree_centrality(g)
    closeness_centrality = nx.closeness_centrality(g)
    betweenness_centrality = nx.betweenness_centrality(g)

    # katz_centrality = nx.katz_centrality(g)

    # pagerank = nx.pagerank(g)
    # load_centrality = nx.load_centrality(g)
    # clustering = nx.clustering(g)
    # local_reaching_centrality = nx.local_reaching_centrality(g, 'START')

    # ("strongly_connected_components: ", [c for c in nx.strongly_connected_components(g)])
    # print("local_reaching_centrality for START: ", local_reaching_centrality)
    # print("clustering: ", clustering)
    # print("load_centrality: ", load_centrality)
    # print("pagerank: ", pagerank)
    # print("degree_centrality: ", degree_centrality)
    # print("katz_centrality: ", katz_centrality)
    # print("closeness_centrality: ", closeness_centrality)
    # print("betweenness_centrality: ", betweenness_centrality)
    # print("local_reaching_centrality: ", local_reaching_centrality)

    threshold_degree = sum(degree_centrality.values()) / len(degree_centrality)
    threshold_closeness = sum(closeness_centrality.values()) / len(closeness_centrality)
    threshold_betweenness = sum(betweenness_centrality.values()) / len(betweenness_centrality)
    # threshold_katz = sum(katz_centrality.values()) / len(katz_centrality)

    # important_nodes.extend([state for state, katz_centrality in katz_centrality.items() if
    #                        (katz_centrality >= threshold_katz) & (state != 'START')])

    important_nodes.extend([state for state, betweenness_centrality in betweenness_centrality.items() if
                            (betweenness_centrality >= threshold_betweenness) & (state != 'START')])

    important_nodes.extend([state for state, closeness_centrality in closeness_centrality.items() if
                            (closeness_centrality >= threshold_closeness) & (state != 'START')])

    important_nodes.extend([state for state, degree_centrality in degree_centrality.items() if
                            (degree_centrality >= threshold_degree) & (state != 'START')])
    return important_nodes


def run(g, g_data, input_size):
    # index = 0
    # mapping = collections.OrderedDict()
    # for node in g.nodes:
    #    mapping[index] = node
    #    index += 1

    # input_matrix = nx.attr_matrix(g, edge_attr='input', rc_order=g.nodes())
    # g_input = nx.relabel_nodes(nx.from_numpy_matrix(input_matrix), mapping)

    # output_matrix = nx.attr_matrix(g, edge_attr='output', rc_order=g.nodes())
    # g_output = nx.relabel_nodes(nx.from_numpy_matrix(output_matrix), mapping)

    important_nodes = get_important_nodes(g)
    # important_nodes.extend(get_important_nodes(g_input))
    # important_nodes.extend(get_important_nodes(g_output))
    important_nodes = list(dict.fromkeys(important_nodes))
    print("important_nodes: ", important_nodes)

    tcs_paths = []
    for important_node in important_nodes:
        # path = [p for p in nx.all_simple_paths(g, source='START', target=important_node)]
        # path = [p for p in nx.all_shortest_paths(g, source='START', target=important_node)]
        path = nx.shortest_path(g, source='START', target=important_node)
        tcs_paths.append(path)
    print("tcs_paths_sna: ", tcs_paths)

    # print("tcs_sna_paths: ", tcs_paths)
    w_set = w_method.get_w_set(g_data, input_size)
    tcs_sna = w_method.get_tcs(g, tcs_paths)
    return w_method.mul(tcs_sna, w_set)


def run2(g):
    if nx.is_strongly_connected(g):
        betweenness_centrality = nx.betweenness_centrality(g)
        min(betweenness_centrality, key=betweenness_centrality.get)


