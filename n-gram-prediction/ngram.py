
"""
N-gram word prediction model
"""


# --------------------------------------------------------------------------------
# Import
# --------------------------------------------------------------------------------

import os
import random
from pprint import pprint, pformat

import numpy as np
import pandas as pd
import nltk
from nltk import tokenize
from tabulate import tabulate

import data as datamodule
import util
from benchmark import benchmark

# --------------------------------------------------------------------------------
# Define ngram class
# --------------------------------------------------------------------------------

class Ngram():

    def __init__(self, data, n=3):
        """
        Create an n-gram model.
        Implements a multidimensional array of word counts as a dictionary of dictionaries.
        data - a Data object - see data.py
        n - amount of context - the n in n-gram
        """
        self.data = data
        self.n = n
        self._d = {} # dictionary of dictionary of ... of counts


    def fit(self, x_train, y_train, train_amount=1.0, debug=0):
        """
        Train the model
        """
        print("Training model n=%d..." % self.n)
        for xs, y in zip(x_train, y_train):
            self._increment_count(xs, y) # add ngram counts to model


    def _increment_count(self, xs, y):
        """
        Increment the value of the multidimensional array at given index (token tuple) by 1.
        """
        # ntokens = len(tuple)
        d = self._d
        # need to iterate down the token stream to find the last dictionary,
        # where you can increment the counter.
        for i, token in enumerate(xs):
            if token in d:
                d = d[token]
            else:
                d[token] = {}
                d = d[token]
        # at last dictionary
        token = y
        if token in d:
            d[token] += 1
        else:
            d[token] = 1


    def test(self, x_test, y_test, nsamples=10):
        """
        Test the model and set the accuracy, relevance score and some sample predictions.
        x_test - context/prompt tokens
        y_test - following token
        nsamples - number of sample predictions to record in self.test_samples
        Returns nothing, but sets
            self.test_accuracy
            self.test_relevance
            self.test_samples
        """
        print("Testing model n=%d..." % self.n)
        ntest = len(x_test)
        nsample_spacing = max(int(ntest / nsamples), 1) # how often to take a sample
        samples = []
        sample_columns = ['Prompt','Predictions','Actual','Status']
        naccurate = 0
        nrelevant = 0
        for i in range(ntest): # iterate over all test tokens
            prompt = x_test[i]
            actual = y_test[i]
            iword_probs = self.predict(prompt, k=3)
            accurate = False
            relevant = False
            if iword_probs: # can be None
                predicted_tokens = [token_prob[0] for token_prob in iword_probs]
                accurate = (actual == predicted_tokens[0])
                if accurate:
                    naccurate += 1
                relevant = (actual in predicted_tokens)
                if relevant:
                    nrelevant += 1
            # add sample predictions
            if (i % nsample_spacing) == 0:
                sprompt = ' '.join([self.data.iword_to_word[iword] for iword in prompt])
                sactual = self.data.iword_to_word[actual]
                if iword_probs:
                    spredictions = '  '.join(['%s (%.1f%%)' % \
                                              (self.data.iword_to_word[iword_prob[0]], iword_prob[1]*100) \
                                              for iword_prob in iword_probs])
                else:
                    spredictions = '(none)'
                saccurate = 'OK' if accurate else 'FAIL'
                sample = [sprompt, spredictions, sactual, saccurate]
                samples.append(sample)
        relevance = nrelevant / ntest if ntest>0 else 0
        accuracy = naccurate / ntest if ntest>0 else 0
        self.test_accuracy = accuracy
        self.test_relevance = relevance
        self.test_samples = pd.DataFrame(samples, columns=sample_columns)


    def generate_token(self, tokens):
        """
        Get a random token following the given sequence.
        """
        if self.n==1:
            tokens = [] # no context - will just return a random token from vocabulary
        else:
            tokens = tokens[-self.n+1:] # an n-gram can only see the last n tokens
        # get the final dictionary, which contains the subsequent tokens and their counts
        d = self._d
        for token in tokens:
            if token in d:
                d = d[token]
            else:
                return None
        # pick a random token according to the distribution of subsequent tokens
        ntotal = sum(d.values()) # total occurrences of subsequent tokens
        p = random.random() # a random value 0.0-1.0
        stopat = p * ntotal # we'll get the cumulative sum and stop when we get here
        ntotal = 0
        for token in d.keys():
            ntotal += d[token]
            if stopat < ntotal:
                return token
        return d.keys()[-1] # right? #. test


    def generate(self, nwords_to_generate=20):
        """
        Generate sentence of random text.
        """
        start1 = self.data.word_to_iword['2017-08-30'] #. magic
        output = []
        input = [start1]
        if self.n>=3:
            keys = list(self._d[start1].keys())
            start2 = random.choice(keys)
            input.append(start2)
            output.append(start2)
        if self.n>=4:
            start3 = random.choice(list(self._d[start1][start2].keys()))
            input.append(start3)
            output.append(start3)
        if self.n>=5:
            start4 = random.choice(list(self._d[start1][start2][start3].keys()))
            input.append(start4)
            output.append(start4)
        for i in range(nwords_to_generate):
            next = self.generate_token(input)
            input.pop(0)
            input.append(next)
            output.append(next)
        sentence = ' '.join([self.data.iword_to_word[iword] for iword in output])
        return sentence

    def generate_with_seeds(self, seed_words, nwords_to_generate=30):
        inputs = []
        output = []

        for w in seed_words:
            inputs.append(self.data.word_to_iword[w])

        for i in range(nwords_to_generate):
            next = self.generate_token(inputs)
            next_word = str(self.data.iword_to_word[next])

            if next_word.startswith('2017'):
                break
            inputs.pop(0)
            inputs.append(next)
            output.append(next)

        sentence = ' '.join([self.data.iword_to_word[iword] for iword in output])

        return sentence

    def predict(self, tokens, k=3):
        """
        Get the k most likely subsequent tokens following the given string.
        """
        #. add assert len(tokens)==self.n, or ignore too much/not enough info?
        # get the last dictionary, which contains the subsequent tokens and their counts
        d = self._d
        for token in tokens:
            if token in d:
                d = d[token]
            else:
                return [] #. ?
        # find the most likely subsequent token
        # see http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        # maxtoken = max(d, key=d.get)
        # return maxtoken
        best_tokens = util.get_best_tokens(d, k)
        return best_tokens



# --------------------------------------------------------------------------------
# Set Parameters
# --------------------------------------------------------------------------------

debug = False

DATASET      = 'need'
TRAIN_AMOUNT = 1 # 0.0 to 1.0
NVOCAB       = 10000
NTEST        = 200

# --------------------------------------------------------------------------------
# Get Data
# --------------------------------------------------------------------------------

data = datamodule.Data(DATASET)
data.prepare(nvocab=NVOCAB, debug=debug)
print()

for n in (3,):

    with benchmark('ngram train and test'):

        x_train, y_train, x_test, y_test = data.split(n=n, ntest=NTEST, train_amount=TRAIN_AMOUNT, debug=debug)

        # --------------------------------------------------------------------------------
        # Build Model
        # --------------------------------------------------------------------------------

        model = Ngram(data, n=n)

        # --------------------------------------------------------------------------------
        # Train Model
        # --------------------------------------------------------------------------------

        model.fit(x_train, y_train, debug=debug)

        # --------------------------------------------------------------------------------
        # Evaluate Model
        # --------------------------------------------------------------------------------

        model.test(x_test, y_test) # sets various model properties

        print('test accuracy:', model.test_accuracy)
        print('test relevance:', model.test_relevance)

        # print('sample predictions:')
        # df = model.test_samples
        # util.uprint(util.table(model.test_samples))

        # print('generated text:')
        nsentences = 1
        # for i in range(nsentences):
        #     try:
        #
        #         msg = model.generate()
        #
        #         util.uprint(msg) # weird symbols can crash print
        #     except :
        #         print('some error', i)
        # print()

        print('predict from long text input:')
        with open('data/need/n-gram-predicted-needs.txt', 'w') as writer:
            with open('data/need/weather.txt') as weatherFile:
                for line in weatherFile:
                    if len(line) < 10:
                        continue
                    line = line.replace('\n', '')
                    seeds = line.split(' ')
                    for i in range(nsentences):
                        msg = model.generate_with_seeds(seeds)
                        complete_msg = ' '.join(seeds) + ' ' + msg
                        util.uprint(complete_msg)  # weird symbols can crash print
                        writer.write(complete_msg + '\n')