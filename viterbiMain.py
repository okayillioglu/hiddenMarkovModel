import config
from viterbiHiddenStates import *
from viterbiTime import *
from viterbiObservations import *
from viterbiHMM import *
from viterbiAlgorithm import *

initialize_hidden()
initialize_time()
initialize_observations()
initialize_observations_vocab()
initialize_observation_vocab_index()
initialize_ab()
viterbi_initialization()
viterbi_recursion()
