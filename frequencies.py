#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enchant
import matplotlib.pyplot as plt
import numpy as np
import copy as cp

# War and Peace Full Text
wp = open("war_and_peace_full_text.txt", "r").read()





########################################### CHAR FREQUENCIES ###########################################
def graphCharFreqs(wp):
    ftable = {}
    # Build char table
    for i in range(ord('a'), ord('z')+1):
        ftable.update({chr(i) : 0 })

    charCount = 0

    for c in wp:
        if ftable.get(c) != None:
            ftable[c] += 1
            charCount += 1


    for key in ftable.keys():
        ftable[key] /= charCount

    ftablelist = sorted(ftable.items(), key=lambda x:x[1]) # ftable.items() returns tuples of (k,v)
    ftable = dict(ftablelist)                              # then the lambda selects the 2nd item of the tuple to be used for sorting

    print(ftable, charCount)

    print(list(ftable.keys()))

    # CHAR FREQ TABLE PLOT
    names = list(ftable.keys())
    values = list(ftable.values())

    plt.figure(figsize=(9, 3)) # specify width and height in inches

    plt.subplot(111)
    plt.bar(names, values)
    plt.suptitle('Char Frequencies [A - Z]')
    plt.show()

def getCharFreqs(wp):
    '''return a table or english char freqs'''
    ftable = {}
    # Build char table
    for i in range(ord('a'), ord('z')+1):
        ftable.update({chr(i) : 0 })

    charCount = 0

    for c in wp:
        if ftable.get(c) != None:
            ftable[c] += 1
        charCount += 1


    for key in ftable.keys():
        ftable[key] /= charCount

    ftablelist = sorted(ftable.items(), key=lambda x:x[1]) # ftable.items() returns tuples of (k,v)
    ftable = dict(ftablelist)                              # then the lambda selects the 2nd item of the tuple to be used for sorting

    return ftable


def graphBigramFreqs(wp):
    ftable = {}
    # Build char table
    for i in range(ord('a'), ord('z')+1):
        for j in range(ord('a'), ord('z')+1):
            ftable.update({chr(i)+chr(j) : 0 })

    bigramCount = 0

    for i in range(1,len(wp)):
        if ftable.get((wp[i-1]+wp[i]).lower()) != None:
            ftable[(wp[i-1]+wp[i]).lower()] += 1
        bigramCount += 1


    for key in ftable.keys():
        ftable[key] /= bigramCount

    ftablelist = sorted(ftable.items(), key=lambda x:x[1]) # ftable.items() returns tuples of (k,v)
    ftable = dict(ftablelist)                              # then the lambda selects the 2nd item of the tuple to be used for sorting

    print(ftable, bigramCount)

    print(list(ftable.keys()))

    # CHAR FREQ TABLE PLOT
    keys = list(ftable.keys())
    vals = list(ftable.values())
    names = keys[len(keys) - 36 : ]
    values = vals[len(vals) - 36 : ]

    plt.figure(figsize=(9, 3)) # specify width and height in inches

    plt.subplot(111)
    plt.bar(names, values)
    plt.suptitle('First 35 Bigrams By Frequency')
    plt.show()





########################################### MOST FREQUENT WORDS (but who cares) ###########################################
def plotMostFrequentWords(wp):
    # English Dict
    edict = enchant.Dict("en-us")

    # screw efficiency lets python it up
    words = wp.split()

    # strip anything that isn't alphabetical
    charSet = [ chr(i) for i in range(1,256) if not chr(i).isalpha() ] # we wont take the null byte
    print(charSet)
    charSet = "".join(charSet)
    words = [ w.strip(charSet) for w in words ]

    words = [ w for w in words if w != "" and edict.check(w) ] # and is short circuiting in python as well

    print(len(words), len(set(words)))
    #  print(charSet)

    ftablelist = [ (k,0) for k in set(words) ] # list of (k,v) tuples

    ftable = dict(ftablelist)

    #  print(ftablelist)

    wordCount = len(words) # we only want to count valid words
    for word in words:
        ftable[word] += 1

    for key in ftable.keys():
        ftable[key] /= wordCount

    ftablelist = sorted(ftable.items(), key=lambda x:x[1]) # ftable.items() returns tuples of (k,v)
    ftable = dict(ftablelist)                              # then the lambda selects the 2nd item of the tuple to be used for sorting

    #  print(ftable,wordCount)

    # WORD FREQ PLOT FIRST 35
    keys = list(ftable.keys())
    vals = list(ftable.values())
    names = keys[len(keys) - 36 : ]
    values = vals[len(vals) - 36 : ]

    plt.figure(figsize=(9, 3)) # specify width and height in inches

    plt.subplot(111)
    plt.bar(names, values)
    plt.suptitle('35 Most Frequent Words')
    plt.show()

def rateWord(s, ftable):
    '''take a string and return its weight based on char freqency in english'''
    return sum([ftable[c] for c in s])

def hash(s):
    return "".join(sorted(s))

def getFiveLetterWordsNo2HaveSameLetters(wp):
    
    # english dict
    edict = enchant.Dict("en-us") # lots of weird stuff in our word list

    wordlist = open("words.txt", "r")

    wordTable = {}

    # strip anything that isn't alphabetical
    charSet = [ chr(i) for i in range(1,256) if not chr(i).isalpha() ] # we wont take the null byte
    #  print(charSet)
    charSet = "".join(charSet)

    # Get a list of 5 letter words where no 2 words have exactly the same characters
    while True:
        word = wordlist.readline()
        if word == '': # we read the last word
            break
    
        word = word.strip(charSet)

        if len(word) == 5 and word.isalpha() and wordTable.get(hash(word.lower())) is None:
            wordTable.update({hash(word.lower()) : word.lower()})

    print(len(wordTable.values()))

    wordsWithUniqueChars = [ w for w in list(wordTable.values()) if len(set(w)) == 5 and edict.check(w) ]
    print(len(wordsWithUniqueChars))
    file = open("5_letter_words_no_2_have_same_letters.txt", "w")

    for word in wordsWithUniqueChars:
        file.write(word+"\n")
    
def wordGroups(words):
    if len(words) == 0:
        return

    # maybe we can think about like sets of chars
    alist = []
    blist = []

    file = open("mutually_exclusive_words.txt", "w")
    count = 0

    # n^2 is 51 million combinations -_- (which it did suprisingly fast)
    for t in words:
        l = [t]
        target = set(t)
        for word in words:
            if len( target.intersection(set(word)) ) == 0:
                target = target.union(set(word))
                l.append(word)

        file.write(" ".join(l) + "\n")
        count += 1
        print("wordList:", l, count)

def weightedSum(group, ftable):
    '''return sum of char freqs weighted by index, given a group of words'''
    S = 0
    for c, word in enumerate(group):
        S += (c+1) * rateWord(word,ftable)
    return S


def orderLists(wordGroups, ftable):

    # put everything in ascending order by frequency
    for i in range(len(wordGroups)):
        wordGroups[i] = sorted(wordGroups[i], key=lambda x:rateWord(x,ftable))

    # make sure it worked
    #  for group in wordGroups:
        #  print(list(map(lambda x:rateWord(x,ftable), group)))

    # sort by weighted sum
    wordGroups = sorted(wordGroups, key=lambda x: weightedSum(x,ftable), reverse=True)

    # make sure it worked again
    #  for group in wordGroups:
        #  print(group,weightedSum(group,ftable))

    # these are basically sorted by length as well. There are no seqeunces of four that have a smaller weight
    # than a sequence of length 3
    return wordGroups

def writeWordLists(wordGroups, ftable):
    '''write sorted groups to 3 files, 1 for seqences of length 2, length 3, etc'''

    breakPoints = []
    for i in range(1,len(wordGroups)):
        if len(wordGroups[i-1]) != len(wordGroups[i]):
            breakPoints.append(i) # this represents the end of a range in a slice

    breakPoints.append(len(wordGroups)) # the last endpoint is the end of list
    print(breakPoints)

    start = 0

    for c,p in enumerate(breakPoints):
        seg = wordGroups[start:p]
        file = open(f"group_{c}.txt", "w")
        file.write("WORD SEQUENCE : WEIGHT\n")
        for group in seg:
            file.write("{} {}\n".format(" ".join(group), str(weightedSum(group,ftable))))
        file.close()
        start = p #next range starts here

def writeWordList(words, ftable):
    '''write out list of words ranked by frequency'''
    words = sorted(words, key=lambda x:rateWord(x,ftable), reverse=True)

    file = open("words_by_frequency.txt", "w")
    file.write("WORD : WEIGHT\n")
    for word in words:
        file.write("{} {}\n".format(word, rateWord(word,ftable)))
    file.close()


if __name__ == "__main__":
    words = list(map(lambda w : w.strip("\n"), open("5_letter_words_no_2_have_same_letters.txt", "r").readlines()))

    wordGroups = [wl.strip("\n").split() for wl in open("mutually_exclusive_words.txt", "r") ]
    ftable = getCharFreqs(wp)

    #  print(wordGroups)

    #  graphCharFreqs(wp)

    #  plotMostFrequentWords(wp)

    #  graphBigramFreqs(wp)

    #  getFiveLetterWordsNo2HaveSameLetters(wp) # generate a file of english words with unique letters

    #  wordGroups(words) # generate file of mutually exclusive word lists

    wordGroups = orderLists(wordGroups, ftable)

    print(wordGroups)

    writeWordLists(wordGroups, ftable)
    writeWordList(words, ftable)



