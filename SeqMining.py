# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 21:00:15 2017

@author: stuve
"""
import sys
from pymining import seqmining

seqTest = seq = [['bike','car','door'],['car'],['door','echo','figure']] #Test Sequence

seq = []
if(len(sys.argv) == 1):
    print("Please input a file name!\n >>python SeqMining.py inputFile.csv 5")
elif(len(sys.argv) == 2):
    print("Don't forget minimum number of occurance values!\n >>python SeqMining.py inputFile.csv 5")
else:
    with open(sys.argv[1], 'r') as inputFile:
        for line in inputFile:
            termList =[]
            terms = line.split('|')[0].replace('"','')
            for term in terms.split(' '):
                termList.append(term)
            seq.append(termList)
    
    #freq_seq_enum(seq[list],minimal support of set include [int]) -> A set(frequence value, support)
    freq_seqs = seqmining.freq_seq_enum(seq,int(sys.argv[2]))

    sorted(freq_seqs)

    for seq in freq_seqs:
        print(seq)
