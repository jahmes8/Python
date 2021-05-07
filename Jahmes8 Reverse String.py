###################
#
# Name: Jahmes8
#
# Program: Reverse String
#
# Date: 04/26/21
#
# Description: Two functions... One that reverses & One that mirrors a given string
#
###################

# import statements

# function as definitions

def reverse(s):
    index=len(s)-1
    reverseString=""
    while index >=0:
        reverseString =reverseString+s[index]
        index=index-1
    return reverseString

def mirror(s):
    rev=reverse(s)
    return s + rev


# main body

answer="hello"
#print(reverse(answer))
print(mirror(answer))