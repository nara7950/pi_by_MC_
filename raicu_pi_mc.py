'''
Naomi Raicu 2024.09.19
Description of what this script does: 
Sets up a random 2D box just based on the possible x and y values: x range = [-1, 1], y range = [-1, 1]
Picks samples based on some kind of built-in probability distribution (I used random.randrange)
Calculates the distance of each point from x = 0, y = 0 (the origin): d = x^2 + y^2
Uses the d value to determine if the point is in the circle or outside the circle using the following logic:

If d is larger than the radius of a unit circle (r = 1), then the point is outside of the circle.
Otherwise, the point is within the circle.

Finally, the number of inside and outside points are counted, and then
this script calculates an approximate value of pi: 4 * ((number of points in circle)/(total number of points))
'''

import random
import os
import numpy as np

num_samples = 10**5
#Define x and y value ranges for a unit 2D box
x_lo = -1
x_hi = 1
y_lo = -1
y_hi = 1

gain = 1000
dec_precision = 1/gain

x_vals = np.array([random.randrange(x_lo*gain, x_hi*gain, 1)/gain for i in range(num_samples)])
y_vals = np.array([random.randrange(y_lo*gain, y_hi*gain, 1)/gain for i in range(num_samples)])
print("\n") #separates terminal outputs since I don't like them bunched up

num_inside_circle = 0 #counter for number of points inside circle

for i in range(len(x_vals)):
    d = (x_vals[i]**2) + (y_vals[i]**2)
    if d > 1: #point is outside of the circle
        pass
    else: #point is on the border or in the circle
        num_inside_circle += 1

pi_estimate = 4*((num_inside_circle)/(num_samples))
print("Pi estimate is " + str(pi_estimate) + " using " + str(num_samples) + " samples, " + str(num_inside_circle) + " of which are inside the circle.")
print("Decimal precision for x and y values: " + str(dec_precision))
print("\n") #separates terminal outputs again