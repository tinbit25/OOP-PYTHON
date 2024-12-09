# **Day 2: Intermediate OOP Concepts**  
### **Session Duration**: 2.5 Hours  

---

## **Part 1: Inheritance**  
### **Objective**  
Understand how to create child classes that inherit properties and methods from a parent class.

---

### **Explanation**  
Inheritance allows a child class to inherit attributes and methods from a parent class.  
- **Parent Class**: A general category (e.g., `Vehicle`).  
- **Child Class**: A more specific category that inherits from the parent (e.g., `Car`).  
- The child class can also override or extend the functionality of the parent class.  

---

### **Code Example 1: Basic Inheritance**  

```python
class Vehicle:
    def move(self):
        return "I can move."

class Car(Vehicle):
    def move(self):
        return "I drive on roads."

class Boat(Vehicle):
    def move(self):
        return "I sail on water."

# Example Usage
vehicle = Vehicle()
car = Car()
boat = Boat()

print(vehicle.move())  # Output: I can move.
print(car.move())      # Output: I drive on roads.
print(boat.move())     # Output: I sail on water.
```

---

### **Code Example 2: Real-World Scenario**  

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        return f"Manager {self.name} manages {self.department} department."

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        return f"Developer {self.name} codes in {self.programming_language}."
```

---

### **Exercise**  
1. Create a `Person` class with attributes `name` and `age` and a method `introduce` to display the person's information.  
2. Create two child classes:
   - `Student` with an additional attribute `course` and override the `introduce` method.  
   - `Teacher` with an additional attribute `subject` and override the `introduce` method.  

---

## **Part 2: Encapsulation**  
### **Objective**  
Learn how to protect data using access modifiers.  

---

### **Explanation**  
Encapsulation allows restricting direct access to some attributes while providing controlled access through methods.  
- **Public Attributes**: Accessible anywhere.  
- **Private Attributes**: Accessible only inside the class (prefix with `__`).  

---

### **Code Example 1: Encapsulation Basics**  

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount}. New balance: {self.__balance}"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance."
        self.__balance -= amount
        return f"Withdrew {amount}. Remaining balance: {self.__balance}"

    def get_balance(self):
        return self.__balance
```

---

### **Exercise**  
1. Create a `Student` class with private attributes for `name` and `grades`.  
2. Add methods to securely add grades and retrieve the list of grades.  

---

## **Part 3: Polymorphism**  
### **Objective**  
Understand how methods can work differently based on the object that calls them.  

---

### **Explanation**  
Polymorphism allows methods in different classes to have the same name but behave differently based on the class.  

---

### **Code Example 1: Basic Polymorphism**  

```python
class Animal:
    def speak(self):
        return "I make a sound."

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Animal(), Dog(), Cat()]
for animal in animals:
    print(animal.speak())
```

---

### **Exercise**  
1. Create a `Shape` class with a method `area`.  
2. Create two subclasses:  
   - `Circle` that overrides the `area` method to calculate the area of a circle.  
   - `Rectangle` that overrides the `area` method to calculate the area of a rectangle.  

---

## **Part 4: Mini-Project**  
### **Objective**  
Combine all concepts (Inheritance, Encapsulation, Polymorphism) into a practical project.  

---

### **Project: Library Management System**  

---

### **Requirements**  
1. A `Book` class with attributes `title` and `author`.  
2. A `Library` class with methods to add, remove, and list books.  
3. Add a `User` class that can borrow and return books.  

---

### **Sample Implementation**  

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title} by {book.author}")

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]
        print(f"Removed book: {title}")

    def list_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(f"{book.title} by {book.author}")

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, title):
        for book in library.books:
            if book.title == title:
                library.remove_book(title)
                self.borrowed_books.append(book)
                print(f"{self.name} borrowed {title}")
                return
        print(f"Book {title} not available.")

    def return_book(self, library, title):
        for book in self.borrowed_books:
            if book.title == title:
                self.borrowed_books.remove(book)
                library.add_book(book)
                print(f"{self.name} returned {title}")
                return
        print(f"{self.name} does not have {title}.")
```

---

### **Exercise**  
Extend the project to include:  
1. A search functionality in the library to find books by title or author.  
2. An admin user who can view all borrowed books and their borrowers.  

--- 

