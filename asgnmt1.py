# import sys

""""
Assignment-1: Warm-up with python
1. Write a command to get the Python version you are using.
2. Write a python script to print Hello Python on the screen directly in the command
line.
3. Write a python script and store it in a file and execute the file from the command line.
4. Write a python script to print Hello Python on the screen using visual studio code.
5. Write a python script to print Hello on the first line and Python on the second line
6. Write a python script to print “MySirG” on the screen
7. Write a python script to print “Teacher’s Day” on the screen
8. Write a python script to print the value of a variable. Variable contains your name as
data.
9. Write a python script to create variables to store your name, age, qualification, years
of experience and print it.
10. Write a python script to print values of three variables, each in a new line. Variable
contains integer value
"""



# 1. Write a command to get the Python version you are using.

# the first step is to import sys(see top)
# print("python version");
# print(sys. version);

# below code is to print version info
# print("version info");
# print(sys. version_info);

# ==================================================================================================================

# 2. Write a python script to print Hello Python on the screen directly in the command line.

# print("Hello Python");

# ==================================================================================================================

# How to Run Python Script by the Command Line
# To run Python program in terminal,store it in a ‘.py’ file in the command line, we have to write ‘python’ keyword before the file name in the command prompt. In this way we can run Python program in cmd.

# python hello.py

# ==================================================================================================================

# 3. Write a python script and store it in a file and execute the file from the command line.

# 4. Write a python script to print Hello Python on the screen using visual studio code.
# ==================================================================================================================

# 5. Write a python script to print Hello on the first line and Python on the second line.
# print("Hello");
# print("Python");
#     OR
# print("Hello\nPython");
#     OR
# print("Hello","Python",sep='\n');
#     OR
# print("Hello", end='\n');
# print("Python");
#     OR
# text = "Hello\nPython"
# lines = text.split('\n')

# print('\n'.join(lines))
# /    OR
# print(          check GFG for the article to print multiple line in python.
# """
# Hello
# Python""");

# a="Hello";
# b="Python";
# print(a,b,sep="+");
# ==================================================================================================================

# 9. Write a python script to create variables to store your name, age, qualification, years of experience and print it.

# a="sachin";
# b=25;
# c="graduate";
# d=1;

# print("name:",a,"age:",b,"qualification:",c,"years of experiance:",d);
#    OR
# print(a,b,c,d,sep='\n');

# ==================================================================================================================
# 10. Write a python script to print values of three variables, each in a new line. Variable contains integer values
# a,b,c=1,2,3;
# print(a,b,c,sep='\n');

# ==================================================================================================================

# To display multiple variables, use the print() method. To set the variables from multiple print() in a single line, use the end operator

# print(5, 10, 15, end=" ")
# print(10, 20, 30, 40, 50)
# ==================================================================================================================