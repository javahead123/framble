#!/usr/bin/python


import random

LETTERS = [l for l in "ABCDEFGHIJKLMNOPRSTUVWXYZ"]
LETTERS.append("Qu")

def pull_random_letter_uniformly():
  random_index = random.randint(0, 24)
  return LETTERS[random_index]
  
  