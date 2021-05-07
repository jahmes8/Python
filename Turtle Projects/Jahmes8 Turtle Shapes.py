###################
#
# Name: Jahmes8
#
# Program: Turtle Shapes Project
#
# Date: 2/12/21
#
# Description: Use the turtle to draw various shapes using functions and parameters

###################

# import statements

import turtle as t

# function as definitions

def polygon(numSides, length, colr):
    t.pd()
    t.color(colr)
    for i in range(numSides):
        t.fd(length)
        t.lt(360/numSides)

def star(colr):
    t.pd()
    t.colormode(255)
    t.pencolor(249, 226, 134)
    
# main body

t.pu()
t.setpos(200, 200)
for i in range(6):
   t.forward(120)
   t.right(144)
   star("F9E286")


t.mainloop()


