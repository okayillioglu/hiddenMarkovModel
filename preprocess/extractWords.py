import os
os.chdir('/home/oguz/Desktop/srilm')

fileName1 = 'dunya.train.450k'
f1 = open(fileName1, 'r')
lines1 = f1.readlines()
n = len(lines1)

fNneos = 'neosWords'
fneos = open(fNneos,'w')

feos = 'eosWords'
feos = open(feos,'w')

for i in range(0, n):
    words = lines1[i].split()
    now = len(words)

    for index in range(0, now-1):
        fneos.write(words[index] + ' ')
    fneos.write('\n')
    feos.write(words[-1] + '\n')



f1.close()
fneos.close()
feos.close()
