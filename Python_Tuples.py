# A tuple is a sequence of immutable Python objects. 
# Tuples are just like lists with the exception that 
# tuples cannot be changed once declared. 
# Tuples are usually faster than lists.

Tuple1 = ('Geeks', 'For') #Creating a Tuple with the use of string
print(Tuple1)
list1 = [1, 2, 4, 5, 6] # Creating a Tuple with the use of list
Tuple2 = tuple(list1)
print(Tuple2)
Tuple3 = (5, 'Welcome', 7, 'Geeks') #Creating a Tuple with Mixed Datatype
print(Tuple3)
Tuple4 = (Tuple1, Tuple2) # Creating a Tuple with nested tuples
print(Tuple4)
Tuple5 = ('Geeks',) * 3 #Creating a Tuple with repetition
print(Tuple5)


