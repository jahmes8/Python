###################
#
# Name: James Chen
#
# Program: Barcode Validation
#
# Date: 05/03/21
#
# Description: Validating Barcodes
#
###################

# Import Statements

# Function as Definitions

barcode=input("Enter a Barcode: ") 
code=[]
if(len(barcode)!=13):
    print("Incorrect Try Again: ")
else:
    barcodeList=list(barcode)
    for number in barcode:
        code.append(number)
    odd=0
    even=1
    oddSum=0
    evenSum=0
    while odd<=12:
        oddSum=oddSum+int(code[odd])
        odd=odd+2
    while even<=12:
        evenSum=evenSum+int(code[even])
        even=even+2
    if( (3*evenSum+oddSum)%10==0):
        print("Valid")
    else:
        print("Invalid")

# Main Body
