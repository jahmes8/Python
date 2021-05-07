###################
#
# Name: Jahmes8
#
# Program: Creating Randomness
#
# Date: 2/23/21
#
# Description: Create 3 functions that use radint to draw
#
###################

# import statements
import turtle as t
import random as r
import time

# function as definitions
def random_lines(amt):
    for i in range(amt):
        t.color(r.randint(0,255), r.randint(0,255), r.randint(0,255))
        t.seth(r.randint(0,360))
        t.pensize(r.randint(1,8))
        t.fd(r.randint(20,100))

def polygon(numsides):
    t.pu()
    x=r.randint(-250,250)
    y=r.randint(-200,200)
    t.setposition(x,y)
    sidelen=r.randint(30,100)
    t.color(r.randint(0,255), r.randint(0,255), r.randint(0,255))
    t.pd()
    t.begin_fill()
    for i in range (numsides):
        t.fd(sidelen)
        t.lt(360/numsides)
    t.end_fill()





# main body
t.colormode(255)

#random_lines(50)

for j in range (2):
    polygon(4)
    polygon(5)
    polygon(6)
    polygon(7)
    polygon(8)
    




t.mainloop()