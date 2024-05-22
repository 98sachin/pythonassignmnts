'''
Assignment - 18 Full Stack Web Development using Python MySirG

Dictionary

1. Write a python program to create and print a dictionary which stores your information.
(name, age, gender .....)
2. Write a python program to access the items of a dictionary by referring to its key
name.
3. Write a python program to get a list of the values from a dictionary.
4. Write a python program to change the value of a specific item by referring to its key
name.
5. Write a python program to print all key names in the dictionary, one by one.
6. Write a python program to create a dictionary that contains three dictionaries.
(nested)
7. Write a python program to create three dictionaries, then create one dictionary that
will contain the other three dictionaries.
8. Write a python program to convert two lists into a dictionary in a way that item from
list1 is the key and item from list2 is the value.
9. Write a python program to merge two python dictionaries into one dictionary.
10. Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
'''

# Q1. Write a python program to create and print a dictionary which stores your information. (name, age, gender .....)

# d = {'name':'sachin', 'age':34, 'gender':'M'}
# print(d)
# print(type(d));
# ==============================================================================

# Q2. Write a python program to access the items of a dictionary by referring to its key name.

# d = {'name':'sachin', 'age':34, 'gender':'M'};
# print(d['name'], d['age'], d['gender']);
# ==============================================================================

# Q3. Write a python program to get a list of the values from a dictionary.

# d = {'name':'sachin', 'age':34, 'gender':'M'}

# l = list(d.values())
# print(l);
# ==============================================================================

# Q4. Write a python program to change the value of a specific item by referring to its key name.

# d = {'name':'sachin', 'age':34, 'gender':'M'}

# del d['age']  # first delete the element

# print(d)

# d['age']=26; # and the add it with the new value

# print(d)
# ==============================================================================

# Q5. Write a python program to print all key names in the dictionary, one by one.

# d = {'name':'sachin', 'age':34, 'gender':'M'};

# for i in d:
#     print(i);
# ==============================================================================

# Q6. Write a python program to create a dictionary that contains three dictionaries.(nested)

# d= {'val1':{"name":'sachin', 'class':12}, 'val2':{'roll_no.':23, 'section':'B'},'val3':{'age':17,'gender':'M'}};

# # print(d)
# print(d['val1'])
# ==============================================================================

# Q7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.

# d1 = {"name":'sachin', 'class':12};
# d2 = {'roll_no.':23, 'section':'B'};
# d3 = {'age':17,'gender':'M'}
# d4 = {'d1':d1, 'd2':d2, 'd3':d3}
# print(d4)
# ==============================================================================

# Q8. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.

# l1=['name','age','gender']
# l2=['sachin',25,'M']

# d = dict(zip(l1,l2))
# print(d)
# ==============================================================================

# Q9. Write a python program to merge two python dictionaries into one dictionary.

# d1 = {"name":'sachin', 'class':12};
# d2 = {'roll_no.':23, 'section':'B'};

# d1.update(d2);
# print(d1)
# ==============================================================================

# Q10. Write a python program to get the key of lowest value from the dictionary. sample_dict = {'C': 92,'Java': 66,'Python': 85}

sample_dict = {'C': 92,'Java': 66,'Python': 85}

key_of_lowest_value = min(sample_dict, key=lambda k: sample_dict[k])
print(key_of_lowest_value)
