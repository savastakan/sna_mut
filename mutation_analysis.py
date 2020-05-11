
def check(g_data, test_suite, selected_node, selected_input):
    for test_case in test_suite:
        node = 'START'
        for input_ in test_case:
            if node == selected_node:
                if input_ == selected_input:
                    return True
            node = g_data[node][input_]['next_state']
    return False


def run(g_data, test_suite):
    kill = 0
    for node in list(g_data.keys()):
        for input_ in list(g_data[node].keys()):
            if check(g_data, test_suite, node, input_):
                kill += 1
    return kill
