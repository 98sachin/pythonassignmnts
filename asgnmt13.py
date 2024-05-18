'''
Assignment - 13 Full Stack Web Development using Python MySirG

List

1. Write a python script to store multiple items in a single variable ( Items are “Java”
,“Python”, “SQL”, “C” ) using list.
2. Write a python script to get the data type of a list.
3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
4. Write a python script to Change the values "SQL" and "Reactnative" with the values
"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
"Javascript", "Python"]
5. Write a python script to add an item to the end of the list (item “Python”. (mylist =
["Java", "SQL", "C", "Reactnative"]
6. Write a python program to append elements from another list to the current list.(
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] )
7. Write a python program to Print all items by referring to their index number (thislist =
["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL",
"C", "Reactjs", "Javascript", "Python"]
9. Write a Python script to create a list of city names taken from the user.
10. Write a Python script to create a list, where each element of the list is a digit of a
given number.
'''
# Q1. Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using list.

# langs = ["Java", "Python", "SQL", "C"]
# print(langs)
# ==============================================================================

# Q2. Write a python script to get the data type of a list.

# langs = ["Java", "Python", "SQL", "C"];
# print(type(langs))
# ==============================================================================

# Q3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"]).

# mylist = ['Java', 'C', 'Python'];
# print(mylist[-1]);
# ==============================================================================

# Q4. Write a python script to Change the values "SQL" and "Reactnative" with the values"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]

# thislist = ['Java', 'SQL', 'C', 'Python', 'Reactnative', 'Javascript'];
# thislist[1]= 'NoSQl';
# thislist[4]= 'Flutter';
# print(thislist);
# ==============================================================================

# Q5. Write a python script to add an item to the end of the list (item “Python”. (mylist =["Java", "SQL", "C", "Reactnative"]

# mylist =["Java", "SQL", "C", "Reactnative"];
# mylist.append("Python");
# print(mylist);

# the code below is not the correct approach and thus throws an error

# mylist =["Java", "SQL", "C", "Reactnative"];
# mylist[4]='Python'
# print(mylist)
# ==============================================================================

# Q6. Write a python program to append elements from another list to the current list.(firstlist = ["Java", "Python", "SQL"]secondlist = ["C", "Cpp", "NoSQL"] )

# firstlist = ["Java", "Python", "SQL"];
# secondlist = ["C", "Cpp", "NoSQL"];

# print(firstlist.append(secondlist)) # this is not correct

# print(firstlist+secondlist) # this is the correct approach
# ==============================================================================

# Q7. Write a python program to Print all items by referring to their index number (thislist =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

# thislist =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"];
# print(thislist[0]);
# print(thislist[1]);
# print(thislist[2]);
# print(thislist[3]);
# print(thislist[4]);
# print(thislist[5]);

#      OR

# i=0;
# while i<=len(thislist):
#     print(thislist[i]);
#     i+=1;
# ==============================================================================

# Q8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]

# thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]

# print(sorted(thislist));
# ==============================================================================

# Q9. Write a Python script to create a list of city names taken from the user.

# n=int(input("how namy cities name you want to enter: "));
# cities=[];
# i=0;
# while i<=n:
#     cities.append(input("enter city name: "));
#     i+=1;
# print(cities);
# ==============================================================================

# Q10. Write a Python script to create a list, where each element of the list is a digit of a given number.


# n=int(input('enter a number: '))
# list = []
# while n>0:
#     list.append(n%10)
#     n = n//10
# print(list);