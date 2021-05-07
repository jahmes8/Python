###################
#
# Name: Jahmes8
#
# Program: List Tutorial Exercise
#
# Date: 04/28/21
#
# Description: Examples of Using Lists
#
###################

# import statements

# function as definitions

def print_list(mylist):
    for item in mylist:
        print(item,end=" ")


# main body

# create list of days of week
week=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# print list
print_list(week)
print()
# remove Saturday and Sunday from list
week.remove("Sat")
week.remove("Sun")
print_list(week)
print()
# sort the list alphabetically
week.sort()
print_list(week)
print()
# reverse the sorting
week.reverse()
print_list(week)
print()
# print the third item from the list
week=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print(week[3])
