import networkx as nx


def remove_node(G, values, scale):
    selectedList = []
    size = int(len(values) * scale)
    sorted_d = sorted(values.items(), key=lambda x: x[1], reverse=True)
    for i in range(size):
        selectedList.append(sorted_d[i][0])
    return selectedList


def remove_transition(G, values, scale):
    selectedList = []
    size = int(len(values) * scale)
    sorted_d = sorted(values.items(), key=lambda x: x[1], reverse=True)
    for i in range(size):
        selectedList.append(sorted_d[i][0])
    return selectedList


def edge_betweenness_centrality(G, scale):
    return remove_transition(G, nx.edge_betweenness_centrality(G), scale)


def betweenness_centrality(G, scale):
    return remove_node(G, nx.betweenness_centrality(G), scale)


def degree_centrality(G, scale):
    return remove_node(G, nx.degree_centrality(G), scale)


def eigenvector_centrality(G, scale):
    return remove_node(G, nx.eigenvector_centrality(G), scale)


def closeness_centrality(G, scale):
    return remove_node(G, nx.closeness_centrality(G), scale)


def clustering(G, scale):
    return remove_node(G, nx.clustering(G), scale)


def load_centrality(G, scale):
    return remove_node(G, nx.load_centrality(G), scale)


def harmonic_centrality(G, scale):
    return remove_node(G, nx.harmonic_centrality(G), scale)


def square_clustering(G, scale):
    return remove_node(G, nx.square_clustering(G), scale)


def average_neighbor_degree(G, scale):
    return remove_node(G, nx.average_neighbor_degree(G), scale)


def degree_centrality(G, scale):
    return remove_node(G, nx.degree_centrality(G), scale)


def edge_load_centrality(G, scale):
    return remove_transition(G, nx.edge_load_centrality(G), scale)
