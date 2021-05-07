 ###################
#
# Name: Jahmes8
#
# Program: Pig Latin
#
# Date: 04/30/21
#
# Description: Converts a Word to Pig Latin and Returns It
#
###################

# import statements

# Function as Definitions

vowels=["a","e","i","o","u"]

def pig_latin(word):
    if word[0] in vowels:
        ans= word + "way"
    else:
        ans= word[1:] + word[0] + "ay"
    print (ans)

# Main Body

pig_latin("boot")
pig_latin("image")
