import copy
import random


def get_output(G, test_case):
    outputs = []
    state = 'START'
    for input_v in test_case:
        if input_v in G[state]:
            outputs.append(G[state][input_v]['output'])
        else:
            return outputs
        state = G[state][input_v]['next_state']
    return outputs


def check(g_mutant, g_data, test_suite, kill):
    for test_case in test_suite:
        if get_output(g_mutant, test_case) != get_output(g_data, test_case):
            kill += 1
    return kill


def process_node(G, g_data, test_suite, important_nodes):
    kill = 0
    for node in important_nodes:
        g_mutant1 = copy.deepcopy(g_data)
        del g_mutant1[node]
        kill = check(g_mutant1, g_data, test_suite, kill)
        del g_mutant1
    return kill


def process_edge(G, g_data, test_suite, important_edges, input_size, output_size):
    kill = 0

    for node1, node2 in important_edges:
        # Missing of Transition(MOT)
        g_mutant2 = copy.deepcopy(g_data)
        del g_mutant2[node1][G.edges[node1, node2]['input']]
        kill = check(g_mutant2, g_data, test_suite, kill)
        del g_mutant2

        # Change of Output (COO)
        g_mutant3 = copy.deepcopy(g_data)
        g_mutant3[node1][G.edges[node1, node2]['input']]['output'] = random.randrange(output_size)
        kill = check(g_mutant3, g_data, test_suite, kill)
        del g_mutant3

        # Change of Input(COI)
        g_mutant4 = copy.deepcopy(g_data)
        g_mutant4[node1][random.randrange(input_size)] = {'next_state': node2,
                                                          'output': g_data[node1][G.edges[node1, node2]['input']][
                                                              'output']}
        kill = check(g_mutant4, g_data, test_suite, kill)
        del g_mutant4
        #
        # Change of Next State (CONS)
        g_mutant5 = copy.deepcopy(g_data)
        next_state = random.choice(list(G.nodes()))
        g_mutant5[node1][G.edges[node1, node2]['input']]['next_state'] = next_state
        kill = check(g_mutant5, g_data, test_suite, kill)
        del g_mutant5

    return kill


def run_edge(G, g_data, test_suite, important_edges, input_size, output_size):
    return process_edge(G, g_data, test_suite, important_edges, input_size, output_size)


def run_node(G, g_data, test_suite, important_nodes):
    return process_node(G, g_data, test_suite, important_nodes)


def run(G, g_data, test_suite, important_nodes, important_edges, input_size, output_size):
    kill = 0
    kill += process_edge(G, g_data, test_suite, important_edges, input_size, output_size)
    kill += process_node(G, g_data, test_suite, important_nodes)
    return kill
