#!/usr/bin/python

import random

LETTERS = [l for l in "ABCDEFGHIJKLMNOPRSTUVWXYZ"]
LETTERS.append("Qu")

REL_FREQ = {
'A':9,
'B':2,
'C':2,
'D':4,
'E':12,
'F':2,
'G':3,
'H':2,
'I':9,
'J':1,
'K':1,
'L':4,
'M':2,
'N':6,
'O':8,
'P':2,
'Qu':1,
'R':6,
'S':4,
'T':6,
'U':4,
'V':2,
'W':2,
'X':1,
'Y':2,
'Z':1     
}

SUM_FREQ = sum(REL_FREQ.values())

def random_letter():
  letters = REL_FREQ.keys()
  rindex = random.randint(0, SUM_FREQ-1)
  letter_index = 0
  size_index = 0
  while size_index <= rindex:  
    #print letter_index
    letter = letters[letter_index-1]
    size = REL_FREQ[letter]
    if rindex < size_index + size:
      return letter  
    letter_index +=1
    size_index = size_index + size

def pull_random_letter_uniformly():
  random_index = random.randint(0, 25)
  return LETTERS[random_index]
  

  