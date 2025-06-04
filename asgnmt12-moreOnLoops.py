'''
Assignment - 12

More on loops

1. Write a python script to reverse a number.
2. Write a python script to check whether a given number is Prime or not
3. Write a python script to print all Prime numbers under 100
4. Write a python script to print all Prime numbers between two given numbers (both
values inclusive)
5. Write a python script to find next prime number of a given number
6. Write a python script to print first N prime numbers
7. Write a python script to check whether a given pair of numbers are co-Prime
numbers or not.
8. Write a python script to print first N terms of a Fibonacci series
9. Write a python script to calculate LCM of two numbers
10. Write a python script to calculate HCF of two numbers
'''

#Q1. Write a python script to reverse a number.

# n=input('Enter a number: ');
# print('Reverse of',n,'is',n[::-1]);

# ================================================================

#Q2. Write a python script to check whether a given number is Prime or not.

# n=int(input('Enter a number: '));
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print(n,'is not a prime number');
#             break;
#     else:
#         print(n,'is a prime number');
# else:
#     print(n,'is not a prime number');
# ================================================================

#Q3. Write a python script to print all Prime numbers under 100

# for num in range(1, 101):
#     if all(num % i != 0 for i in range(2, num)):
#         print(num)

# Number = 1
# while Number <= 100:
#     count = 0
#     i = 2
#     while i <= Number // 2:
#         if Number % i == 0:
#             count += 1
#             break
#         i += 1
#     if count == 0 and Number != 1:
#         print(Number, end=' ')
#     Number += 1
# ================================================================

# Q4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)

# n1=int(input('Enter the number: '));
# n2=int(input('Enter the number: '));
# is_prime=True;
# if n1<n2:
#     for num in range(n1, n2+1):
#         if num > 1:
#             for i in range(2, int(num**0.5) + 1):
#                 if (num % i) == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 print(num, end=' ')
#             is_prime = True
# ================================================================

#Q 5. Write a python script to find next prime number of a given number.

# n = int(input('Enter a number: '))
# is_prime = False
# while not is_prime:
#     n += 1
#     is_prime = True
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
# if is_prime:
#     print(f'The next prime number is {n}')
# ================================================================

#Q 6. Write a python script to print first N prime numbers.

# n = int(input('Enter the number of prime numbers to print: '))

# if n <= 0:
#     print("Please enter a positive integer.")
# else:
#     count = 0
#     num = 2
#     while count < n:
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num, end=' ')
#             count += 1
#         num += 1
# ================================================================

#Q 7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not.

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def are_coprime(x, y):
#     return gcd(x, y) == 1

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if are_coprime(num1, num2):
#     print(f"{num1} and {num2} are co-prime numbers.")
# else:
#     print(f"{num1} and {num2} are not co-prime numbers.")

# Or in the simplest way check the code below:

# import math

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# if math.gcd(a, b) == 1:
#     print("The numbers are co-prime.")
# else:
#     print("The numbers are not co-prime.")
 
# ================================================================

# Q 8. Write a python script to print first N terms of a Fibonacci series.

# n = int(input("Enter the number of terms in the Fibonacci series: "))
# a, b = 0, 1
# print("Fibonacci series:")
# for _ in range(n):
#     print(a, end=' ')
#     a, b = b, a + b
# ================================================================

#Q 9. Write a python script to calculate LCM of two numbers

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# def lcm(a, b):
#     return abs(a * b) // gcd(a, b)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")
# ================================================================

#Q 10. Write a python script to calculate HCF of two numbers

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# def hcf(a, b):
#     return gcd(a, b)
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(f"The HCF of {num1} and {num2} is {hcf(num1, num2)}")
# ================================================================
