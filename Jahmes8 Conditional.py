###################
#
# Name: Jahmes8
#
# Program: Examples of Conditionals
#
# Date: 04/13/21
#
# Description: Python code introducing conditionals (If Statements)
#
###################

# main body

'''answer=input("What is your favorite food? ")
if answer == "pizza":
    print("that is also my favorite.")
else:
    print(answer + " is not my favorite food. ")'''

have_pet=input("Do you have a pet? (yes/no)")

if have_pet == "yes":
    pet = input("Cool, what kind of pet do you have?")
    pet_name = input("Whats your pet's name?")
else: #they don't have a pet
    pet = input("Well, if you did get a pet, what kind would it be?")

if (pet=="dog" or pet=="Dog"):
    print("Dogs are great!")
elif pet == "cat" or pet == "Cat":
    print("cats are wonderful!")
else:
    print("Oh well, so you don't have a Cat or Dog?")

if(pet == "dog" or pet == "Dog") and (pet_name=="Buster"):
    print("Gee,my dog's name is Buster too.")

if have_pet == "yes":
    if (pet=="dog" or pet=="Dog"):
        print("I hope " + pet_name + " is a happy dog.")
    elif pet == "cat" or pet == "Cat":
        print("I hope " + pet_name + " is a sweet cat.")
    else:
        print("I hope you like your" + pet + ".")
else:
    print("you should go get yourself a " + pet + " today.")