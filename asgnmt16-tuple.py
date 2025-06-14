'''
Assignment - 16 

Tuple

1. Write a python script to store multiple items in a single variable ( Items are “Java”
,“Python”, “SQL”, “C” ) using tuple
2. Write a python program to store only one item using tuple.
3. Write a python program to reverse the tuple.
4. Write a python program to Swap two tuples in Python.
5. Write a python program to check if all items in the tuple are the same.
6. Write a python program to divide the tuple into four variables.
tuple1=(100, 200, 300, 400)
7. Write a python program to copy elements 4 and 5 from the following tuple into a new
tuple. tuple1=(1,2,3,4,5,6)
8. Write a python program to Sort a tuple of tuples by the second item.
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
9. Write a python program to print the value 20 from given nested tuple
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
10. Write a python program to change the first item (22) of a list within the following tuple
to 222.
tuple1 = (11, [22, 33], 44, 55)
'''

# Q1. Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using tuple

# a = ("Java", "Python", "SQL", "C");
# print(a);
# print(type(a));

# ==============================================================================

# Q2. Write a python program to store only one item using tuple.

# a = ("C",) #the comma is important in tuple.
# or
# a=(3,)
# print(a);
# print(type(a));
# ==============================================================================

# Q3. Write a python program to reverse the tuple.

# a= ("Java", "C", 78, 89.5, True);
# print(type(a))
# b = a[::-1];
# print(b)
# ==============================================================================

# Q4. Write a python program to Swap two tuples in Python.

# a=(54, "john")
# b=(78, "mary")
# c=a;
# a=b;
# b=c;
# print(a);
# print(b);
# ==============================================================================

# Q5. Write a python program to check if all items in the tuple are the same.

# t=(23,24,23);

# for i in range(1,(len(t))):
#     if t[0]!=t[i]:
#         print('the items in t are not equal');
#         break;
#     else:
#         print('the items in t are equal');
#         break;
# ==============================================================================

#Q6.Write a python program to divide the tuple into four variables.tuple1=(100, 200, 300, 400)

# tuple1=(100, 200, 300, 400)
# a,b,c,d=tuple1;
# print(a,b,c,d)
# ==============================================================================

# Q7. Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)


# tuple1=(1,2,3,4,5,6);
# tuple2=tuple1[3:6];
# print(tuple2)
# ==============================================================================

# Q.8. Write a python program to Sort a tuple of tuples by the second item.tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

# tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29));


# t = sorted(tuple1[2])
# print(t)
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxX

# Q9. Write a python program to print the value 20 from given nested tuple tuple1 = ("Python", [10, 20, 30], (2, 4, 16))

# tuple1 = ("Python", [10, 20, 30], (2, 4, 16))

# print(tuple1[1][1])
# ==============================================================================

# Q10. Write a python program to change the first item (22) of a list within the following tuple to 222. tuple1 = (11, [22, 33], 44, 55)

# tuple1 = (11, [22, 33], 44, 55)

# tuple1[1][0]=222;

# print(tuple1)
