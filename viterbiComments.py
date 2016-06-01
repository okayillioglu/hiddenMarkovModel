# Written by Oğuz Kayıllıoğlu
# version: 0.1

# This is the main file for running viterbi decoder.

# Problem Definition
# Given as input an HMM lambda = (A,B) and a sequence of observations O = o1o2...oT, find the probable sequence of
# hidden states Q = q1q2...qT

# Hidden Markov Model (5 components)
# 1- Q = q1q2q3...qN, a set of N hidden states, Dimensions N by 1
# 2- A = a01a02...aNN, a transition probability matrix A, each aij representing transition probabilities from
# hidden state i to hidden state j, such that sum aij over j = 1 for all i, Dimensions: N by N
# 3- B = bi(ot) = P(ot|qt=j) a sequence of observation likelihoods, also called emission probabilities,
# expressing probability of an observation ot being generated from hidden state i, Dimensions: noov by nohs
# 4- O = o1o2...oT, a sequence of T observations, each drawn from observation vocabulary V = v1v2...vv,
# Dimensions v by 1
# 5- q0qF = a special start (q0) and an end (qF) state

# Define
# HMM parameters A (N+2xN+2) matrix and B (noov x nohs) matrix
# t: time

# Calculate vt(j), that is element of viterbi trellis
# vt(j) = max q0q1...qt-1 P(q0,q1...qt-1,o1,o2,...,ot,qt=j|A,B)
# vt(j) = max from i to N vt-1(j)*aij*bj(ot)
# vt(j) probability that the HMM is in hidden state j after seeing the first t observations and passing through the
# most probable hidden state sequence q0q1...qt-1, given automaton lambda = (A,B)
# Viterbi Matrix, Dimensions

# define
# nohs: # non-emitting hidden states
# noov: # elements in observations vocabulary
# t: Time index ranging from 1 to T
# T: runtime of a observation sequence o1o2...oT
# ot: observation symbol at time t
# V observation vocabulary V=v1v2...vv
# hiddenStates: a list containing index number of emitting hidden states in ascending order, from 1 to N
# for this specific case, q1 = hot and q2 = cold
# ObservationsVocabularyIndex: a list containing corresponding index number of each observation in
# ObservationVocabulary, a list containing possible observations, number of elements is v
# Viterbi: A matrix containing viterbi path probabilities