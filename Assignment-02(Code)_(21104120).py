#Assignment 2

#FIRST PROGRAM(Q1)
print("PYHTON PROGRAM FOR GIVEN INPUT STRING")

str = "Python is a case sensitive language"

print("The length of the given string is: ", len(str))
print("Reverse of the given string is: ", str[::-1])
print("After slicing a particular string: ", str[slice(10, 26, 1)])
print("After replacing: ", str.replace("a case sensitive", "object oriented"))
print("Position of 'a' in the string is: ", str.index("a"))
print("String after removing white spaces: ", str.replace(" ", ""))

print("--------------------------------------------------------")


#SECOND PROGRAM(Q2)
print("PYTHON PROGRAM TO STORE VALUES IN DIFFERENT VARIABLES WITH THE USE OF STRING FORMATTING PRINT")

name = input("Enter Name: ")
SID = input("Enter SID: ")
dept = input("Enter Department: ")
cgpa = input("Enter CGPA: ")
print("Hey, ", name, " here!\nMy SID is ", SID, "\nI'm from ", dept, "department and my CGPA is ", cgpa)

print("--------------------------------------------------------")


#THIRD PROGRAM(Q3)
print("PYTHON PROGRAM FOR PERFORMATION OF DIFFERNT OPERATIONS WITH THE HELP OF BIT-WISE OPERATOR")

a = 56
b = 10
print("a = ", a)
print("b = ", b)
print("a & b = ", a&b)
print("a | b = ", a|b)
print("a ^ b = ", a^b)
print("a after left shift with 2 bits: ", a<<2)
print("b after left shift with 2 bits: ", b<<2)
print("a after right shift with 4 bits: ", a>>4)
print("b after right shift with 4 bits: ", b>>4)

print("--------------------------------------------------------")


#FOURTH PROGRAM(Q4)
print("PYTHON PROGRAM TO FIND THE GREATEST OF THREE NUMBERS")

a = int(input("Enter first no.: "))
b = int(input("Enter second no.: "))
c = int(input("Enter third no.: "))
if(a>=c and a>=b): gr = a
elif(b>=c and b>=a): gr = b
else: gr = c
print("Greatest of the 3 no. is: ", gr)

print("--------------------------------------------------------")


#FIFTH PROGRAM(Q5)
print("PYTHON PROGRAM TO CHECK IF THE WORD “NAME” IS PRESENT IN THE STRING")

str = input("Enter any string: ")
if("name" in str): print("Yes, the string contains name")
else: print("No, the string doesn't contains name")

print("--------------------------------------------------------")


#SIXTH PROGRAM(Q6)
print("PYTHON PROGRAM FOR GIVEN THREE SIDES TO FORM A TRIANGLE")

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if((a+b)<c or (b+c)<a or (a+c)<b): print("Yes, a triangle can be formed.")
else: print("No, a triangle can not be formed.")

print("--------------------------------------------------------")
