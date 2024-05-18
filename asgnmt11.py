"""
Assignment - 11 Full Stack Web Development using Python MySirG

loops

1. Write a python script to calculate sum of first N natural numbers
2. Write a python script to calculate sum of squares of first N natural numbers
3. Write a python script to calculate sum of cubes of first N natural numbers
4. Write a python script to calculate sum of first N odd natural numbers
5. Write a python script to calculate sum of first N even natural numbers
6. Write a python script to calculate factorial of a given number
7. Write a python script to count digits in a given number
8. Write a python script to calculate sum of digits of a given number
9. Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)
10. Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)

"""

# Q1. Write a python script to calculate sum of first N natural numbers.

# n=int(input("Enter a number: "));
# sum=0;
# for i in range(1,n+1):
#     sum=sum+i;

# print("Sum of first",n,"natural numbers is: ",sum);

# ================================================================

#Q2. Write a python script to calculate sum of squares of first N natural numbers.

# n=int(input('Enter a number: '));
# sum=0;
# for i in range(1,n+1):
#     sum+=(i*i)

# print("Sum of squares of first",n,"natural numbers is: ",sum);
# ================================================================

#Q3. Write a python script to calculate sum of cubes of first N natural numbers.

# n=int(input('Enter the number: '));
# sum=0;
# for i in range(1,n+1):
#     sum+=(i*i*i)

# print("Sum of cubes of first",n,"natural numbers is: ",sum);
# ================================================================

#Q4. Write a python script to calculate sum of first N odd natural numbers.

# n=int(input('Enter a number: '));
# sum=0;
# for i in range(1,n+1,2):
#     sum+=i;

# print("Sum of first",n,"odd natural numbers is: ",sum);
# ================================================================

#Q5. Write a python script to calculate sum of first N even natural numbers.

# n=int(input('Enter a number: '));
# sum=0;
# for i in range(2,n+1,2):
#     sum+=i;

# print("Sum of first",n,"even natural numbers is: ",sum);
# ================================================================

#Q6. Write a python script to calculate factorial of a given number.

# n=int(input('Enter a number: '));
# fact=1;
# for i in range(1,n+1):
#     fact*=i;

# print("Factorial of",n,"is: ",fact);
# ================================================================

#Q7. Write a python script to count digits in a given number.

# n=input('Enter a number to know the digits in it: ');
# print("Number of digits in",n,"is: ",len(n));

# ================================================================

#Q8. Write a python script to calculate sum of digits of a given number.

# n=input('Enter a number to know the sum of digits in it: ');
# sum=0;
# for i in n:
#     sum+=int(i);
# print(sum);
# ================================================================

#Q9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method).

# n=int(input('Enter a number: '));
# binary='';
# while n>0:
#     binary=str(n%2)+binary;
#     n=n//2;
# print("Binary equivalent of",n,"is: ",binary);

# ================================================================

#Q10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method).

# n=int(input('Enter a number: '));
# octal='';
# while n>0:
#     octal=str(n%8)+octal;
#     n=n//8;   
# print("Octal equivalent of",n,"is: ",octal);
