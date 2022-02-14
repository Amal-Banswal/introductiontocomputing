#Assignment 3

#FIRST PROGRAM

print("Python program to count the number of occurrences of each word or character in the string entered by the user")

str = input("Enter the string: ")
wordslist = list(str.split())
if len(wordslist)==1:
    ch = input("Enter the character: ")
    cnt=0
    for i in str:
        if i==ch: 
            cnt+=1
    print("Occurences of {} is: {}".format(ch, cnt))
else:
    word = input("Enter the word: ")
    cnt = wordslist.count(word)
    print("Occurences of {} is: {}".format(word, cnt))

print("--------------------------------------------------------")



#SECOND PROGRAM

print("python script to print next date of input date with given input")

def cal_day(day, month, year, month_length):
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
            
    return [day, month, year]
   
def cal_month(month, leap_year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30
        
    return month_length

def cal_year(year):
    if (year % 400 == 0):
        leap_year = True
    elif (year % 100 == 0):
        leap_year = False
    elif (year % 4 == 0):
        leap_year = True
    else:
        leap_year = False
        
    return leap_year

def main():
    day = int(input("Day [1-31]: "))
    month = int(input("Month [1-12]: "))
    year = int(input("Year[1800-2025]: "))
    leap_year = cal_year(year)
    month_length = cal_month(month, leap_year)
    n_list = cal_day(day, month, year, month_length)
    print("The next date is: {}/{}/{}".format(n_list[0], n_list[1], n_list[2]))
    
main()

print("--------------------------------------------------------")



#THIRD PROGRAM

print("Python program to create a list of tuples with the first element as the number and Second element as the square of the number")

p_list = [1,2,3,4]
new_list = []
for i in p_list:
    new_list.append((i, i*i))
print(new_list)

print("--------------------------------------------------------")



#FOURTH PROGRAM

print("program to prompt the user for a grade")

def grade(points):
    switcher = {
        10: ["A+", "Outstanding"],
        9 : ["A", "Excellent"],
        8: ["B+", "Very Good"],
        7: ["B", "Good"],
        6: ["C+", "Average"],
        5: ["C", "Below Average"],
        4: ["D", "Poor"]
    }
    return switcher.get(points, "Error")
 
def main():
    points = int(input("Enter grade points: "))
    g_list = grade(points)
    if g_list=="Error":
        print("You entered wrong points")
    else:
        print("Your Grade is {} and {} Performance".format(g_list[0], g_list[1]))
    
main()

print("--------------------------------------------------------")



#FIFTH PROGRAM

print("Python program to print Given pattern")

str = "ABCDEFGHIJK"
l = len(str)
space = 0
while l>=1:
    sl = slice(l)
    for i in range(0, space):
        print(" ",end="")
    l-=2
    space+=1
    print(str[sl])

print("--------------------------------------------------------")
    


#SIXTH PROGRAM

print("python script that repeatedly ask user to enter name and SID of students")

dic = {}
name = input("Enter Name: ")
sid = int(input("Enter SID: "))
dic[sid] = name
ch = input("Do you want to enter more details[y/n]: ")
while ch=="y":
    name = input("Enter Name: ")
    sid = int(input("Enter SID: "))
    dic[sid] = name
    ch = input("Do you want to enter more details[y/n]: ")
    
print("\nDetails of the students: ") 
print("SID\tName")
for i in dic:
    print("{}\t{}".format(i, dic[i]))
    
print("\nSorted dictionary using student SID: ") 
sort_id = {k: v for k, v in sorted(dic.items())}
print("SID\tName")
for i in sort_id:
    print("{}\t{}".format(i, dic[i]))    
        
print("\nSorted dictionary using student Names: ") 
sort_names = {k: v for k, v in sorted(dic.items(), key = lambda v:v[1])}
print("SID\tName")
for i in sort_names:
    print("{}\t{}".format(i, dic[i]))   
        
id = int(input("\nEnter the SID of the student: "))
if id in dic:
    print("Name of the student is: ",dic[id])
else:
    print("The entered SID is not found")

print("--------------------------------------------------------")



#SEVENTH PROGRAM

print("python program to print Fibonacci sequence and  average of the resultant Fibonacci series")

def fibo(n):
    total=0
    t1=0
    t2=1
    for i in range(0, n):
        t3=t1+t2
        print(t1, end=" ")
        total+=t1
        t1=t2
        t2=t3
    return total
    
def main():
    n = int(input("Enter the terms: "))
    print("\nThe fibonacci series is:")
    total = fibo(n)
    avg = total/n
    print("\nThe average of the fibonacci series: ",avg)
main()

print("--------------------------------------------------------")



#EIGHTH PROGRAM

print("Question 8")

Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
Set4= {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#first part
z=Set2.difference(Set1)
y=Set1.difference(Set2)
S = y.union(z)
print(S)
    
#second part
x = Set1.difference(Set2.union(Set3))
y = Set2.difference(Set1.union(Set3))
z = Set3.difference(Set2.union(Set1))
S = x.union(y.union(z))
print(S)
    
#third part
x = (Set1.intersection(Set2)).difference(Set3)
y = (Set3.intersection(Set2)).difference(Set1)
z = (Set1.intersection(Set3)).difference(Set2)
S = x.union(y.union(z))
print(S)
    
#fourth part
S = Set4.difference(Set1)
print(S)
    
#fifth part
t = Set1.union(Set2.union(Set3))
S = Set4.difference(t)
print(S)

print("--------------------------------------------------------")

    
