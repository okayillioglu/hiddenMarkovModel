import os
os.chdir('/home/oguz/Desktop/srilm')
import numpy

nohs=2

fileName1 = 'dunya.train.450k'
f1 = open(fileName1, 'r')
lines1 = f1.readlines()

fileName1neosWords = 'dunya.train.450k.neosWords'
f1Name1neosWords = open(fileName1neosWords, 'w')

now = 0
n = len(lines1)
for i in range(0,n):
    words = lines1[i].split()
    now = now + len(words)

pqt2 = n/now
pqt1 = 1 - pqt2

###########################################
fileName2 = 'vocab'
f2 = open(fileName2, 'r')
lines2= f2.readlines()
noov = len(lines2)

observation_vocab = [0]*noov
for i in range(0, noov):
    observation_vocab[i] = lines2[i][:-1]

x=[0]*noov
for i in range(0,noov):
    x[i] = i

dict_observation_vocab = dict(zip(observation_vocab, x))


###########################################
B = numpy.zeros((noov, nohs), dtype=float)

vocabStateCounts = numpy.zeros((noov,nohs), dtype=int)


