###################
#
# Name: Jahmes8
#
# Program: Using the loop variable i
#
# Date: 2/18/21
#
# Description: Increase or decrease the size of shapes by using the variable in the for loop
#
###################

# import statements

import turtle as t

# function as definitions

def stars(size):
    t.pd()
    for i in range(5):
        t.fd(size)
        t.rt(144)

def square_spiral(size, spacing):
    t.seth(0)
    for i in range(size):
        t.fd(i*spacing)
        t.lt(90)


# main body
t.pu()
t.setpos(-200,200)
for i in range(1,5):
    stars(i*20)
    t.pu()
    t.seth(0)
    t.fd(i*20+50)

t.pu()
t.setpos(-200,-200)
t.pd()
square_spiral(30, 10)

t.mainloop()
