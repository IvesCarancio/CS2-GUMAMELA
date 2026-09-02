import math # imports the map library

point_x1 = float(input("Please enter point_x1. ")) # 
point_x2 = float(input( "Please enter point_x2. "))
point_y1 = float(input("Please enter point y_1. " ))
point_y2 = float(input( "Please enter point_y2. "))

point_a = pow( point_x2 - point_x1, 2 )
point_b = pow(point_y2 - point_y1, 2)
distance = math.sqrt(point_a + point_b)

print ("Your distance is", distance)
