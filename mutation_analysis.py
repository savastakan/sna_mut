import copy
import random


def get_output(Gm, test_suite):
    outputs = []
    for test_case in test_suite:
        state = 'START'
        for input_v in test_case:
            if input_v in Gm[state]:
                outputs.append(Gm[state][input_v]['output'])
            else:
                return outputs
            state = Gm[state][input_v]['next_state']
    return outputs


def check(g_mutant, g_data, test_suite, kill):
    if get_output(g_mutant, test_suite) != get_output(g_data, test_suite):
        kill += 1
    return kill


def run(g_data, test_suite, output_size):
    kill = 0
    for node in list(g_data.keys()):
        g_mutant1 = copy.deepcopy(g_data)
        del g_mutant1[node]
        kill = check(g_mutant1, g_data, test_suite, kill)
        del g_mutant1

        for input_value in list(g_data[node].keys()):
            g_mutant2 = copy.deepcopy(g_data)
            del g_mutant2[node][input_value]
            kill = check(g_mutant2, g_data, test_suite, kill)
            del g_mutant2

            g_mutant3 = copy.deepcopy(g_data)
            g_mutant3[node][input_value]['output'] = random.randrange(output_size)
            kill = check(g_mutant3, g_data, test_suite, kill)
            del g_mutant3

            g_mutant4 = copy.deepcopy(g_data)
            next_state = random.choice(list(g_mutant4.keys()))
            g_mutant4[node][input_value]['next_state'] = next_state
            kill = check(g_mutant4, g_data, test_suite, kill)
            del g_mutant4
    return kill

