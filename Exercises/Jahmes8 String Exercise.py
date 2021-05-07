###################
#
# Name: Jahmes8
#
# Program: String Excercise
#
# Date: 04/23/21
#
# Description: Using letters from a prefix check and concatonate letters from a suffix
#
###################

#import statements

#function as definitions

def spelling():
    prefix="JKLMNOPQ"
    suffix="ack"

    for letter in prefix:
        if letter == "O" or letter == "Q":
            print(letter+"U"+suffix)
        else:
            print(letter+suffix)
def count_letters(phrase,char):
    count=0
    for letter in phrase: 
        if letter == char:
            count +=1
    return count 



#main body

# spelling()

numLetters=count_letters("Hello there, It Is Friday!", 'r')
print(numLetters)

