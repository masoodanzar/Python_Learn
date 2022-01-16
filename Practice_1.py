# # Create a program that asks the user to enter their name and their age. 
# name= input('Enter Name')
# age=int(input('Enter age'))
# x =  (2021 + 100-age)
# # Print out a message addressed to them that tells them the year that they will turn 100 years old.
# print("Hello," + name + ". You will be 100 in year " + str(x))
# #print (2021 + 100-age)
# ***********************************************************************************************
# Python program to interchange first and last elements in a list
# def swapnum(x):
#     tp= x[-1], x[0]
#     x[0], x[-1]= tp
#     return x 

# Inp = [12, 35, 9, 56, 24]
# print(Inp)
# Iny = swapnum(Inp)
# print(Iny)
# ***********************************************************************************************
# Python3 program to illustrate
# the usage of * operarnd
list = [1, 2, 3, 4]
list1 = [5, 6, 7]
list.append(list1)
list.insert(0, "Numbers") #Insert item at specific location in list
print(list)
list.removd(0)
print(list)
a, b, *c = list
# print(a)
# print(b)
# print(c)
# ***********************************************************************************************
