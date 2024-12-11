![My Image](image.png)

# **Day 1: Introduction to Object-Oriented Programming (OOP) with Python** 
---

## **Table of Contents**  

1. [Session Objectives](#session-objectives)  
2. [Session Outline](#session-outline)  
   - [Part 1: Introduction to Object-Oriented Programming (OOP)](#part-1-introduction-to-object-oriented-programming-oop)  
     - What is OOP?  
     - Everything in Python is an Object  
     - Creating a Class  
     - Creating an Object  
     - Class Constructor  
     - Using Multiple Parameters in the Constructor  
     - Real-Life Analogy  
     - Code Example: Dog Class  
   - [Part 2: Understanding Classes and Objects](#part-2-understanding-classes-and-objects)  
     - Class vs. Object  
     - Code Example: Car Class  
     - Exercise: Create Student and Phone Classes  
   - [Part 3: The `__init__` Method (Constructor)](#part-3-the-init-method-constructor)  
     - Understanding the Constructor Method  
     - Code Example: Book Class  
     - Exercise: Create a Laptop Class  
   - [Part 4: Adding Methods to Classes](#part-4-adding-methods-to-classes)  
     - Defining Methods  
     - Code Example: Calculator Class  
     - Exercise: Create BankAccount Class  
   - [Part 5: Default Values in Classes](#part-5-default-values-in-classes)  
     - Using Default Values in Class Attributes  
     - Code Example: Person Class with Defaults  
     - Exercise: Create Pet Class with Default Values  
   - [Part 6: Modifying Attributes Dynamically](#part-6-modifying-attributes-dynamically)  
     - Modifying Attributes After Object Creation  
     - Code Example: Person Class with Dynamic Skills  
     - Exercise: Create Student Class with Dynamic Subjects  
3. [Key Takeaways](#key-takeaways)  
4. [Homework](#homework)  
   - Library Class  
   - Shape Class  

---

## **Session Objectives**  

- Understand the fundamental concepts of Object-Oriented Programming (OOP).  
- Learn how to create and use classes and objects in Python.  
- Explore the `__init__` constructor method and basic object methods.  
- Gain hands-on experience with OOP concepts through practical examples and exercises.  

---

## **Session Outline**  

### **Part 1: Introduction to Object-Oriented Programming (OOP)**  

#### **Objective**  
Grasp the core idea of OOP through relatable real-life analogies and practical examples.  

#### **Explanation**  
1. **What is OOP?**  
   - OOP is a programming paradigm that organizes code into **objects**.  
   - **Objects** represent real-world entities with **attributes** (characteristics) and **methods** (actions).  
   - Everything in Python is an object, including numbers, strings, lists, and dictionaries.  


#### **Everything in Python is an Object**  

In Python, every element is an object of a specific class. 
```python
>>> num = 10
>>> type(num)
<class 'int'>

>>> string = 'Hello, World!'
>>> type(string)
<class 'str'>

>>> lst = []
>>> type(lst)
<class 'list'>
```  

Every variable here is an object of a corresponding class.  

 ```python
   x = 5  # x is an integer object
   y = "Hello"  # y is a string object
   print(x.bit_length())  # Method of the integer object
   print(y.upper())  # Method of the string object
   ```
   ---

Every variable here is an object of a corresponding class.  

---
### **Part 2: Understanding Classes and Objects**  


#### **Explanation**  
- **Class**: A blueprint or template for creating objects (e.g., "Car"). 
- Data structure defined by user. 
- **Object**: A specific instance of the class (e.g., "Red Toyota Corolla, 2020").  

### **Creating a Class**  

To create a class, use the `class` keyword, followed by the class name in **CamelCase** format.  

```python
class Person:
    pass
```

This defines an empty class.  

---

### **Creating an Object**  

You can create an object by calling the class as if it were a function.  

```python
p = Person()
print(p)
```

This creates an object `p` of the `Person` class.  

---

### **Part 3: The `__init__` Method (Constructor)**  

#### **Objective**  
Understand how the `__init__` method initializes object attributes during object creation.  

#### **Explanation**  
A class constructor is defined using the `__init__()` method. It initializes object attributes. The `self` parameter refers to the object itself.  
- The `__init__` method is a special method that runs automatically when a new object is created.  
- It sets initial values for object attributes.  



```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person('Selam')
print(p.name)  # Output: Selam
```

In this case, the `name` is assigned to the object's `name` attribute.  

---

### **Using Multiple Parameters in the Constructor**  

You can pass multiple parameters to the constructor to set more attributes.  

```python
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = Person('Selam', 'Yetayeh', 25, 'Finland', 'Helsinki')
print(p.firstname)  # Output: Selam
print(p.lastname)   # Output: Yetayeh


```
### **3. Attributes: Class and Instance Variables**

In Python, attributes can be categorized as **instance attributes** and **class attributes**. Here’s a detailed explanation with examples:

---

### **Instance Attributes**
- **Definition**: Attributes unique to each object.
- **Scope**: Defined and accessed through a specific object.
- **Declaration**: Typically defined in the `__init__` method using `self`.

#### **Example of Instance Attributes**:
```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    

# Creating two objects of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing instance attributes
print(person1.name, person1.age)  # Output: Alice 25
print(person2.name, person2.age)  # Output: Bob 30

# Modifying instance attributes
person1.age = 26
print(person1.age)  # Output: 26
```

---

### **Class Attributes**
- **Definition**: Attributes shared across all objects of a class.
- **Scope**: Same for all instances of the class.
- **Declaration**: Defined directly in the class (outside methods).

#### **Example of Class Attributes**:
```python
class Car:
    wheels = 4  # Class attribute

    def __init__(self, make, model):
        self.make = make  # Instance attribute
        self.model = model  # Instance attribute

# Creating two objects of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing class attributes
print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4

# Accessing instance attributes
print(car1.make, car1.model)  # Output: Toyota Corolla
print(car2.make, car2.model)  # Output: Honda Civic

# Modifying the class attribute
Car.wheels = 5
print(car1.wheels)  # Output: 5
print(car2.wheels)  # Output: 5
```

---

### **Key Differences**
| Feature                | Instance Attribute                     | Class Attribute                    |
|------------------------|----------------------------------------|------------------------------------|
| **Scope**              | Specific to each object.              | Shared across all objects.        |
| **Definition**         | Inside `__init__` (or methods).       | Directly in the class body.       |
| **Access**             | Accessed via `self.attribute`.        | Accessed via `ClassName.attribute`. |
| **Modification**       | Changes affect only the object.       | Changes affect all objects.       |

---

### **Combining Class and Instance Attributes**
```python
class Employee:
    company_name = "TechCorp"  # Class attribute

    def __init__(self, name, position):
        self.name = name  # Instance attribute
        self.position = position  # Instance attribute

# Creating objects
emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Manager")

# Accessing both attributes
print(emp1.name, emp1.position, Employee.company_name)  # Output: Alice Developer TechCorp
print(emp2.name, emp2.position, emp2.company_name)  # Output: Bob Manager TechCorp
```

---

### ** Questions**

1. Create a `Person` class to store a person's name, age, and a list of their favorite colors. Instantiate the class and display the person's name, age, and all the favorite colors.

2. Define a `Library` class to store the library's name, location, and a list of available books (titles). Display the library name, location, and all the book titles.

3. Build a `Student` class that holds a student's name, age, grades (in a dictionary), and enrolled courses (a list). Create an instance of a student and print their name, age, and grades.
4. Implement a `Product` class to accept name, price, and manufacturing date. Display all the product details. 
5. Create a `Car` class to store the car's brand, model, year, and a list of service dates. Instantiate the class with a car’s information and print all details, including the car's brand, model, year, and service dates.

6. Implement a `School` class to store the school's name, the number of students, and a dictionary of student names with their respective grades. Display the school's name, the number of students, and the students with their grades.
 
---

### **Part 4: Adding Methods to Classes**

---
### **Methods**
Methods define the behavior of objects. They can perform actions using the object’s attributes.  

#### **Code Example: Dog Class**  
```python
class Dog:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
    
    def bark(self):
        return "Woof! Woof!"

dog1 = Dog("Labrador", "Black")
print(dog1.breed)  # Output: Labrador
print(dog1.bark())  # Output: Woof! Woof!
  ```

---
### Different types of methods to add functionality to classes, including **instance methods**, **class methods**, and **static methods**.

---

### **Concept 1: Instance Methods**

#### **Definition**:
- Operate on **instance attributes** (unique to each object).
- Require `self` as the first parameter to refer to the instance.

#### **Code Example: Calculator Class**  

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(3, 5))  # Output: 8
print(calc.multiply(4, 6))  # Output
```
---

### **Concept 2: Class Methods**

#### **Definition**:
- Operate on **class attributes** (shared across all objects).
- Use the `@classmethod` decorator.
- Require `cls` as the first parameter to refer to the class.

#### **Code Example: Employee Management**
```python
class Employee:
    company_name = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name
        return f"Company name changed to {cls.company_name}"

# Accessing and modifying class attributes using class methods
print(Employee.company_name)  # Output: TechCorp
print(Employee.change_company_name("InnovateTech"))  # Output: Company name changed to InnovateTech
print(Employee.company_name)  # Output: InnovateTech
```

---

### **Concept 3: Static Methods**

#### **Definition**:
- Do **not** operate on instance or class attributes.
- Use the `@staticmethod` decorator.
- Do not require `self` or `cls`.

#### **Code Example: Utility Methods**
```python
class MathUtility:
    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def is_even(number):
        return number % 2 == 0

# Calling static methods
print(MathUtility.add_numbers(5, 10))  # Output: 15
print(MathUtility.is_even(4))  # Output: True
```

---

### **Summary of Method Types**

| **Method Type**  | **Decorator**   | **First Parameter** | **Purpose**                     |
|-------------------|-----------------|---------------------|---------------------------------|
| Instance Method   | None            | `self`              | Operates on instance attributes |
| Class Method      | `@classmethod`  | `cls`               | Operates on class attributes    |
| Static Method     | `@staticmethod` | None                | General utility or independent functionality |

---

### **Practice Example: Student Management System**
Write a class `Student` with the following:
1. An instance method `add_marks(self, subject, marks)` to add marks for a subject.
2. A class method `set_school(cls, school_name)` to change the school name.
3. A static method `is_passing(marks)` to check if marks are above 50.

#### **Solution**:
```python
class Student:
    school_name = "Global High School"

    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks
        return f"Added {marks} for {subject}."

    @classmethod
    def set_school(cls, school_name):
        cls.school_name = school_name
        return f"School name updated to {cls.school_name}."

    @staticmethod
    def is_passing(marks):
        return marks > 50

# Example Usage
student = Student("John Doe")
print(student.add_marks("Math", 75))  # Output: Added 75 for Math.
print(Student.set_school("Future Academy"))  # Output: School name updated to Future Academy.
print(Student.is_passing(75))  # Output: True
print(Student.is_passing(45))  # Output: False
```


---


### **Part 5: Default Values in Classes**  

#### **Objective**  
Learn how to provide default values for class attributes and handle scenarios where no arguments are passed.  

#### **Code Example: Person Class with Defaults**  

```python
class Person:
    def __init__(self, firstname='John', lastname='Doe', age=30, country='USA'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old from {self.country}.'

# Using default values
p1 = Person()
print(p1.person_info())  # Output: John Doe is 30 years old from USA.

# Overriding default values
p2 = Person('Alice', 'Smith', 25, 'Canada')
print(p2.person_info())  # Output: Alice Smith is 25 years old from Canada.
```  

---
### **Easy Questions**

1. Create a `Book` class that stores the title, author, and publication year. Add a method to display the book's details.
3. Create an Animal class with an instance method describe to return the animal's name and species, a class method display_class_info , and a static method is_domestic to check if a species is domestic or wild.
3. Design a `Company` class with attributes for name, industry, and founding year. Write a method to display the company's details and another method to calculate its age based on the current year.
---

### **Mid-Level Questions**

4. Design a `Product` class with the attributes name, price, and stock quantity. Include a method to calculate the total value of the stock.

5. Define a `Car` class with attributes such as brand, model, and year. Include a method that prints the car's full description.

6. Create a `Student` class with the following attributes: name, age, and a list of grades. Implement a method that calculates the average grade.

7. Build a `BankAccount` class to store the account holder's name and balance. Add methods for deposit and withdrawal. 

---

### **Hard Questions**

8. Implement a `Library` class that holds a list of books, each represented by a dictionary containing the title, author, and year. Write a method to display all books.

9. Create a `House` class with attributes like address, number of rooms, and square footage. Implement a method that calculates the price based on square footage.

10. Build an `Employee` class that stores an employee’s name, position, and salary. Write a method to calculate the annual salary.

11. Design a `Store` class that stores a list of products, each represented by a dictionary with name, price, and quantity. Write a method that displays the total value of all products in the store. 


---
#### **Real-Life Analogy**  
- A **class** is like a blueprint (e.g., blueprint for a house).  
- An **object** is the actual house built using the blueprint.  
- **Attributes** = Characteristics (e.g., house color, size).  
- **Methods** = Actions the house can perform (e.g., open the door).  

## **Key Takeaways**  

- OOP allows for organizing code into classes and objects.  
- Classes act as blueprints, and objects are instances of these blueprints.  
- The `__init__` constructor method is used to initialize object attributes.  
- Methods define the behavior of objects and can be called to perform actions.  

---

## **Homework**  

 
1.  Create a `Shape` class with methods for calculating the area and perimeter of different shapes.
2. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.
3. **Create a `BankAccount` Class with Multiple Transactions**
   Create a class called `BankAccount` that models a user's bank account. The class should have attributes such as account holder's name, account number, and a list of transactions (each transaction is a dictionary containing 'description' and 'amount'). Implement methods to:
   - Add a transaction (deposit or withdrawal)
   - Calculate the total balance of the account (sum of all deposits minus withdrawals)
   - Generate a report summarizing all transactions and the current balance.

4. **Create a `StudentGradebook` Class**
   Design a `StudentGradebook` class with attributes for the student's name, list of courses, and corresponding grades. Implement methods to:
   - Add a course and its grade
   - Calculate the average grade
   - Display the student's information, including the courses they are enrolled in, their grades, and the average grade.
   - Add functionality to allow grade updates for a specific course.





