'''
Assignment - 15 Full Stack Web Development using Python MySirG

Strings

1. Write a python script to create a String in 3 different possible ways.
2. Write a python script to Get the characters from the start to position 5 (Given String
“iNeuron” using the slice syntax)
3. Write a python script to Get the characters from position 2 to position 5 (Given String
“Hello Learners” using the slice syntax)
4. Write a python script to demonstrate String Concatenation adding space in between (
Given Strings a=”Learning” b=”Python” )
5. Write a python script to get the count of total number of characters in String a=
“iNeuron”
6. Write a python script to reverse a String. (“iNeuron”)
7. Write a python script to determine whether a string contains a specific substring.
8. Write a python script to check if a string contains only numbers.
9. Write a python script to check if a string contains only characters of the alphabet.
10. Write a python script to convert an integer to a string.
'''

# Q1. Write a python script to create a String in 3 different possible ways.

# s1="String1";
# s2='String2';
# s3='''String3''';

# print(type(s1),type(s2),type(s3))
# ==============================================================================

# Q2. Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)

# s="iNeuron";
# print(s[0:5]);
# ==============================================================================

# Q3. Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)

# s="Hello Learners";
# print(s[2:5]);
# ==============================================================================

# Q4. Write a python script to demonstrate String Concatenation adding space in between (Given Strings a=”Learning” b=”Python” )

# a="Learning";
# b="Python";

# print(a+' '+b);
# ==============================================================================

# Q5. Write a python script to get the count of total number of characters in String a=“iNeuron”

# a="iNeuron";
# count=0;
# for i in a:
#     count=count+1;
# print(count);
# ==============================================================================

# Q6. Write a python script to reverse a String. (“iNeuron”).

# a="iNeuron";
# print(reversed(a)); #this will not give the answer

# print(a[::-1]);
# ==============================================================================

# Q7. Write a python script to determine whether a String is a palindrome or not. (Given String “iNeuron”)

# a="iNeuron";
# b=a[::-1];
# print(b);
# if a==b:
#     print("Palindrome");
# else:
#     print("Not a Palindrome");
# ==============================================================================

# Q7. Write a python script to determine whether a string contains a specific substring.

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# ===========================================================================

# Q8. Write a python script to check if a string contains only numbers.

# a='12345'
# b='12345a'

# c='12345a'
# if a.isdigit():
#     print('yes')
# else:
#     print('no')
# ==============================================================================

# Q9. Write a python script to check if a string contains only characters of the alphabet.

# a='asde234f'
# b='asde234f'
# if a.isalpha():
#     print('yes')
# else:
#     print('no')
# ==============================================================================

# Q10. Write a python script to convert an integer to a string.

# a=23423;
# b=str(a)
# print(b);