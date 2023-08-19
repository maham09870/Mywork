# print("<===== First Assignment====>")
# Eng = 67
# Maths=90
# Isl=80
# total =300
# Obt=Eng+Maths+Isl
# percentage = (Obt/total)*100
# print ( percentage)
# if   percentage < 100 and percentage >= 80:
#      print("A+ passed")
# elif percentage < 80 and percentage >=70:
#      print("A passed")
# elif percentage < 70 and percentage > 60:
#      print ("B passed")
# elif percentage < 60 and percentage > 50:
#      print ("C passed")
# else:
#      print ("failed")
# print("<=====Assignment 2,3,4=====>")
# print("<=====Question:1====")
# print("Twinkel twinkel little star")
# print("\tHow i wonder what you are")
# print("\t\t\tUp above the once so high")
# print("\t\t\tlike a diamond in the sky")
# print("Twinkel twinkel little star")
# print("\tHow i wonder what you are\n")

# print("<=========Question:2==============>\n")
# import sys
# python_version= sys.version
# print("python version:",python_version)
# print("<=====Question:3======>")
# import datetime

# print("current date and time",datetime.datetime.now())
# print("<====Question:4==>")

# radius=int((input("enter the radius:\n")))
# area=3.142*(radius*radius)
# print(area)
# print("<====Question:5===>")
# firstname=input("enter your first name:\n")
# lastname=input("enter your last name:\n")
# reversed_string=firstname[::-1]+' '+lastname[::-1]

# print(lastname+" "+firstname)

# print("<=====Question:6===>")
# first_num=int(input("enter your first number"))
# second_num=int(input("enter your second number"))
# add=first_num+second_num
# print("your result is" ,add)


# print("<===Question:7=====>\n")
# Eng =int(input("Subject 1:")) 
# Maths=int(input("Subject 2:"))
# Isl=int(input("Subject 3:"))
# comp=int(input("Subject 4:"))
# urdu=int(input("Subject 5:"))


# total =500
# Obt=Eng+Maths+Isl+comp+urdu
# percentage = (Obt/total)*100
# print ( percentage)
# if   percentage < 100 and percentage >= 80:
#      print("A+ passed")
# elif percentage < 80 and percentage >=70:
#      print("A passed")
# elif percentage < 70 and percentage >= 60:
#      print ("B passed")
# elif percentage <= 60 and percentage >= 50:
#      print ("C passed")
# else:
#      print ("failed")


# print("<==========3==Quserion:8========>")
# x=int(input("enter the number"))
# if x%2==0:
#     print("given number is even")
# else:
#     print("given number is odd")
# print("<========Question9:Write a program which print the length of the list?======>")
# List=['English','Math','Urdu','Science','Computer','SST']
# print(len(List))
# print("<question10: Write a python program to sum all the numeric item in list ?> ")
# List2=[23,34,55,67,21,33,56,7,23]
# # Sum=sum(List2)
# # print(Sum)
# sum=0
# for Q in List2:
#     sum+=Q
#     print(sum)
# print('<Question11: Write the python Program to get the Largest num from the numeric list')
# List2=[23,34,55,67,21,33,56,7,23]
# print(max(List2))
# print('<question12:Take a list, say for example this one: A=[1,1,2,3,5,8,13,21,34,55,89>] write a program that prints out all the element of the list that are less than 5')
# A=[1,1,2,3,5,8,13,21,34,55,89]
# for x in A:
#     if x<5:
#         print(x)
# print('<Assignment#4><Question01:Make a calculator using Python with Addition, Subtraction,multiplication, division,and power>')

# num1= int(input("Enter your first number="))
# num2= int(input("Enter your second number="))
# print("1,addition")
# print("2,subtration")
# print('3,multiplication')
# print("4,division")
# print("5,power")
# User=int(input("select 1 for addition \n select 2 for subtraction \n select 3 for multiplication \n 4 for division \n 5 for power\n please select opttion 1-5 ="))
# if User== 1:
#     print(num1+num2)
# elif User==2:
#      print(num1-num2)
# elif User==3:
#     print(num1*num2)
# elif User==4:
#     print(num1/num2)
# elif User==5:
#     print(pow(num1,num2))
# else:
#     print("Invalid")
# print("==<Assignmetn 4> <Question2>==")
# def has_numeric_value(lst):
#     for item in lst:
#         if isinstance(item, (int, float)):
#             return True
#     return False

# user_list = input("Enter a list of values (separated by spaces): ").split()

# for i in range(len(user_list)):
#     try:
#         user_list[i] = int(user_list[i])
#     except ValueError:
#         try:
#             user_list[i] = float(user_list[i])
#         except ValueError:
#             pass

# if has_numeric_value(user_list):
#     print("The list contains at least one numeric value.")
# else:
#     print("The list does not contain any numeric values.")
# print("==<Assignmetn 4> <Question2 again>==")
# def has_numeric_value(lst):
#     for item in lst:
#         if isinstance(item, (int, float)):
#             return True
#     return False
# my_list = [1, 'apple', 3.14, 'banana', True, 42]

# if has_numeric_value(my_list):
#     print("The list contains at least one numeric value.")
# else:
#     print("The list does not contain any numeric values.")
    
# print("==<Assignmetn 4> <Question4>==")
# my_dict = {
#     "a": 10,
#     "b": 20,
#     "c": "not a number",
#     "d": 15.5,
#     "e": "another string",
#     "f": 7
# }

# def sum_numeric_values(dictionary):
#     total = 0
#     for value in dictionary.values():
#         if isinstance(value, (int, float)):
#             total += value
#     return total

# total_sum = sum_numeric_values(my_dict)
# print("Sum of numeric values in the dictionary:", total_sum)
# print("==<Assignmetn 4> <Question3>==")
# my_dict = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# my_dict["occupation"] = "Engineer"

# print(my_dict)
# print("==<Assignmetn 4> <Question5>==")
# def find_duplicates(lst):
#     duplicates = []
#     seen = set()
    
#     for item in lst:
#         if item in seen:
#             duplicates.append(item)
#         else:
#             seen.add(item)
    
#     return duplicates

# my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]

# duplicate_values = find_duplicates(my_list)

# if len(duplicate_values) > 0:
#     print("Duplicate values in the list:", duplicate_values)
# else:
#     print("No duplicate values found in the list.")

# print("==<Assignmetn 4> <Question6>==")
# def count_numeric_values(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item, (int, float)):
#             count += 1
#     return count

# user_list = []

# while True:
#     user_input = input("Enter a value (or 'exit' to finish): ")
    
#     if user_input.lower() == 'exit':
#         break
    
#     try:
#         num_value = int(user_input)
#     except ValueError:
#         try:
#             num_value = float(user_input)
#         except ValueError:
#             num_value = user_input
        
#     user_list.append(num_value)

# numeric_count = count_numeric_values(user_list)

# if numeric_count > 0:
#     print(f"The list contains {numeric_count} numeric value(s).")
# else:
#     print("The list does not contain any numeric values.")

# print("User list:", user_list)