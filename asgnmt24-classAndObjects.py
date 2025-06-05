'''Assignment - 24 

Classes and Objects

1. Write a python program to create a user class with 3 properties : name, age, email.
2. Write a python program to create a user class with a method to greet the user.
3. Write a python program to create 2 objects of the user class and assign different values.
4. Write a python program to init default values for user object using __init__ method.
5. Write a python program to delete the age property of the user.
6. Write a python program to create 3 user objects and find the youngest of all.
7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu, hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the values).
8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
order based on the ram size.
9. Write a python program to create a School class and 3 instance variables and 1 class
variable.
10. Define a class Employee with instance object variables empid, name, salary. Write
__init__() method in the class to initialize instance object variables. Also define
instance methods to input fields and display field values
'''

# Q1. Write a python program to create a user class with 3 properties : name, age, email.

# class User:
#     def __init__(self, name, age, email):
#         self.name = name;
#         self.age = age;
#         self.email = email;
# -------------------------------------------------------------------

# Q2. Write a python program to create a user class with a method to greet the user.

# class User:
#     def __init__(self, name, age, email):
#         self.name = name;
#         self.age = age;
#         self.email = email;

#     def greet(self):
#         print(f"Hello, {self.name}! Welcome on board.");
# -------------------------------------------------------------------

# Q3. Write a python program to create 2 objects of the user class and assign different values.

# class User: 
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email

#     def greet(self):
#         print(f"Hello, {self.name}! Welcome on board.")

# # Creating two objects of the User class with different values
# user1 = User("Betaal", 55, "asdf@asdf.com");
# user2 = User("Bheem", 45, "dddd@dddd.com");
# user1.greet();
# user2.greet();
# print(user1.name, user1.age, user1.email);
# print(user2.name, user2.age, user2.email);
# -------------------------------------------------------------------

# Q4. Write a python program to init default values for user object using __init__ method.

# class User:
#     def __init__(self, name="Default Name", age=0, email="default@email.com"):
#         self.name = name;
#         self.age = age;
#         self.email = email;
#     def greet(self):
#         print(f"Hello, {self.name}! Welcome on board.");
# # Creating an object of the User class with default values
# user_default = User();
# user_default.greet();
# print(user_default.name, user_default.age, user_default.email);
# # Creating an object of the User class with custom values
# user_custom = User("Custom Name", 30, "cust@om.com");
# user_custom.greet();
# print(user_custom.name, user_custom.age, user_custom.email);
# -------------------------------------------------------------------

# Q5. Write a python program to delete the age property of the user.

# class User:
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email
#     def greet(self):
#         print(f"Hello, {self.name}! Welcome on board.");
#     def delete_age(self):
#         if hasattr(self, 'age'):  # Check if the age property exists. The hasattr() function in Python is a built-in utility used to check if an object has a specific attribute. It takes two arguments: the object to be checked and the attribute name as a string. It returns True if the attribute exists and False otherwise. 
#             del self.age
#             print(f"Age property deleted for user {self.name}.")
#         else:
#             print(f"Age property does not exist for user {self.name}.")
# # Creating an object of the User class
# user = User("Chintu", 30, "chin@tu.com");
# user.greet();
# print(f"Before deletion: {user.name}, {user.age}, {user.email}");
# # Deleting the age property
# user.delete_age();
# # Attempting to access the deleted age property
# try:
#     print(f"After deletion: {user.name}, {user.age}, {user.email}");
# except AttributeError:
#     print(f"Age property has been deleted for user {user.name}.");
# -------------------------------------------------------------------

# Q6. Write a python program to create 3 user objects and find the youngest of all.

# class User:
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email

#     def greet(self):
#         print(f"Hello, {self.name}! Welcome on board.")

#     def __str__(self):
#         return f"User(name={self.name}, age={self.age}, email={self.email})"

# #     def __repr__(self):
# #         return f"User(name={self.name}, age={self.age}, email={self.email})"
# # Function to find the youngest user
# def find_youngest_user(users):
#     if not users:
#         return None
#     youngest = users[0]
#     for user in users[1:]:
#         if user.age < youngest.age:
#             youngest = user
#     return youngest
# # Creating three user objects
# user1 = User("Alice", 25, "aaa@aa.com")
# user2 = User("Bob", 22, "bbb@bb.com")
# user3 = User("Charlie", 30, "ccc@cc.om")
# # Adding the user objects to a list
# users = [user1, user2, user3]
# # Finding the youngest user
# youngest_user = find_youngest_user(users)
# if youngest_user:
#     print(f"The youngest user is: {youngest_user.name}, Age: {youngest_user.age}, Email: {youngest_user.email}")    
# else:
#     print("No users available to find the youngest.")
# -------------------------------------------------------------------

# Q7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu, hdd) and 2 methods (__init__() to initialize the values, showConfig() to print the values).

# class Laptop:
#     def __init__(self, brand, ram, cpu, hdd):
#         self.brand = brand
#         self.ram = ram
#         self.cpu = cpu
#         self.hdd = hdd

#     def showConfig(self):
#         print(f"Laptop Configuration:\nBrand: {self.brand}\nRAM: {self.ram}GB\nCPU: {self.cpu}\nHDD: {self.hdd}GB")
# # Creating three Laptop objects
# laptop1 = Laptop("Dell", 8, "Intel i5", 512)
# laptop2 = Laptop("HP", 16, "Intel i7", 1024)
# laptop3 = Laptop("Lenovo", 4, "Intel i3", 256)
# # Adding the Laptop objects to a list
# laptops = [laptop1, laptop2, laptop3]
# # Displaying the configurations of each laptop
# for laptop in laptops:
#     laptop.showConfig()
#     print()  # Print a newline for better readability
# -------------------------------------------------------------------

# Q8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted order based on the ram size.

# class Laptop:
#     def __init__(self, brand, ram, cpu, hdd):
#         self.brand = brand
#         self.ram = ram
#         self.cpu = cpu
#         self.hdd = hdd
#     def showConfig(self):
#         print(f"Laptop Configuration:\nBrand: {self.brand}\nRAM: {self.ram}GB\nCPU: {self.cpu}\nHDD: {self.hdd}GB")
#     def __lt__(self, other):
#         return self.ram < other.ram  # Compare based on RAM size
# # Creating three Laptop objects
# laptop1 = Laptop("Dell", 8, "Intel i5", 512)
# laptop2 = Laptop("HP", 16, "Intel i7", 1024)
# laptop3 = Laptop("Lenovo", 4, "Intel i3", 256)
# # Adding the Laptop objects to a list
# laptops = [laptop1, laptop2, laptop3]
# # Sorting the laptops based on RAM size
# laptops.sort()  # This will use the __lt__ method defined in the Laptop class
# # Displaying the configurations of each laptop in sorted order
# for laptop in laptops:
#     laptop.showConfig()
#     print()  # Print a newline for better readability
# -------------------------------------------------------------------

# Q9. Write a python program to create a School class and 3 instance variables and 1 class variable.

# class School:
#     school_name = "The Coding School"  # Class variable

#     def __init__(self, name, location, num_students):
#         self.name = name  # Instance variable
#         self.location = location  # Instance variable
#         self.num_students = num_students  # Instance variable

#     def show_info(self):
#         print(f"School Name: {self.school_name}")
#         print(f"Name: {self.name}")
#         print(f"Location: {self.location}")
#         print(f"Number of Students: {self.num_students}")
# # Creating three School objects
# school1 = School("TheCodingSchool1", "Bengaluru", 500)
# school2 = School("TheCodingSchool2", "Gurugram", 300)
# school3 = School("TheCodingSchool3", "Pune", 450)
# # Adding the School objects to a list
# schools = [school1, school2, school3]
# # Displaying the information of each school
# for school in schools:
#     school.show_info()
#     print()  # Print a newline for better readability
# -------------------------------------------------------------------

# Q10. Define a class Employee with instance object variables empid, name, salary. Write __init__() method in the class to initialize instance object variables. Also define instance methods to input fields and display field values.

# class Employee:
#     def __init__(self, empid, name, salary):
#         self.empid = empid
#         self.name = name
#         self.salary = salary

#     def input_fields(self):
#         self.empid = input("Enter Employee ID: ")
#         self.name = input("Enter Employee Name: ")
#         self.salary = float(input("Enter Employee Salary: "))

#     def display_fields(self):
#         print(f"Employee ID: {self.empid}")
#         print(f"Employee Name: {self.name}")
#         print(f"Employee Salary: {self.salary}")

# # Creating an Employee object
# employee = Employee("", "", 0.0)
# # Inputting fields for the employee
# employee.input_fields()
# # Displaying the employee's field values
# employee.display_fields()
# -------------------------------------------------------------------
