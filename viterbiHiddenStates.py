import config
import numpy


def initialize_hidden():
    config.hidden_states = [1, 2]
    config.hidden_states = numpy.array(config.hidden_states, dtype=int)
    config.nohs = len(config.hidden_states)

