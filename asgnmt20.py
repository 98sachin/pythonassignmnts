'''
Assignment - 20 Full Stack Web Development using Python MySirG

More on functions

1. Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements.
2. Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not.
3. Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
4. Write a python program to create a function that checks whether a passed string is
palindrome or not.
5. Write a python program to create a function to find the Min of three numbers.
6. Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30.
7. Write a python program to access a function inside a function.
8. Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters.
9. Write a python program to create a function to check whether a string is a pangram
or not.
10. Write a python program to create a function to check whether a string is an anagram
or not.
'''

# Q1. Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.

# def unique_list(l):
#     return list(set(l))
# print(unique_list([1,2,3,3,3,3,4,5]))
# ==============================================================================

# Q2. Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.

# def prime(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         else:
#             return True
#     else:
#         return False
# print(prime(int(input("Enter a number: "))))
# ==============================================================================

# Q3. Write a python program to create a function that prints the even numbers from a given list. Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def func(nums):
#     for i in nums:
#         if i%2==0:
#             print(i)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9];
# func(list);
# ==============================================================================

# Q4. Write a python program to create a function that checks whether a passed string is palindrome or not.

# def palindrome(s):
#     return s == s[::-1]
# print(palindrome('malayalam'))
# ==============================================================================

# Q5. Write a python program to create a function to find the Min of three numbers.

# def func(min):
#         min_nums=min[0];
#         if min[1]<min[0]:
#                 min_nums=min[1];
#         elif min[2]<min[1]:
#                 min_nums=min[2];
#         return min_nums;

# lst = [24,33,44];
# print(func(lst)); 
# ==============================================================================

# Q6. Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.

# def func(nums):
#     for i in range(1,31):
#         nums.append(i**2)
#     return nums
# nums = []
# print(func(nums))
# ==============================================================================

# Q7. Write a python program to access a function inside a function.

# def func1():
#     def func2():
#         print("Hello")
#     func2()
# func1()
# ==============================================================================

# Q8. Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.

# def func(s):
#     upper = 0
#     lower = 0
#     for i in s:
#         if i.isupper():
#             upper += 1
#         elif i.islower():
#             lower += 1
#     return upper,lower
# s = "Hello World"
# print(func(s))
# ==============================================================================

# Q9. Write a python program to create a function to check whether a string is a pangram or not.

# def func(pan):
#     pan = pan.lower();
#     for i in "abcdefghijklmnopqrstuvwxyz":
#         if i not in pan:
#             return False;
#     return True;

# pangram = "The quick brown fox jumps over the lazy dog";
# print(func(pangram));
# ==============================================================================

# Q10. Write a python program to create a function to check whether a string is an anagram or not.

# def func(str1,str2):
#     str1 = str1.lower()
#     str2 = str2.lower()
#     if len(str1) != len(str2):
#         return False
#     else:
#         return sorted(str1) == sorted(str2)
# str1 = "hear"
# str2 = "hire"
# print(func(str1,str2))
# ==============================================================================