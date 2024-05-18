"""
Assignment - 10 Full Stack Web Development using Python MySirG

 for loop and range

1. Write a python script to print the first 10 multiples of 5.
2. Write a python script to print first 10 multiples of N
3. Write a python script to print first M multiples of N.
4. Write a python script to print the first 10 multiples of N in reverse order.
5. Write a python script to print table of user’s choice
6. Write a python script to print first N even natural numbers.
7. Write a python script to print first N odd natural numbers.
8. Write a python script to print squares of first N natural numbers.
9. Write a python script to print cubes of first N natural numbers.
10. Write a python script to display all prime numbers within a range.
# range
start = 15
end = 45
"""

# Q1. Write a python script to print the first 10 multiples of 5.

# for i in range(1, 11):
#     print(i * 5, end=" ")

# # print()
# ===========================================================================

# Q2. Write a python script to print first 10 multiples of N.

# n=int(input("Enter a number: "));
# for i in range(1,11):
#     print(n*i, end=" ");
# ===========================================================================

# Q3. Write a python script to print first M multiples of N.

# n=int(input("Enter a number: "))
# m=int(input("Enter the no. of miltiples: "))

# for i in range(1,m+1):
#     print(n*i, end=" ");
# ===========================================================================

# Q4. Write a python script to print the first 10 multiples of N in reverse order.

# n=int(input("Enter a number: "));

# for i in range(10,0,-1):
#     print(n*i, end=" ");
# ===============================================================================

# Q5. Write a python script to print table of user’s choice

# n=int(input("Enter a number for table: "));

# for i in range(1,11):
#     print(n*i, end=" ");
# ===============================================================================

# Q6. Write a python script to print first N even natural numbers.

# n=int(input("Enter a number: "));

# for i in range(1,n+1):
#     print(i*2,end=" ")
# ===============================================================================

# Q7. Write a python script to print first N odd natural numbers.

# n=int(input("Enter a number: "));
# for i in range(n):
#     print(i*2+1, end=" ")

# OR

# n=int(input("Enter a number: "));
# for i in range(n):
#     j=i+1;
#     print(j+i,end=" ");
# ==============================================================================

# Q8. Write a python script to print squares of first N natural numbers.

# for i in range(int(input("Enter a number: "))):
#     print((i+1)**2,end=" ")
# ==============================================================================

# Q9. Write a python script to print cubes of first N natural numbers.

# for i in range(int(input("Enter a number: "))):
#     print((i+1)**3,end=" ");
# ==============================================================================

# Q10. Write a python script to display all prime numbers within a range.

# l=int(input("Enter a lower number: "));
# u=int(input("Enter a upper number: "));

# for i in range(l,u+1):
#     if i>1:
#         for j in range(2,i):
#             if(i%j)==0:
#                 break;
#     else:
#             print(i,end=" ");