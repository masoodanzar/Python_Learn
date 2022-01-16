num = input ("Enter number :")
name1 = input("Enter name : ")
print(num)
print ("type of number", type(num))
print(name1)
print ("type of name", type(name1))
# print("*************************")
x, y = input("Enter a two value: ").split(sep=',')
x=int(x); y=int(y); z=x+y; 
print("Number of boys: ", x)
print("Number of girls: ", y)
print("Boys {} + Girls {}= Total {}".format(x,y,z))
print(z)
# print("*************************")
print("Python", end='@') # Using end argument
print("GeeksforGeeks")

# ******************   VARIABLE TYPES ********************
#                          LIST
# taking multiple inputs at a time and type casting using list() function
lsx=["X1", 2 , "X2"]
for x1 in lsx:
    print(x1)

x2 = list(map(int, input("Enter Values").split()))
print("List of students: ", x2)


#                          TUPLE
mytuple = ("apple", "banana", "cherry")
for x3 in mytuple:
    print(x3)

#                          SET
thisset = {"apple", "banana", "cherry"}
print(thisset)

#                        DICTIONARY
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964 }
thisdict["color"] = "red" # Add Items
print(thisdict)
y = thisdict["model"]
print(y)
print(thisdict.keys())

# ARRAY
a = [1, 2, 3, 4]
for i in range(4):
    print(a[i], end =" + ")

# Program to demonstrate conditional operator
a, b = 10, 20
min = a if a < b else b
print(min) 
print( (b, a) [a < b] )
print({True: a, False: b} [a < b])
print((lambda: b, lambda: a)[a < b]())

