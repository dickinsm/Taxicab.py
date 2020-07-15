# Author: Makaliah Dickinson
# Date: 7/14/2020
# Description: Write a class named Taxicab that has three private data members: one that holds the current x-coordinate,
#              one that holds the current y-coordinate, and one that holds the odometer reading (the actual odometer
#              distance driven by the Taxicab, not the Euclidean distance from its starting point). The class should
#              have an init method that takes two parameters and uses them to initialize the coordinates, and also
#              initializes the odometer to zero. The class should have get methods for each data member: get_x_coord,
#              get_y_coord, and get_odometer. The class does not need any set methods. It should have a method called
#              move_x that takes a parameter that tells how far the Taxicab should shift left or right. It should have a
#              method called move_y that takes a parameter that tells how far the Taxicab should shift up or down.

class Taxicab():
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.odometer = 0

    def get_x_coord(self):
        return self.x_coordinate

    def get_y_coord(self):
        return self.y_coordinate

    def get_odometer(self):
        return self.odometer

    def move_x(self, distance):
        self.x_coordinate += distance
        # add the absolute distance to odometer
        self.odometer += abs(distance)

    def move_y(self, distance):
        self.y_coordinate += distance
        # add the absolute distance to odometer
        self.odometer += abs(distance)



cab = Taxicab(5,-8)
cab.move_x(3)
cab.move_y(-4)
cab.move_x(-1)
print(cab.odometer) # will print 8 3+4+1 = 8