###################
#
# Name: Jahmes8
#
# Program: Variables, Expressions, Input 
#
# Date: 2/26/21
#
# Description: Variables, Expressions, Input worksheet
#
###################

# function as definitions

def quarts2gallons(qts):
    gallons = qts/4
    print ("There are " + str(qts) + " quarts in " + str(gallons) + " gallons." )

# main body

quarts=int(input("How many quarts? "))
quarts2gallons(quarts)

 
'''a = 2
b = 5
c = 6.4 
d = a+b
e = b/a
f = c/a
print ("The Total is " + str(d))
print ("Integer Division is " + str(e))
print ("Float Division is " + str(f))

def age_in_ten(name, age):
    future_age = age + 10
    print (name + " in ten years youll be " + str(future_age) + " years old")

your_name = input("what is your Name? ")
your_age = int(input("How old are you? "))
age_in_ten(your_name, your_age)

print("Jame has 4 cats and 2.5 gallons of milk")'''







