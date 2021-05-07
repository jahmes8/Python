###################
#
# Name: Jahmes8
#
# Program: Variables and Expressions
#
# Date: 04/12/21
#
# Description: Various funcitons to do math calculations 
#
###################

# import statements
import math
# function as definitions

def lengthConversion(num):
    answer = num/2.54
    print("There are " + str(answer) + " inches in " + str(num) + " centimeters")

def timeConversion(num):
    answer = num*3600
    print(str(num) + " hours is " + str (answer) + " seconds ")

def temperatureConversion(num):
    answer = (9.0/5)*fah+32
    print(str(num) + " degree Celsius is " + str(answer) + " degree Fahrenheit")

def quadraticFormula(a,b,c):
    a1=4*a*c
    a2=b*b
    a3=2*a
    a4=a2+a1
    a5=-1*b
    a10=math.sqrt(a4)
    a7=a5+a10
    b7=a5+a10
    a8=a7/a3
    b8=b7/a3
    print("The first answer is x=" + str(a8) + ", and the second answer is x=" + str(b8))



# main body

inches=int(input("Please enter the number of centimeters to change to inches: "))
lengthConversion(inches)

time=int(input("Please enter time in Hours: "))
timeConversion(time)

fah=int(input("Please enter the degrees in Celsius you want to convert to Fahrenheit: "))
temperatureConversion(fah)

a = int(input("enter the value for a: "))
b  = int(input("enter the value for b: "))
c  = int(input("enter the value for c: "))
quadraticFormula(a,b,c)


