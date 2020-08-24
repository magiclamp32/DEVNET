class Circle:

    def __init__(self, radius):
        print(dir())
        self.radius = radius
        print(self)

    def circumference(self):
      # Formula for a circumference is c = pi * 2 * radius
      pi = 3.14 #
      circumferenceValue = pi * self.radius * 2
      return circumferenceValue

    def printCircumference(self):
      myCircumference = self.circumference()
      print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))

circle1 = Circle(2)
circle1.printCircumference()
# The Circle class can be instantiated multiple times
#circle2 = Circle(5)
#circle2.printCircumference()

#circle3 = Circle(7)
#circle3.printCircumference()
