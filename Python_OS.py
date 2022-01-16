# Python program to explain os.getcwd() method importing os module
import os
cwd = os.getcwd() # Get the current working directory (CWD)
print(cwd)
# Python program to change the
# current working directory


# Function to Get the current working directory
def current_path():
	print("Current working directory before")
	print(os.getcwd())
	print()


# Driver's code
# Printing CWD before
current_path()

# Changing the CWD
os.chdir('../')

# Printing CWD after
current_path()

# Python program to explain os.mkdir() method

# importing os module
import os

# Directory
directory = "GeeksforGeeks"

# Parent Directory path
parent_dir = "D:/Pycharm projects/"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '% s' created" % directory)

# Directory
directory = "Geeks"

# Parent Directory path
parent_dir = "D:/Pycharm projects"

# mode
mode = 0o666

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)

# Python program to explain os.makedirs() method
	
# importing os module
import os
	
# Leaf directory
directory = "Nikhil"
	
# Parent Directories
parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"
	
# Path
path = os.path.join(parent_dir, directory)
	
# Create the directory
# 'Nikhil'
os.makedirs(path)
print("Directory '% s' created" % directory)
	
# Directory 'GeeksForGeeks' and 'Authors' will
# be created too
# if it does not exists
	
	
	
# Leaf directory
directory = "c"
	
# Parent Directories
parent_dir = "D:/Pycharm projects/GeeksforGeeks/a/b"
	
# mode
mode = 0o666
	
path = os.path.join(parent_dir, directory)
	
# Create the directory 'c'
	
os.makedirs(path, mode)
print("Directory '% s' created" % directory)
	
	
# 'GeeksForGeeks', 'a', and 'b'
# will also be created if
# it does not exists
	
# If any of the intermediate level
# directory is missing
# os.makedirs() method will
# create them
	
# os.makedirs() method can be
# used to create a directory tree

# Python program to explain os.listdir() method
	
# importing os module
import os

# Get the list of all files and directories
# in the root directory
path = "/"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# print the list
print(dir_list)

# Python program to explain os.remove() method
	
# importing os module
import os
	
# File name
file = 'file1.txt'
	
# File location
location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
	
# Path
path = os.path.join(location, file)
	
# Remove the file
# 'file.txt'
os.remove(path)
# Python program to explain os.rmdir() method
	
# importing os module
import os
	
# Directory name
directory = "Geeks"
	
# Parent Directory
parent = "D:/Pycharm projects/"
	
# Path
path = os.path.join(parent, directory)
	
# Remove the Directory
# "Geeks"
os.rmdir(path)


