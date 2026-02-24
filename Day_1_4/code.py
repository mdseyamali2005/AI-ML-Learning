# '''#Veriable
# name = "Md Seyam Ali"
# ID = "0203492123"
# cgpa = 3.53
# student = True
# print(name, "ID is:",ID,"Cgpa is:", cgpa, "Is student",student,type(name)) 
# #Print veriable type
# print(type(ID))
# print(type(cgpa))
# #comment
# #Hello everyone how are you
# '''
# How are you doing , i am very fine thank youy
# i hope you are also fine
# Now i am working on google colab platform
# '''
# #arithmetic operations
# a = 3
# b = 2
# print(a+b)#sum
# print(a/b)#division
# print(a*b)#multiplication
# print(a-b)#subtraction
# print(a%b)#modulus
# print(a**b)#power
# print(a//b)#floor division
# #relational operations
# print(a==b)
# print(a<b)
# print(a!=b)
# print(a>=b)
# #assignment operator
# c=23
# c=c+6
# print(c)
# c+=3
# print(c)
# #Logical operator
# x = 4
# y = 6
# print(not(x<y))
# print(x<y and y<x)
# print(x<y or y<x)
# #type casting
# s = 53
# w = 34.34
# ans = int(s + w)
# print (ans, type(ans))
# #input
# a =float (input("Enter a: "))
# b =float (input("Enter b: "))
# sum = a + b
# print(sum)'''
# name = input("Enter your name: ")
# age = float(input("Enter your age: "))
# print(name,",", age)
# a = float (input("Enter a: "))
# b = float (input("Enter b: "))
# sum = a+b
# difference = a-b
# prouct = a*b
# quotient = a/b
# print(sum, difference, prouct, quotient)
# take_a = float(int(input("Enter a: ")))
# take_b = float(int(input("Enter b: ")))
# take_c = float(input("Enter c: "))
# average = (take_a + take_b + take_c) / 3
# print(average)
# uuu = input("Enter a noumber: ")
# a = int(uuu)
# b = float(uuu)
# c = str (uuu)
# print(type(uuu), type(a), type(b), type(c))
# x = 10 + 3* 2**2
# print(x)
# s = int (input("Enter a number: "))
# t = int (input("Enter another number: "))
# x = s
# s = t
# t = x
# print (s,   t)
# t = float(input("Enter temperature in celsius: "))
# f = (t*(9/5)) + 32
# print(f)
# import math
# r = float(input("Enter the radius of the circle: "))
# area = math.pi * r**2
# print(area)
# u = float(input("Enter the value of u: "))
# x = int(u)
# y = float(u-x)
# print("Integer part: ", x, "Fractional part: ", y)
# color = input("Enter a color: ")
# if color == "red":
#     print("stop")
# elif color == "yellow":
#     print("ready")
# elif color == "green":
#     print("go")
# else:
#     print("wrong color")
# o = int(input("Enter a number: "))
# if o % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# color = input("Enter a color: ")
# match color:
#     case "red":
#         print("stop")
#     case "yellow":
#         print("ready")
#     case "green":
#         print("start")
#     case _:
#         print("Wrong color")
# count = 1
# while count < 21:
#     print("I love you ", count)
#     count += 1
# print ("Value of count after the Loop:", count)
# n = int (input("Enter a number: "))
# i = 1
# while i < 11:
#     print (n*i)
#     i += 1


# i = 1
# while True:
#     if i %2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1
# word = "ami ki tomai valobasi"
# count = 0
# for ch in word:
#     if ch == "i":
#         count += 1
# print("Number of i in the string: ", count)
# for i in range(2, 11, 2):
#     print(i)
# def hello(a, b):
#     s = a+b
#     return s
# print(hello(3,5))
# print(hello(5,5))
#lambda function
# sum = lambda a,b: a+b
# print(sum(32,3))
# def fec(n):
#     i =1
#     for c in range(1,n+1):
#         i = i * c
#     return i
# n = int(input("Enter the number: "))
# print(fec(n))   
# g = float(input("Enter the value of g: "))
# if (30000 > g):
#     print(g*0.05)
# elif (30000 >= g and g <= 70000):
#     print(g*0.15)
# elif (g > 70000):
#     print(g*0.25)
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# for i in range (a, b+1):
#     if i % 2 == 0:
#         print(i)
# a = int(input("Enter a number: "))
# b = str(a)
# for c in range (0, len(b)):
#     print(b[c])
# def calculator(a, b , op):
#     if op == "+":
#         print(a+b)
#         return 0
#     elif op == "-":
#         print(a-b)
#         return 0
#     elif op == "*":
#         print(a*b)
#         return 0
#     elif op == "/":
#         print(a/b)
#         return 0
#     else:
#         print("wrong operator")
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# op = input("Enter an operator (+, -, *, /): ")
# calculator(a, b, op)
# word = "programming"
# word2 = " i fuck in sex"
# senence = word + word2
# print (senence)
# for ch in senence:
#     print(ch)
# word = "programming"
# print(word[-4:-2])
# a = 3 
# b = 34
# sum = a + b
# # print("Sum of {} and {} is {}".format(a, b, sum))
# print(f"Sum of {a} and {b} is {sum}")
# lois = ["aasdjkfhf", "fasdhtfg", "oetyhr", 4324, 432 , 34.234]
# print(type(lois[2:6]))
# num = [3, 43, 234]
# num.append(5)
# print(num)
# num.insert(2,78)
# print(num)
# num.reverse()
# print(num)
# num.sort()
# print(num)
# num = [3, 43, 234, 342, 232, 4521, 5234, 56234]
# find = 234
# inx = 0
# for val in num:
#     if val == find:
#         print(f"Found {find} at index {inx}")
#         break
#     inx += 1
# tup = (23,313,1,123,132,141,123)
# print(tup)
# print(tup[3:5])
# print(type(tup[:3]))
# tup = (23,313,1,123,132,141,123,1,123)
# for c in tup:
#     print(f"World is my love {c}")
# print(tup.index(123))
# print(tup.count(123))
#dictionary 
# my_dict = {
#     "name": "Md Seyam Ali",
#     "ID": "o23231233234231",
#     "cgpa": 3.20,
#     "subjects": ["cse3432", "cse234", "cses234"],
#     "skills": ["ai/ml", "data base", "web development"]
# }
# my_dict["cgpa"] = 22.42
# print(my_dict["name"], my_dict["subjects"])
# print(my_dict.get("cgpa"))
# list = my_dict.keys()
# print(list)
# values = my_dict.values()
# print(values)
# items = my_dict.items()
# print(items)
# my_dict.update({"bal": "23123"})
# print(my_dict)
#set 
# s = {324,242,42,3,3,3,3,5,234}
# s.add(6)
# print(s)
# info= [
#     ("Sara","Math"),
#     ("John","Science"),
#     ("Emma","History"),
#     ("Seyam","Science"),
#     ("Kate","Math"),
#     ("Mike","History"),
#     ("jara","Math"),
#     ("John","Math"),
#     ("Emma","Science"),
#     ("Emma","Math"),
#     ("Seyam","CSE"),


# ]
# course_unick = set()

# for tup in info:
#     course_unick.add(tup[1])
# print("unick mal ", course_unick)
# for name, course in info:
#     if course == "Math":
#         print(name)
# disc = {}
# for name, course in info:
#     if disc.get(name) == None:
#         disc.update({name: set()})
#         disc[name].add(course)
#     else:
#         disc[name].add(course)
# print(disc)
# string = input("Enter a string: ")
# string2 = str()
# bg = len(string)-1
# for ch in range(bg, -1,-1):
#     string2 += string[ch]
# if (string == string2):
#     print("palindrome")
# else:
#     print("not palindrome")
# seyam_list = [23, 43, 12, 54, 65, 34, 87]
# sum = 0
# avg = len(seyam_list)
# for i in seyam_list:
#     sum += i
# print("Sum is: ", sum)
# print("Average is: ", sum/avg)
# list1 = []
# list2 = []
# for i in range (0, 10):
#     list1.append(int(input("Enter list1 number: ")))
# for i in range (0, 10):
#     list2.append(int(input("Enter list2 number: ")))
# print("List1: ", list1)
# print("List2: ", list2)
# list3 = list1 + list2
# list3.sort()
# print(list3)
# tup = (23,313,1,123,132,141,123,1,123)
# odd = ()
# even = ()
# for c in tup:
#     if c % 2 == 0:
#         even += (c,)
#     else:
#         odd += (c,)
# print("Odd: ", odd)
# print("Even: ", even)
# disc = {
#     "seyam": 2.34,
#     "sara": 3.43,
#     "john": 3.23,
#     "emma": 3.75,
#     "kate": 3.65
# }
# print("A - Add a student\nB - Update marks\nC - Search for a student\nD - Display all students and marks\nE - Exit ")
# disc = {
#     "seyam": 623.234,
#     "sara": 732.43,
#     "john": 523.23, 
#     "emma": 875.75,
#     "kate": 665.65
# }
# while True:
#     choice = input("Enter your choice: ")
#     if choice == "A":
#         name = input("Enter student name: ")
#         if name in disc:
#             print("Student already exists.")
#         else:
#             marks = float(input("Enter student marks: "))
#             disc.update({name: marks})
#             print("Student added successfully.")
#     elif choice == "B":
#         name = input("Enter student name to update marks: ")
#         if name in disc:
#             marks = float(input("Enter new marks: "))
#             disc[name] = marks
#             print("Marks updated successfully.")
#         else:
#             print("Student not found.")
#     elif choice == "C":
#         name = input("Enter student name to search: ")
#         if name in disc:
#             print(f"{name}'s marks: {disc[name]}")
#         else:
#             print("Student not found.")
#     elif choice == "D":
#         for name, marks in disc.items():
#             print(f"Name is : {name}, Marks are: {marks}")
#     elif choice == "E":
#         print("Exiting the program.")
#         break
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# disc = {}
# for ch in words:
#     disc[ch] = len(ch)
# print(disc)
# random_test = input("Enter a string: ")
# count = 0
# for ch in random_test:
#     if ch == " ":
#         count += 1
# print("Number of spaces: ", count)  
##################################################  
# list1 = []
# number = int(input("Enter number of elements: "))
# for i in range (number):
#     list1.append(int(input("Enter for list1 element: ")))
# print(list1)
# list2 = []
# number2 = int(input("Enter number of elements: "))
# for i in range (number2):
#     list2.append(int(input("Enter for list2 element: ")))
# print(list2)
# sow1 = set()
# sow2 = set()
# for i in list1:
#     sow1.add(i)
# for i in list2:
#     sow2.add(i)
# print(sow1)
# print(sow2)
# if (sow1.intersection(sow2) == None):
#     print("No common elements") 
# else:
#     print("There are common elements")
#################################################
# seyam_list = [3,543,2,443,2,3,55,234,532]
# set1 = set(seyam_list)
# now_list = []
# for i in seyam_list:
#     if i in set1:
#         set1.remove(i)
#     else:
#         now_list.append(i)
# print("Duplicate elements are: ", now_list)

#################################################
# list1 = []
# number = int(input("Enter number of elements: "))
# for i in range (number):
#     list1.append(int(input("Enter for list1 element: ")))
# print(list1)
# list2 = []
# number2 = int(input("Enter number of elements: "))
# for i in range (number2):
#     list2.append(int(input("Enter for list2 element: ")))
# print(list2)
# sow1 = set(list1)
# sow2 = set(list2)
# print(sow1)
# print(sow2)
# if (sow1.intersection(sow2) == None):
#     print("No common elements") 
# else:
#     print("There are common elements")
################################################
# now_input = set(input("Enter a string: "))
# print(now_input)
# print(len(now_input))