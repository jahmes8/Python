###################
#
# Name: Jahmes8
#
# Program: Triangle Area Calculator 
#
# Date: 3/01/21
#
# Description: Ask the user for the base and height of a triangle and calculate the area
#
###################

# import statements

# function as definitions

def calcArea(b, h):
    result=0.5*b*h
    return result 

# main body

base=input("Enter the base length of the triangle: ")
height=input("Enter the height of the triangle: ")

area=calcArea(float(base),float(height))
print("The area of the triangle is: " + str(area))
