import collections
import math
import subprocess

import networkx as nx


def create_graph(output_file):
    g = nx.DiGraph()
    g_data = collections.defaultdict(dict)
    input_file = open(output_file, "r")
    for line in input_file:
        if not line.startswith("."):
            parts = line.split()
            input_value = int(parts[0], 2)
            output_value = int(parts[3], 2)
            g.add_edge(parts[1], parts[2], input=input_value, output=output_value)
            g_data[parts[1]][input_value] = {'next_state': parts[2], 'output': output_value}
    input_file.close()
    return g, g_data


def create_fsm(state_size=5, input_=1, output_=1, output_file='test.kiss2'):
    transition_size = state_size * math.pow(2, input_)
    subprocess.run(["genstate.exe", "-i", str(input_), "-o", str(output_), "-t", str(transition_size), "-s",
                    str(state_size),
                    output_file])
