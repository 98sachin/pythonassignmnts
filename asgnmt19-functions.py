'''
Assignment - 19

Functions

1. Write a python program to create a simple function which prints “MySirG”.
2. Write a python program to create a function which expects two arguments and print
them in the function body.
3. Write a python program to create a function which expects an unknown number of
arguments.
4. Write a python program to create a function which expects kwargs arguments.
5. Write a python program to create a function which expects a list as an argument.
6. Write a python program to create a function that finds a maximum of four numbers.
7. Write a python program to sum all the numbers in a list.
8. Write a python program to multiply all the numbers in a list.
9. Write a python program to create a function to check whether a number falls in a
given range.
10. Write a python program to create a function to check whether a given number is even
or odd.
'''

#Q1. Write a python program to create a simple function which prints “MySirG”.

# Fuction definition 
# def name():
#     print();

# Function calling
# name();
# name();
# name();
# ==============================================================================

# Q2.Write a python program to create a function which expects two arguments and print them in the function body.

# def func(a):
#     print(a);
# func('sachin');
# func('saurav');

# def func(a,b):
#     print(a,b);
# func('sachin','sharma');

# def func(a,b):
#     print(f'a={a} , b={b}');
# func(10,20);
# func('sachin','sharma')
# ==============================================================================

# Q3. Write a python program to create a function which expects an unknown number of arguments.

# def arg(*any):
#     print(any);
#   OR
# def arg(*any):
#     for i in any:
#         print(i);

# arg(12,23,34,54);
# arg('sachin', 'sharma', 'will', 'be', 'rich')
# arg('sachin sharma will be rich')

#      OR

# def myFun(arg1, *argv):
#     print("First argument :", arg1)
#     for arg in argv:
#         print("Next argument through *argv :", arg)


# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
# ==============================================================================

# Q4. Write a python program to create a function which expects kwargs arguments.

# **kwargs = keyword arguments
# *args = Non keyword arguments

# def fun(**kwargs):
#     print(f'My name is {kwargs['name']}');

# fun(name='Sachin')

# def fun(**kwargs):
#     for a,b in kwargs.items():
#         print(f'{a} = {b}')

# fun(name='Sachin', age=23, city='Delhi')
# ==============================================================================

# Q5. Write a python program to create a function which expects a list as an argument.

# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

# def func(list):
#     for i in list:
#         print(i);

# plang = ['Python', 'Java', 'Go', 'Javascript', 'C', 'C++'];

# func(plang);

# ==============================================================================

# Q6. Write a python program to create a function that finds a maximum of four numbers.

# def func(num1, num2, num3, num4):
#     max_num = num1;
#     if num2>max_num:
#         max_num= num2;
#     if num3>max_num:
#         max_num=num3;
#     if num4>max_num:
#         max_num=num4;
#     return max_num;

# a=34;
# b=44;
# c=63;
# d=54;

# result = func(a,b,c,d)
# print(result)
# ==============================================================================

# Q7. Write a python program to sum all the numbers in a list.

# def sum_list(list):
#     sum = 0;
#     for i in list:
#         sum = sum + i;
#     return sum;
# nums = [5,5,5,5];
# result = sum_list(nums);
# print(result)
# ==============================================================================

# Q8. Write a python program to multiply all the numbers in a list.

# def sum_list(list):
#     sum = 1;
#     for i in list:
#         sum = sum * i;
#     return sum;
# nums = [5,4,5];
# result = sum_list(nums);
# print(result)
# ==============================================================================

# Q9. Write a python program to create a function to check whether a number falls in a given range.

# def func(num):
#     for i in range(min, max+1):
#         if num == i:
#             return True;
#     return False;

# min = int(input('Enter the min num: '));
# max = int(input('Enter the max num: '));
# num = int(input('Enter the num: '));
# ans = func(num)
# print(ans)
# ==============================================================================

# Q10. Write a python program to create a function to check whether a given number is even or odd.

# def check(nums):
#     if nums%2==0:
#         return True;
#     return False;
# num = int(input('Enter the num: '));
# ans = check(num);
# print(ans);
# ==============================================================================
