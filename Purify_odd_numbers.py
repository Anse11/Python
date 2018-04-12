#Purify list and return only even numbers on a new list

def purify(lst):
  a = []
  for n in lst:
    if n % 2 == 0:
      result = a.append(n)

      return result
