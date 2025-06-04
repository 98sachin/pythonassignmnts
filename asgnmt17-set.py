'''
Assignment - 17

Set

1. Write a python program to store all the programming languages known to you using
Set.
2. Write a python program to store your own information {name, age, gender, so on..}
3. Write a python script to get the data type of a Set.
4. Write a Python script to find if “Python” is present in the set thisset = {"Java",
"Python", "Django"}
5. Write a python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
6. Write a python program to add elements of list to a set
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
7. Write a python program to remove last item of the given set
thisset = {"Python", "Django", "JavaScript", “SQL”}
8. Write a python program to delete the set completely.
9. Write a python program to loop through the set and print values
thisset = {"Python", "Django", "JavaScript", “SQL”}
10. Write a python program to find the maximum and minimum value in a set.
'''

# Q1. Write a python program to store all the programming languages known to you using Set.

# set = {"C", "C++", "Java","Python", "Javascript","Go", "PHP", "Flutter","Rust"}
# print(set)
# print(type(set))

# ==============================================================================

# Q2. Write a python program to store your own information {name, age, gender, so on..}

# myInfo = {"Sachin", 26, "M", "Python developer"}
# print(myInfo)
# print(type(myInfo))
# ==============================================================================

# Q3. Write a python script to get the data type of a Set.

# myInfo = {"Sachin", 26, "M", "Python developer",False}

# for i in myInfo:
#     print(type(i));
# ==============================================================================

# Q4. Write a Python script to find if “Python” is present in the set thisset = {"Java", "Python", "Django"}

# thisset = {"Java", "Python", "Django"}

# if "Python" in thisset:
#     print("Yes, Python is present in the set")
# else:
#     print("No, Python is not present in the set")
# ==============================================================================

# Q5. Write a python program to add items from another set to the current set. thisset ={"Java", "Python", "SQL"} secondset= {"C", "Cpp", "NoSQL"}

# thisset = {"Java", "Python", "SQL"}
# secondset= {"C", "Cpp", "NoSQL"}

# thisset.update(secondset)
# print(thisset)
# ==============================================================================

# Q6. Write a python program to add elements of list to a set thisset = {"Python", "Django", "JavaScript"} mylist = ["Java", "C"]

# thisset = {"Python", "Django", "JavaScript"}
# mylist = ["Java", "C"]

# thisset.update(mylist)
# print(thisset)
# ==============================================================================

# Q7. Write a python program to remove last item of the given set thisset = {"Python", "Django", "JavaScript", “SQL”}

# thisset = {"Python", "Django", "JavaScript", "SQL"}

# thisset.remove('SQL')
# print(thisset)
# ==============================================================================

# Q8. Write a python program to delete the set completely.

# thisset = {"Python", "Django", "JavaScript", "SQL"}

# print(thisset)


# del thisset
           
           
# print(thisset)
# ==============================================================================

# Q9. Write a python program to loop through the set and print values thisset = {"Python", "Django", "JavaScript", “SQL”}

# thisset = {"Python", "Django", "JavaScript", "SQL"}

# for i in thisset:
#     print(i)
# ==============================================================================

# Q10. Write a python program to find the maximum and minimum value in a set.

set = {34,45,233,56,34,87,43,65}

print(max(set));
