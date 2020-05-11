import itertools
import math

import networkx as nx
import util


def get_path(g_tree, labels):
    paths_without_labels = nx.shortest_path(g_tree, source=0)
    tcs_paths = []
    for path in paths_without_labels.values():
        p = []
        for state in path:
            p.append(labels[state])
        tcs_paths.append(p)
    return tcs_paths


def mul(tcs, wSet):
    test_suite = list()
    for tcs_tmp in tcs:
        for w_tmp in wSet:
            test_suite.append(tcs_tmp + w_tmp)
    return test_suite


def get_w_set(g_data, input_size):
    result = dict()
    g_remains = nx.DiGraph()
    for pair in itertools.combinations(g_data.keys(), 2):
        if pair[0] != pair[1]:
            for input_val in range(input_size):
                output1 = g_data[pair[0]][input_val]['output']
                output2 = g_data[pair[1]][input_val]['output']
                if output1 != output2:
                    result[frozenset(pair)] = [input_val]
                    break
            if frozenset(pair) not in result:
                for input_val in reversed(range(input_size)):
                    next_state1 = g_data[pair[0]][input_val]['next_state']
                    next_state2 = g_data[pair[1]][input_val]['next_state']
                    if next_state1 != next_state2:
                        g_remains.add_edge(frozenset(pair), frozenset({next_state1, next_state2}), input=input_val)
    sources = []
    targets = []
    for state in g_remains.nodes:
        if not g_remains.in_degree(state):
            sources.append(state)
        if state in result.keys():
            targets.append(state)
    all_paths_ = []
    for source in sources:
        for target in targets:
            if nx.has_path(g_remains, source, target):
                all_paths_.append(nx.shortest_path(g_remains, source=source, target=target))
    for path_ in all_paths_:
        pair1 = path_.pop(-1)
        values = result[pair1].copy()
        for pair2 in reversed(path_):
            values.append(g_remains[pair2][pair1]['input'])
            result[pair2] = list(reversed(values.copy()))
            pair1 = pair2
    tmp = set(tuple(test_case) for test_case in result.values() if test_case)
    return [list(x) for x in tmp]


def get_tcs(g, tcs_paths):
    tcs = list()
    for tcs_path in tcs_paths:
        temp = []
        node1 = tcs_path.pop(0)
        while tcs_path:
            node2 = tcs_path.pop(0)
            temp.append(int(g[node1][node2]['input']))
            node1 = node2
        tcs.append(temp)
    return tcs


def get_tree(g):
    g_tree = nx.DiGraph()
    labels = dict()
    index = 0
    labels[index] = "START"
    g_tree.add_node(index, label="START")
    stack = [index]
    while stack:
        state_index = stack.pop()
        for neighbour in g[labels[state_index]]:
            index += 1
            if neighbour not in labels.values():
                stack.append(index)
            labels[index] = neighbour
            g_tree.add_node(index, label=neighbour)
            g_tree.add_edge(state_index, index)
    return g_tree, labels


def run(g, g_data, input_size):
    w_set = get_w_set(g_data, input_size)
    g_tree, labels = get_tree(g)
    tcs_paths = get_path(g_tree, labels)
    print("tcs_paths: ", tcs_paths)
    tcs_w = get_tcs(g, tcs_paths)
    return mul(tcs_w, w_set)
