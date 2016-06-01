import config
import numpy


def initialize_time():

    config.time = [0, 1, 2, 3]
    time = numpy.array(config.time, dtype=int)
    config.T = len(time) - 1
