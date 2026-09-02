import math # imports the map library

point_x1 = float(input("Please enter point_x1. ")) # This is the input for the first x coordinate.
point_x2 = float(input( "Please enter point_x2. ")) # This is the input for the second x coordinate.
point_y1 = float(input("Please enter point y_1. " )) # This is the input for the first y coordinate.
point_y2 = float(input( "Please enter point_y2. ")) # This is the input for the second y coordinate.

point_a = pow( point_x2 - point_x1, 2 ) # this computes for the point a.
point_b = pow(point_y2 - point_y1, 2) # this computes for the point b.
distance = math.sqrt(point_a + point_b) # This computes the final distance.

print ("Your distance is", distance) #This shows the final distance.
