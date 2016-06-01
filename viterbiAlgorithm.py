import config
import numpy


def viterbi_initialization():

    config.viterbi_probability = numpy.zeros((config.nohs + 2, config.T + 1))
    config.backtrace = numpy.zeros((config.nohs + 2, config.T + 1), dtype=int)

    ###########################
    # Initialization step
    for j in config.hidden_states:
        config.viterbi_probability[j][1] = config.A[0][j] * config.B[config.observations_vocab_index[1]][j]
        # redundant since we already initialized all elements of backtrace matrix to 0,
        # We write this assignment for the sake of completeness
        config.backtrace[j][1] = 0


def viterbi_recursion():
    ###########################
    # Recursion step
    vi = [0] * (config.nohs + 1)
    for t in config.time[2:]:
        for j in config.hidden_states:
            for i in config.hidden_states:
                vi[i] = config.viterbi_probability[i][t - 1] * config.A[i][j] * \
                        config.B[config.observations_vocab_index[t]][j]
            config.viterbi_probability[j][t] = max(vi)
            config.backtrace[j][t] = vi.index(config.viterbi_probability[j][t])

    # Termination Step
    for i in config.hidden_states:
        vi[i] = config.viterbi_probability[i][config.T] * config.A[i][-1]
    config.pstar = max(vi)
    config.qTstar = vi.index(max(vi))

    print("the Viterbi Matrix is \n")
    print(config.viterbi_probability), print("\n")
    print("the Backtrace Matrix is \n")
    print(config.backtrace), print("\n")

    # Set last element of bt and follow backtrace
    bt = numpy.zeros(config.T, dtype=int)
    bt[-1] = config.qTstar
    for t in range(config.T - 1, 0, -1):
        bt[t - 1] = config.backtrace[bt[t]][t + 1]
    print("the backtrace for hidden states is \n")
    print(bt)