"""Scrabble score calulator:
    for example word "Helix" would return 15.
    4 + 1 + 1 + 1 + 8. """







score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
  lowers = word.lower() #Make em lower to work with Uppers too
  total = 0
  for c in lowers: # For every letter in the word add the equilevalent score of that letter to total
    total += score[c]
  return total
