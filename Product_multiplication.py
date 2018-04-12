#Makes a list of integers as input and returns the product of all of the elements in the list. For example: product([4, 5, 5]) should return 100
def product(list):
  total = 1
  for num in list:
    total = total * num
  return total
