grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

#Count the total of scores in list, in grades_sum
#Then take the total and count the average with grades_average
#Count the variance  


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

#Count the total sum of grades
def grades_sum(scores):
  total = 0
  for score in scores:
    total += score
  return total

#Average is counted by total divided by the count of items total/lenght
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

#Count the variance of the grades, If variance is big grades were all over the place
def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) ** 2
  total = variance / len(scores)
  return total

print grades_variance(grades)
