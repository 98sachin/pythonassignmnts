import keyword

"""
Assignment-2: Python Basics

1. Write a python script to add comments and print “Learning Python” on screen.
2. Write a python script to add multi line comments and print values of four variables,
each in a new line. Variable contains any values.
3. Write a python script to print types of variables. Create 5 variables each of them
containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
4. Write a python script to print the id of two variables containing the same integer
values.
5. Create four variables in a Python script and assign values of different data types to
them. Write a Python script to print value, its type and id of each variable
6. Write a python script to print all the keywords
7. On Python shell use help() function and display the list of keywords
8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
value to it. Write a python script to import A1 module in A0 and print value of the
variable created in A0.py
9. Name the keywords, used as data in the Python script.
10. Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)
"""

# 3, 5.
# a=23;
# b=True;
# c=3+4j;   j in complex number is called "iota".
# d=4.5;
# e="sachin";

# print(a, type(a), id(a));
# print(b, type(b), id(b));
# print(c, type(c), id(c));
# print(d, type(d), id(d));
# print(e, type(e), id(e));

# =======================================================================

# 4.
# x=34;
# y=34;

# print(id(x));
# print(id(y));

# ==================================================================

# 6. Write a python script to print all the keywords

# print(keyword.kwlist);

# ====================================================================

# 9. Name the keywords, used as data in the Python script.

# Ans: False, None and True.  these are soft keyword because these can also be used a data.

# =====================================================================

# 10. Write a python script to display the current date and time. First create variables to store date and time, then display date and time in proper format (like: 13-8-2022 and 9:00 PM).


# Getting current date and time using now().
 
# importing datetime module for now()
# import datetime
 
# using now() to get current time
# current_time = datetime.datetime.now()
 
# Printing value of now.
# print("Time now at greenwich meridian is:", current_time)

# OR  =======================

# Python3 code to demonstrate
# attributes of now()
 
# importing datetime module for now()
# import datetime
 
# using now() to get current time
# current_time = datetime.datetime.now()
 
# Printing attributes of now().
# print("The attributes of now() are :")
 
# print("Year :", current_time.year)
 
# print("Month : ", current_time.month)
 
# print("Day : ", current_time.day)
 
# print("Hour : ", current_time.hour)
 
# print("Minute : ", current_time.minute)
 
# print("Second :", current_time.second)
 
# print("Microsecond :", current_time.microsecond)

# OR ============

# Get Current Time In UTC using datetime Module
# UTC Stands for Coordinated Universal Time, These times are useful when you are dealing with Applications that have a global user for logging the events. You can get the current time in UTC by using the datetime.utcnow() method

# from datetime import datetime
 
# print("UTC Time: ", datetime.utcnow());

# REFER TO GFG 
