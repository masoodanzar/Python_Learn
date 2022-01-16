# https://www.geeksforgeeks.org/file-handling-python/?ref=lbp
# a file named "geek", will be opened with the reading mode.
file = open('D:\PYTHON_PROGRAM\data\sample_text.txt', 'r')
# This will print every line one by one in the file
for each in file:
	print (each)

# Python code to illustrate read() mode
file = open("D:\PYTHON_PROGRAM\data\sample_text.txt", "r")
print (file.read(3))

# Python code to illustrate append() mode
file = open('D:\PYTHON_PROGRAM\data\sample_text.txt','a')
file.write("This will add this line")
file.close()
# Python code to illustrate with()
with open("file.txt") as file:
	data = file.read()
# do something with data

# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f:
	f.write("Hello World!!!")

# Python code to illustrate split() function
with open("file.text", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print (word)
