import os
import numpy

nohs = 2
A = numpy.zeros((nohs+2, nohs+2), dtype=float)

print('started\n')
path = '/home/oguz/Desktop/srilm'
os.chdir(path)

fileName1 = '3grams'
f1 = open(fileName1, 'r')
lines = f1.readlines()
n = len(lines)
print(n)

counter1 = 0
counter2 = 0

for index in range(0,n):
    if ( lines[index].split()[0] == '<s>' ):
        counter1 += int(lines[index].split()[3])

        if ( lines[index].split()[2] == '</s>'):
            counter2 += int(lines[index].split()[3])

A[0][2] = counter2/counter1
A[0][1] = (counter1 - counter2)/counter1


counter0 = 0
counter3 = 0
counter4 = 0
counter5 = 0

for index in range(0, n):
    counter0 += int(lines[index].split()[3])
    if (lines[index].split()[0] != '<s>'):
        counter3 = counter3 + int(lines[index].split()[3])

        if (lines[index].split()[2] == '</s>'):
            counter5 = counter5 + int(lines[index].split()[3])

        if (lines[index].split()[2] != '</s>'):
            counter4 = counter4 + int(lines[index].split()[3])


A[1][1] = counter4 / counter3
A[1][2] = counter5 / counter3


fileName2 = 'dunya.train.450k'
f2 = open(fileName2, 'r')


f1.close()
f2.close()
print('\ndone\n')