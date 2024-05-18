"""
Assignment - 7 Full Stack Web Development using Python MySirG

Match Case

1. Write a python script to display the number of days in a given month number.
2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division
3. Write a menu driven program with the following options:
    a. Check whether a given set of three numbers are lengths of an isosceles
    triangle or not
    b. Check whether a given set of three numbers are lengths of sides of a right
    angled triangle or not
    c. Check whether a given set of three numbers are equilateral triangle or not
    d. Exit.
4. Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen.
5. Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.
6. Write a python program to check whether a given string is a multiword string or single
word string using match case statement
7. Write a python program to check whether a given number is positive, negative or
zero using match case statement
8. Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement
9. Write a python script to check whether a given year is
    a. Non century leap year
    b. Century leap year
    c. Non century non leap year
    d. Century non leap year
10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
    a. Yellow - Monday
    b. Blue - Tuesday
    c. Orange - Wednesday
    d. White - Thursday
    e. Black - Friday
    f. Red - Saturday
    g. All other colours - Sunday

"""

# Q1. Write a python script to display the number of days in a given month number.

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
#         print('Enter a valid month number.');

#                   OR

# month=int(input('Enter month number: '));
# match month:
#     case month if month in (1,3,5,7,8,10,12):
#         print('31 days');
#     case month if month in (4,6,9,11):
#         print('30 days');
#     case 2:
#         print('28 or 29(in a leap year) days');
#     case _:
#         print('Enter a valid month number');

# =================================================================

# Q2. Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division.

# print('Press 1 for Addition');
# print('Press 2 for Subtraction');
# print('Press 3 for Multiplication');
# print('Press 4 for Division');
# print('Enter your choice');
# choice=int(input());
# match choice:
#     case 1:
#         print('Enter two numbers');
#         a,b=float(input()), float(input());
#         c=a+b;
#         print('Sum is ',c);
#     case 2:
#         print('Enter two numbers');
#         a,b=float(input()), float(input());
#         c=a-b;
#         print('Difference is ',c);
#     case 3:
#         print('Enter two numbers');
#         a,b=float(input()), float(input());
#         c=a*b;
#         print('Product is ',c);
#     case 4:
#         print('Enter two numbers');
#         a,b=float(input()), float(input());
#         c=a/b;
#         print('Division is ',c);
#     case _:
#         print('Invalid choice');

# =================================================================

# Q6. Write a python program to check whether a given string is a multiword string or single word string using match case statement.

# s=input('Enter the string: ');
# s.strip()

# match s:
#     case s if ' ' in s:
#         print('Multi-word string');
#     case s if ' ' not in s:
#         print('Single word string')

# check once

# =================================================================

# Q8. Write a python script to check whether two given strings are identical, first string comes before the second in dictionary order or first string comes after the second string in dictionary order using match case statement.

# s1=input('Enter 1st string: ');
# s2=input('Enter 2nd string: ');
# match (s1,s2):
#     case (s1,s2) if s1==s2:
#         print('Identical strings');
#     case (s1,s2) if s1>s2:
#         print('{} comes after {}'.format(s1,s2));
#     case (s1,s2) if s2>s1:
#         print('{} comes after {}'.format(s2,s1));
# print()
# =================================================================

# Q10. Write a program to display day name on the basis of user’s liking of a colour. Ask user for his favorite colour. User can answer in a sentence like “I like red colour”.
# Assuming all colour name entered by user is in lowercase. Use match case to display day name associated with the colour.
#     a. Yellow - Monday
#     b. Blue - Tuesday
#     c. Orange - Wednesday
#     d. White - Thursday
#     e. Black - Friday
#     f. Red - Saturday
#     g. All other colours - Sunday

# s1=input('What is your favourite colour? ');
# l1=["yellow", "blue", "orange", "white", "black", 'red', 'other'];
# for colour in l1:
#     if colour in s1:
#         c=colour;
#         break;
# else:
#     c='other';

# match c:
#     case 'yellow':
#         print('Monday');
#     case 'blue':
#         print('Tuesday');
#     case 'orange':
#         print('Wednesday');
#     case "white":
#         print('Thursday');
#     case 'black':
#         print('Friday');
#     case 'red':
#         print('Saturday');
#     case 'other':
#         print('Sunday');
# print()
# =================================================================