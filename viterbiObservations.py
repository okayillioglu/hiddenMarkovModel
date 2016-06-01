import config
import numpy


def initialize_observations():
    config.observations = [3, 1, 3]
    config.observations = numpy.array(config.observations, dtype=int)
    config.v = len(config.observations)


def initialize_observations_vocab():

    config.observation_vocab = [1, 2, 3]
    config.observation_vocab = numpy.array(config.observation_vocab, dtype=int)
    config.noov = len(config.observation_vocab)


def initialize_observation_vocab_index():
    config.observations_vocab_index = numpy.zeros(config.v + 1, dtype=int)
    # index refers to t, time
    for index in range(0, config.v):
        config.observations_vocab_index[index + 1]\
            = numpy.where(config.observation_vocab == config.observations[index])[0]
