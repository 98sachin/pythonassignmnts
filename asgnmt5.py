"""
Assignment - 5 Full Stack Web Development using Python MySirG

Operators

1. Write a python script to remove the last digit from a given number. (for example, if
user enters 2534 then your output should be 253)
2. Write a python script to get the last digit from a given number. (for example, if user
enters 2089 then your output should be 9)
3. Write a python script to swap data of two variables
4. Write a python script to find x power y, where values of x and y are given by user
5. Write a python script which takes a three digit number from the user and displays
only its first digit.
6. Write a python script which takes a three digit number from the user and displays
only its middle digit.
7. Write a python script which takes a three digit number from the user and displays
only its last digit.
8. Write a python script to use IN operator to display the data present in the list
9. Write a python script to use NOT IN operator to display the data not present in list
10. Write a python script to use IS operator to display if both variables are the same
object or not?

"""

# Q1. Write a python script to remove the last digit from a given number. (for example, if
# user enters 2534 then your output should be 253).

# a=str(input("Enter a number: "));
# print(int(a[:-1]));

#       OR

# a=int(input('Enter the number: '));
# print(a//10);

#       OR

# a=int(input('Enter the number: '));
# print(int(a/10));


# =================================================================

# Q2. Write a python script to get the last digit from a given number. (for example, if user
# enters 2089 then your output should be 9).

# b=str(input("Enter a number: "));
# print(int(b[-1:]));

#         OR

# b=int(input('Enter the number: '));
# print(b%10);
# =================================================================

# Q3. Write a python script to swap data of two variables.

# c=23;
# d='sachin';   # the 3rd variable can be temp or flag.
# e=c;
# c=d;
# d=e;
# print("the value of c is: ",c);
# print("the value of d is: ",d);

#           OR

# num_1=float(input('Enter the 1st number: '));
# num_2=float(input('Enter the 2nd number: '));
# num_1 , num_2 = num_2 , num_1;
# print('The new value of num_1:', num_1);
# print('The new value of num_2:', num_2);
# =================================================================

# Q4. Write a python script to find x power y, where values of x and y are given by user.

# x=int(input('Enter the 1st number: '));
# y=int(input('Enter the 2nd number: '));
# print(x**y);
# =================================================================

# Q5. Write a python script which takes a three digit number from the user and displays only its first digit.

# q=str(input('Enter a 3 digit number: '));
# print(int(q[0]));

#         OR

# q=int(input('Enter a 3 digit number: '));
# print(q//100);
# =================================================================

# Q6. Write a python script which takes a three digit number from the user and displays only its middle digit.

# w=str(input("Enter a 3 digit number: "));
# print(int(w[1]));

#         OR

# w=int(input("Enter a 3 digit number: "));
# x=w//10;
# print(x%10);
# =================================================================

# Q7. Write a python script which takes a three digit number from the user and displays only its last digit.

# w=str(input("Enter a 3 digit number: "));
# print(int(w[-1]));
# =================================================================

# Q8. Write a python script to use IN operator to display the data present in the list.

# r=str(input("Enter the characters here: "));
# print(str(input('Search for the character: ') in r));
# =================================================================

# Q9. Write a python script to use NOT IN operator to display the data not present in list.

# s=str(input("Enter the characters here: "));
# print(str(input('Search for the character: ') not in s));
# =================================================================

# Q10. Write a python script to use IS operator to display if both variables are the same object or not?

# t=34;
# y=34;
# print(t is y);

