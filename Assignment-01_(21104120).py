# QUESTION 1
print("PYHTON PROGRAM TO FIND AVERAGE OF THREE GIVEN NUMBERS")

first_no=eval(input("Enter the first number: "))
sec_no=eval(input("Enter the second number: "))
third_no=eval(input("Enter the third number: "))
avg=(first_no + sec_no + third_no) / 3

print("Average of ",first_no,", ",sec_no," and ",third_no," is ",avg)

print("--------------------------------------------------------")



#QUESTION 2
print("PYTHON PROGRAM TO CALCULATE THE INCOME TAX OF PERSON AFTER SEVERAL DEDUCTION OF MONEY (GROSS INCOME>$30000)")
gross_income=int(input("Please Enter the Gross Income($) "))
noOfDep=int(input("Please Enter the number of dependents: "))

# deduction1=Standard Deduction
deduc_1=10000

#deduction2=Dependent Deduction
deduc_2=int(3000 * noOfDep)
taxable_income = gross_income- deduc_1 - deduc_2
tax_rate= 0.20 * taxable_income
tax=taxable_income + tax_rate
print("The total Income Tax of a person is: $" , tax)

print("--------------------------------------------------------")





#QUESTION 3
print("PYTHON PROGRAM TO STORE VALUES IN LISTS")
stu_details=[]
S_id=int(input("Enter the SID of the student: "))
stu_name=input("Enter the NAME of the student: ")
stu_gender=input("Enter the GENDER (M/F): ")
stu_course=input("Enter the COURSE NAME of the student: ")
CG=float(input("Enter the CGPA of the student: "))
stu_details.append(S_id)
stu_details.append(stu_name)
stu_details.append(stu_gender)
stu_details.append(stu_course)
stu_details.append(CG)
print(stu_details)

print("--------------------------------------------------------")





#QUESTION 4
print("PYTHON PROGRAM TO ENTER THE MARKS OF FIVE STUDENTS")

stu_1=int(input("Enter the marks of first Student:"))
stu_2=int(input("Enter the marks of second Student: "))
stu_3=int(input("Enter the marks of third Student: "))
stu_4=int(input("Enter the marks of fourth Student: "))
stu_5=int(input("Enter the marks of fifth Student: "))
stu_list=[]
stu_list.append(stu_1)
stu_list.append(stu_2)
stu_list.append(stu_3)
stu_list.append(stu_4)
stu_list.append(stu_5)
print("The Lists of marks of five students is: " )
print(stu_list)

print("--------------------------------------------------------")





#QUESTION 5
print("PYTHON PROGRAM TO PRINT A SPECIFIED LIST IN A MANNER")
LIST=['Red','Green','White','Black','Pink','Yellow']
LIST.remove('Black')
print(LIST)
LIST[3]=('Purple')
print(LIST)

print("--------------------------------------------------------")





