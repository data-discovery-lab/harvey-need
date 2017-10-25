# Harvey-Need

## Sequential Mining using Pymining

### Import Library

`from pymining import seqmining`

### Sequence Formatting

Pymining iterates over elements inside of an array, therefor in order to find word sequences, the sequence must be an array inside an array. See below for an example:

`seqEx = [['bike','car','door'],['car'],['door','echo','figure']]`

### Output Example Using Sequence Above

```
freq_seqs = seqmining.freq_seq_enum(seqEx,2)

>> (('door',), 2)
>> (('car',), 2)
```

### Compile SeqMining.py

`$python SeqMining.py inputFile.csv 5`

*inputFile.csv:* Collection of terms for sequence creation

*5:* Number to represent the minimum number of occurances that any term must appear in the sequence

**Input File Format (CSV)**

Every data entry is in one column

```
term1 term2 term3 term4 | Date of tweet,
term3 term4 term5 term6 | Date of tweet,
term6 term7 term8 term9 | Date of tweet,
term9 term10 term11 term12 | Date of tweet
```

**Output of 'input.csv'**

Prints an array of tuples (word list, frequency count):
1. Word list is a list of words that were common in the sequence
2. Frequency count is the number of times the word list occured in the entire sequence

```
$python SeqMining.py input.csv 5

(('people', 'hurricane', 'help', 'avtweep', 'avgivesback', 'harvey'), 10)
(('hurricaneharvery', 'allegro', 'prayer'), 5)
(('realmadridhack', 'jimmy', 'morale', 'trndnl'), 6)
(('pic', 'hurricaneharvey'), 6)
(('body', 'txwx', 'wutv', 'arwx', 'nhc', 'okwx', 'txdot'), 31)
(('meme',), 31)
(('damage', 'rockport', 'harvey'), 11)
(('rockport', 'texa', 'hurricane'), 13)
(('friend', 'texa', 'hurricane', 'harvey'), 5)
(('txwx', 'nw', 'nhc'), 32)
```




For more information check out [Pymining's Repository](https://github.com/bartdag/pymining).
