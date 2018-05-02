class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  #Print out all the details about the car 
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
#If drive_car is called change the car's condition to used
  def drive_car(self):
    self.condition = "used"
#Make a new car class ElectricCar that inherits from original Car
class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type
#Change the drive_car method to behave differently when used with class ElectricCaar
  def drive_car(self):
    self.condition = "like new"

#Set a variable my_car to reference Class ElectricCar with given variables.
my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")

#Print the car's condition before driving it
print my_car.condition
#Call the ElectricCar's drive_car method to change the condition to like new
my_car.drive_car()
#Print the new condition.
print my_car.condition