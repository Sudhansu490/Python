# Read the file
# use open() function to read the content of a file 

# Ex=1
# f=open('OOP Python/file1.txt')  # by default the mode is 'r(read)'
# data=f.read()
# print(data)
# f.close()

# Ex=2
# f=open('OOP Python/file1.txt','r')
# data=f.read(5)  # reads first 5 characters from the file
# print(data)
# f.close()

# ------------------------------------------------------------------------
# readline() function

# f=open('OOP Python/file1.txt')
# data=f.readline()
# print(data)  # read the first line & also prints the backslash so we get a blank line
# data=f.readline()
# print(data)  # read the second line
# data=f.readline()
# print(data)  # read the third line & so on
# data=f.readline()
# print(data)  # if the line is not available then it prints a blank line

# ------------------------------------------------------------------------
# write a file

# Ex=1
# f=open('OOP Python/file2.txt','w')  # 'w' mode used to write a file
# f.write('I am writing here')  # write at first line 
# f.write('\nwriting over')  # write at second line(we have to give \n to print the statement in a new line)
# f.close()

# Ex=2
# f=open('OOP Python/file2.txt','a')  # 'a'= add the text at the end 
# f.write('I am appending')  # can be called multiple times
# f.close()

# -------------------------------------------------------------
# with statement
# The best way to open & close the file automatically is the 'with' statement

# with open('OOP Python/file3.txt','w') as f:
#     a=f.write('This file 3rd file')
# with open('OOP Python/file3.txt','r') as f:
#     a=f.read()
# print(a)
# Don't need to write f.close() as it is done automatically