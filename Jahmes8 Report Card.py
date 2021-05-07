###################
#
# Name: Jahmes8
#
# Program: Report Card
#
# Date: 04/29/21
#
# Description: Create a Simple Report Card of Classes and Grades
#
###################

# import statements

# function as definitions

def report_card():
    classes=[]
    grades=[]
    sum=0.0
    numClasses=int(input("How Many Classes Are You Taking? "))
        
    




# for loop - inside prompt for the class name then prompt for the class grade
# add the class to the list, add the grade to the list classes.append(var)

    for i in range(numClasses):
        className=input("Class Name? ")
        classes.append(className)
        grade=int(input("What is the %? "))
        grades.append(grade)
        sum = sum + grade

# for loop to print each class and each grade... also add each grade to the sum
# also calculate the average (when done printing)
# print the average



    print("REPORT CARD:")

    for i in range(len(classes)):
        print(classes[i] + " - " + str(grades[i]))
    
    avg=sum/numClasses
    print("Overall GPA: " + str(avg))

# main body

report_card()