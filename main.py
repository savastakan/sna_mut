import collections
import math

import matplotlib.pylab as plt
import mutation_analysis
import sna_method
import util
import w_method


def run(inp_, file_name):
    g, g_data = util.create_graph(file_name)
    input_size = int(math.pow(2, inp_))
    test_suite_w = w_method.run(g, g_data, input_size)
    test_suite_sna = sna_method.run(g, g_data, input_size)
    kill_w_ = mutation_analysis.run(g_data, test_suite_w)
    kill_sna_ = mutation_analysis.run(g_data, test_suite_sna)
    kill_w_div_test_suite = kill_w_ / len(test_suite_w)
    kill_sna_div_test_suite = kill_sna_ / len(test_suite_sna)
    return kill_w_, kill_sna_, kill_w_div_test_suite, kill_sna_div_test_suite


def plot(kill_w_inputs, kill_sna_inputs, index):
    plt.plot(index, kill_w_inputs, label="W-Method")
    plt.plot(index, kill_sna_inputs, label="SNA-Method")
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.legend()
    plt.show()


def main():
    state_ = 5
    input_ = 4
    output_ = 4
    file_name = 'test.kiss2'
    repeated = 5
    experiment = 10
    kill_w_ = []
    kill_sna_ = []
    kill_w_div_ts = []
    kill_sna_div_ts = []
    index = []

    print("state:")

    for i in range(state_, state_ + experiment):
        util.create_fsm(i, input_, output_, file_name)
        kill_w, kill_sna, kill_w_div_test_suite, kill_sna_div_test_suite = run(input_, file_name)
        kill_w_div_ts.append(kill_w_div_test_suite)
        kill_sna_div_ts.append(kill_sna_div_test_suite)
        kill_w_.append(kill_w)
        kill_sna_.append(kill_sna)
        index.append(i)
    plot(kill_w_, kill_sna_, index)
    plot(kill_w_div_ts, kill_sna_div_ts, index)

    print("input:")
    kill_w_.clear()
    kill_sna_.clear()
    kill_sna_div_ts.clear()
    kill_w_div_ts.clear()
    index.clear()
    for i in range(input_, input_ + experiment):
        util.create_fsm(state_, i, output_, file_name)
        kill_w, kill_sna, kill_w_div_test_suite, kill_sna_div_test_suite = run(input_, file_name)
        kill_w_.append(kill_w)
        kill_sna_.append(kill_sna)
        kill_w_div_ts.append(kill_w_div_test_suite)
        kill_sna_div_ts.append(kill_sna_div_test_suite)
        index.append(i)
    plot(kill_w_, kill_sna_, index)
    plot(kill_w_div_ts, kill_sna_div_ts, index)

    print("output:")
    kill_w_.clear()
    kill_sna_.clear()
    index.clear()
    kill_sna_div_ts.clear()
    kill_w_div_ts.clear()
    for i in range(output_, output_ + experiment):
        util.create_fsm(state_, input_, i, file_name)
        kill_w, kill_sna, kill_w_div_test_suite, kill_sna_div_test_suite = run(input_, file_name)
        kill_w_.append(kill_w)
        kill_sna_.append(kill_sna)
        kill_w_div_ts.append(kill_w_div_test_suite)
        kill_sna_div_ts.append(kill_sna_div_test_suite)
        index.append(i)
    plot(kill_w_, kill_sna_, index)
    plot(kill_w_div_ts, kill_sna_div_ts, index)

main()
