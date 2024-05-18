"""
Assignment - 6 Full Stack Web Development using Python MySirG

Decision Control

1. Write a python script to check whether a given number is positive or non-positive
2. Write a python script to check whether a given number is divisible by 5 or not
3. Write a python script to check whether a given number is even or odd
4. Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same.
5. Write a python script to print two given words in dictionary order
6. Write a python script to check whether a given number is a three digit number or not.
7. Write a python script to check whether a given number is positive, negative or zero.
8. Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots
9. Write a python script to check whether a given year is a leap year or not.
10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same.
11. Write a python script to take the month value in numeric format and display the
number of days in it.
12. Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part

"""
# Q1. Write a python script to check whether a given number is positive or non-positive.

# a=float(input('Enter a number: '));
# if (a>0):
#     print("The entered number is a positive number.");
# else:
#     print("The entered number is a negative number.");
# =================================================================

# Q2. Write a python script to check whether a given number is divisible by 5 or not.

# b=float(input("Enter a number: "));
# if b%5==0:
#     print("The entered number is divisible by 5.");
# else:
#     print("The entered number is not divisible by 5.");
# =================================================================

# Q3. Write a python script to check whether a given number is even or odd.

# c=float(input("Enter a number: "));
# if c%2==0:
#     print("The number is even.");
# else:
#     print("The number is odd.");
# =================================================================

# Q4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.

# d=float(input("Enter the first number: "));
# e=float(input("Enter the second number: "));
# if d>e:
#     print("The greater number is: ", d);
# elif e>d:
#     print("The greater number is: ",e);
# else:
#     print("Both the numbers are equal.");

#               OR

# print('Enter two numbers');
# d,e = int(input()) , int(input());
# print(d if d>e else e);
# =================================================================

# Q5. Write a python script to print two given words in dictionary order.

# f=str(input("Enter the 1st word: "));
# g=str(input("Enter the 2nd word: "));
# if f>g:
#     print(g,f);
# else:
#     print(f,g);

#          OR

# print('Enter two words');
# f,g = input() , input();
# print((g,f) if f>g else (f,g));
# =================================================================

# Q6. Write a python script to check whether a given number is a three digit number or not.

# h=int(input("Enter the number: "));
# if h>999 or h<100:
#     print("The number is not a 3 digit number.");
# else:
#     print("The number is a 3 digit number.");

#          OR

# h=int(input("Enter the number: "));
# if 99<h<1000:
#     print(h,' is a three digit number.');
# else:
#     print(h, ' is not a three digit number.');    
# =================================================================

# Q7. Write a python script to check whether a given number is positive, negative or zero.

# i=float(input('Enter a number: '));
# if i>0:
#     print("The number is Positive.");
# elif i<0:
#     print('The number is Negative');
# else:
#     print('The number is Zero.');
# =================================================================

# Q8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots.

# print('Enter the value of a,b and c of a quadratic equation: ');
# a,b,c=int(input()),int(input()),int(input());
# d=b**2-4*a*c;
# if d>0:
#     print('Real and distinct roots');
# elif d==0:
#     print('Real and equal roots');
# else:
#     print('Imaginary roots');
# =================================================================

# Q9. Write a python script to check whether a given year is a leap year or not.

# a leap year is always a multiple of 4. however one need to know that all the century years(1900, 1800, 2000 etc.) are divisible by 4 but not all the century years are leap year. So, if a particular year is not a century year than one can write a code for the year is divisible by 4 or not. But when the year is a century year then one need to check that the year is divisible by 400 or not.

# Below is the code for checking whether a non-century year is a leap year or not.
# j=int(input("Enter the year: "));
# if j%4==0:             
#     print(j," is a leap year.");
# else:
#     print(j," is not a leap year.");

# Below is the correct code
# print('Enter the year');
# year=int(input());
# if year%400==0 or year%100!=0 and year%4==0:
#     print("Leap year");
# else:
#     print('Non Leap year');

# =================================================================

# Q10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.

# k=float(input('Enter the 1st number: '));
# l=float(input('Enter the 2nd number: '));
# m=float(input('Enter the 3rd number: '));
# if (k>l and m):
#     print(k, " is the greatest number.");
# elif l>k and m:
#     print(l," is the greatest number.");
# elif m>l and k:
#     print(m, ' is the greatest number.');
# else:
#     print(k,'All the numbers are equal.');

#                   OR

# print('Enter three numbers');
# a,b,c=int(input()),int(input()),int(input());
# print((a if a>c else c)if a>b else (b if b>c else c) );

# =================================================================

# Q11. Write a python script to take the month value in numeric format and display the number of days in it.

# n=int(input('Enter the month number: '));
# match n:
#     case 1:
#         print('January:31 days');
#     case 2:
#         print('February:28/29(in a leap year) days.');
#     case 3:
#         print('March:31 days.');
#     case 4:
#         print('April:30 days.');
#     case 5:
#         print('May:31 days.');
#     case 6:
#         print('June:30 days.');
#     case 7:
#         print('July:31 days.');
#     case 8:
#         print('August:31 days.');
#     case 9:
#         print('September:30 days.');
#     case 10:
#         print('October:31 days.');
#     case 11:
#         print('November:30 days.');
#     case 12:
#         print('December:31 days.');
#     case _:
#         print('Enter a valid month number.')

            #   OR

# x=int(input('Enter month number: '));
# if x in (1,3,5,7,8,10,12):
#     print("31 days");
# elif x in (4,6,9,11):
#     print('30 days');
# elif x==2:
#     print('28 or 29(in a leap year) days');
# else:
#     print('Enter a valid year number');
# =================================================================

# Q12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part.

# x=complex(input('Enter a complex number: '));
# print(x.real if x.real>x.imag else x.imag);
# =================================================================