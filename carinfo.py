#Make a new class for the car 
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  
  #Method to add up all the variables 
  def display_car(self):
  	print "This is a", self.color, self.model, "with", str(self.mpg), "MPG."

#Ask for the car's info
imodel = raw_input("Model of the car ?: ")
icolor = raw_input("Color of the car ?: ")
impg = raw_input("Input mpg:  ")

#Insert the given info
my_car = Car(imodel, icolor, impg)

#Call the display_car with the info given by the user
my_car.display_car()
