# Katerina Chinnappan
# your kachinna@ucsc.edu
# programming assignment 1
#  Python program that computes the volume and surface area of a sphere
# whose radius is entered by the user.

#import pi
from math import pi as p

#get radius input from user
radius = float(input("Enter the radius of the sphere: "));

#calculate volume and surface area
volume = (4/3)*(p)*(radius**3);
surfaceArea = (4)*(p)*(radius**2);

#print the results
print("The volume is: "+str(volume));
print("The surface area is: "+str(surfaceArea));
                            