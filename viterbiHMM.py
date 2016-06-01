import config
import numpy


def initialize_ab():

    config.A = numpy.zeros((config.nohs + 2, config.nohs + 2))
    config.A[0][:] = [0.0, 0.8, 0.2, 0.0]
    config.A[1][:] = [0.0, 0.7, 0.3, 0.5]
    config.A[2][:] = [0.0, 0.4, 0.6, 0.5]
    config.A[3][:] = [0.0, 0.0, 0.0, 1.0]

    config.B = numpy.zeros((config.noov, config.nohs + 1))
    B0 = numpy.zeros((config.noov, 1))
    BS1 = numpy.reshape(numpy.array([0.2, 0.4, 0.4]), (3, 1))
    BS2 = numpy.reshape(numpy.array([0.5, 0.4, 0.1]), (3, 1))
    config.B = numpy.concatenate((B0, BS1, BS2), 1)
