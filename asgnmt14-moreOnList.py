'''
Assignment - 14

More on List

1. Write a Python script to create a list of first N natural numbers.
2. Write a Python script to create a list of first N odd natural numbers.
3. Write a Python script to create a list of first N even natural numbers.
4. Write a Python script to find the greatest number in a given list of numbers.
5. Write a Python script to find the smallest number in a given list of numbers.
6. Write a Python script to calculate the sum of elements in a given list of numbers.
7. Write a Python script to remove all non int values from a list.
8. Write a Python script to print distinct elements along with their frequencies of
occurrence in the list.
9. Write a Python script to print indices of all occurrences of a given element in a given
list.
10. Write a python script to sort a list.
'''

# Q1. Write a Python script to create a list of first N natural numbers.

# n=int(input('Enter a number: '));
# list=[]
# i=1;
# while i<=n:
#     list.append(i);
#     i+=1;
# print(list);
# ==============================================================================

# Q2. Write a Python script to create a list of first N odd natural numbers.

# n=int(input('Enter a number: '));
# list=[]

# i=1;
# while i<=n:
#     if i%2!=0:
#         list.append(i);
#     i+=1;
# print(list);
# ==============================================================================

# Q3. Write a Python script to create a list of first N even natural numbers.

# n=int(input('Enter a number: '));
# list=[];
# i=1;
# while i<=n:
#     if i%2==0:
#         list.append(i);
#     i+=1;
# print(list);
# ==============================================================================

# Q4. Write a Python script to find the greatest number in a given list of numbers.

# n=int(input("How many numbers you want to enter in the list? "));
# list=[];
# i=0;
# while i<n:
#     list.append(int(input("Enter the number: ")));
#     i+=1;
# print("The list is: ",list);
# # print("The greatest number in the list is: ",max(list));

# #    OR

# list1 = sorted(list)
# print(list1)
# print(list1[-1]) # this will also give the greatest number.
# ==============================================================================

# Q5. Write a Python script to find the smallest number in a given list of numbers.

# n=int(input('How many numbers you want to add in the list? '));
# list=[];
# i=0;
# while i<n:
#     list.append(int(input('Enter the number: ')));
#     i+=1;
# print('The list is: ',list);
# # print('The smallest number in the list is: ',min(list));

# #      OR

# # l2 = sorted(list);
# # print(l2[0]);  # this will also give the smallest number.
# ==============================================================================

# Q6. Write a Python script to calculate the sum of elements in a given list of numbers.

# n=int(input('How many numbers you want to add in the list? ')); 
# list=[];
# i=1;
# while i<=n:
#     list.append(int(input('Enter the number: ')));
#     i+=1;
# print('The list is: ',list);

# sum=0;

# for j in list:
#     sum+=j;

# print('The sum of the list is: ',sum);
# ==============================================================================

# Q7. Write a Python script to remove all non int values from a list.

# l=[44,True,"sachin",False,87,87.9,"asfa"];

# print(l[1]);
# print(type(l[1]))

# for i in l:
#     if type(i) != int:
#         l.remove(i);
# print(l);
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ==============================================================================

# Q8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.

# l=[44,True,"sachin",False,87,87,87.9,"asfa","asfa","asfa"];

# for i in l:
#     if l.count(i)==1:
#      print(i);
# ==============================================================================

# Q9. Write a Python script to print indices of all occurrences of a given element in a given list.

# l=[44,True,"sachin",False,87,87,87.9,"asfa","asfa","asfa"];
# # print(l.index(87)); # this will not work
# ind = 0;
# for i in l:
#     if l.count(i)>1:
#         print (l.index(i))
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Q. 10. Write a python script to sort a list.

# l=[23,34,55,43,67,87,77,];
# l1=l.sort();
# print(l1)
