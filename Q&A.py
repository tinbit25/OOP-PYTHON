
#DAY-1
#class,object,__init__

# Easy Questions
# Question 1: Create a Person class to store the person's name, age, and a list of their favorite colors. Instantiate the class and display the person's name, age, and all the favorite colors.

# Answer:

# python
# Copy code
# class Person:
#     def __init__(self, name, age, favorite_colors):
#         self.name = name
#         self.age = age
#         self.favorite_colors = favorite_colors

# person1 = Person("Alice", 30, ["Red", "Blue", "Green"])
# print(f"Name: {person1.name}, Age: {person1.age}, Favorite Colors: {', '.join(person1.favorite_colors)}")
# # Output: Name: Alice, Age: 30, Favorite Colors: Red, Blue, Green
# Question 2: Define a Library class to store the library's name, location, and a list of available books (titles). Display the library name, location, and all the book titles.

# Answer:

# python
# Copy code
# class Library:
#     def __init__(self, name, location, books):
#         self.name = name
#         self.location = location
#         self.books = books

# my_library = Library("Central Library", "Downtown", ["The Great Gatsby", "1984", "To Kill a Mockingbird"])
# print(f"Library Name: {my_library.name}, Location: {my_library.location}, Books: {', '.join(my_library.books)}")
# # Output: Library Name: Central Library, Location: Downtown, Books: The Great Gatsby, 1984, To Kill a Mockingbird
# Question 3: Build a Student class that holds a student's name, age, grades (in a dictionary), and enrolled courses (a list). Create an instance of a student and print their name, age, and grades.

# Answer:

# python
# Copy code
# class Student:
#     def __init__(self, name, age, grades, courses):
#         self.name = name
#         self.age = age
#         self.grades = grades
#         self.courses = courses

# student1 = Student("John", 20, {"Math": "A", "History": "B+"}, ["Math", "History", "Physics"])
# print(f"Name: {student1.name}, Age: {student1.age}, Grades: {student1.grades}")
# # Output: Name: John, Age: 20, Grades: {'Math': 'A', 'History': 'B+'}

# Hard Questions
# Question 4: Create a Car class to store the car's brand, model, year, and a list of service dates. Instantiate the class with a car’s information and print all details, including the car's brand, model, year, and service dates.

# Answer:

# python
# Copy code
# class Car:
#     def __init__(self, brand, model, year, service_dates):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.service_dates = service_dates

# my_car = Car("Toyota", "Camry", 2020, ["2021-06-15", "2022-04-10", "2023-09-18"])
# print(f"Brand: {my_car.brand}, Model: {my_car.model}, Year: {my_car.year}, Service Dates: {', '.join(my_car.service_dates)}")
# # Output: Brand: Toyota, Model: Camry, Year: 2020, Service Dates: 2021-06-15, 2022-04-10, 2023-09-18


# Question 5: Design a Product class that tracks the name, price, manufacturing date, and reviews (stored in a dictionary with usernames and ratings). Create an instance of a product and print all its details, including the reviews.

# Answer:

# python
# Copy code
# class Product:
#     def __init__(self, name, price, manufacture_date, reviews):
#         self.name = name
#         self.price = price
#         self.manufacture_date = manufacture_date
#         self.reviews = reviews

# product1 = Product("Laptop", 1200, "2023-05-01", {"User1": {"rating": 4.5, "comment": "Great product!"}, "User2": {"rating": 5.0, "comment": "Highly recommended!"}})
# print(f"Product Name: {product1.name}, Price: {product1.price}, Manufactured On: {product1.manufacture_date}")
# print(f"Reviews: {product1.reviews}")
# # Output: Product Name: Laptop, Price: 1200, Manufactured On: 2023-05-01
# # Reviews: {'User1': {'rating': 4.5, 'comment': 'Great product!'}, 'User2': {'rating': 5.0, 'comment': 'Highly recommended!'}}

# Question 6: Implement a School class to store the school's name, the number of students, and a dictionary of student names with their respective grades. Display the school's name, the number of students, and the students with their grades.

# Answer:

# python
# Copy code
# class School:
#     def __init__(self, name, num_students, student_grades):
#         self.name = name
#         self.num_students = num_students
#         self.student_grades = student_grades

# school1 = School("Greenwood High", 1500, {"Alice": "A", "Bob": "B", "Charlie": "A+"})
# print(f"School Name: {school1.name}, Number of Students: {school1.num_students}")
# print(f"Student Grades: {school1.student_grades}")
# # Output: School Name: Greenwood High, Number of Students: 1500
# # Student Grades: {'Alice': 'A', 'Bob': 'B', 'Charlie': 'A+'}

#








# Methods, default value practice

# ### **Easy Questions**

# 1. **Create a Book class that stores the title, author, and publication year. Add a method to display the book's details. Instantiate the class and call the method.**

# ```python
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
    
#     def display_details(self):
#         print(f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}")

# # Creating an object and calling the method
# book1 = Book("1984", "George Orwell", 1949)
# book1.display_details()
# ```

# **Output:**
# ```
# Title: 1984
# Author: George Orwell
# Year: 1949
# ```

# 2. **Design a Company class with attributes for name, industry, and founding year, along with methods to display the company's details and calculate its age based on the current year:

# class Company:
#     def __init__(self, name, industry, founding_year):
#         self.name = name
#         self.industry = industry
#         self.founding_year = founding_year
    
#     def display_details(self):
#         print(f"Company: {self.name}")
#         print(f"Industry: {self.industry}")
#         print(f"Founding Year: {self.founding_year}")
    
#     def calculate_age(self, current_year):
#         return current_year - self.founding_year

# # Creating an object and calling the methods
# company1 = Company("TechCorp", "Technology", 2005)
# company1.display_details()
# company_age = company1.calculate_age(2024)
# print(f"Company Age: {company_age} years")
# ---

# ### **Mid-Level Questions**

# 3. **Design a Product class with the attributes name, price, and stock quantity. Include a method to calculate the total value of the stock (price * quantity). Add a default stock quantity and test the class with and without specifying a stock quantity.**

# ```python
# class Product:
#     def __init__(self, name, price, quantity=10):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
#     def total_value(self):
#         return self.price * self.quantity

# # Creating objects and calling the method
# product1 = Product("Laptop", 1000, 5)
# print(f"Total Value: {product1.total_value()}")

# product2 = Product("Phone", 800)
# print(f"Total Value: {product2.total_value()}")
# ```

# **Output:**
# ```
# Total Value: 5000
# Total Value: 8000
# ```

# ---


# 4. **Define a Car class with attributes such as brand, model, and year. Include a method that prints the car's full description. Provide default values for some attributes and test the class with and without providing custom values.**

# ```python
# class Car:
#     def __init__(self, brand="Toyota", model="Corolla", year=2020):
#         self.brand = brand
#         self.model = model
#         self.year = year
    
#     def display_description(self):
#         print(f"Car: {self.year} {self.brand} {self.model}")

# # Creating objects and calling the method
# car1 = Car()
# car1.display_description()

# car2 = Car("Honda", "Civic", 2022)
# car2.display_description()
# ```

# **Output:**
# ```
# Car: 2020 Toyota Corolla
# Car: 2022 Honda Civic
# ```

# 5. **Create a Student class with the following attributes: name, age, and a list of grades. Implement a method that calculates the average grade. Set default values for name and age and compute the average grade for a student.**

# ```python
# class Student:
#     def __init__(self, name="John Doe", age=20, grades=None):
#         if grades is None:
#             grades = []
#         self.name = name
#         self.age = age
#         self.grades = grades
    
#     def calculate_average(self):
#         return sum(self.grades) / len(self.grades) if self.grades else 0

# # Creating an object and calling the method
# student1 = Student(grades=[85, 90, 88])
# print(f"Average Grade: {student1.calculate_average()}")
# ```

# **Output:**
# ```
# Average Grade: 87.66666666666667
# ```

# 6. **Build a BankAccount class to store the account holder's name and balance. Add methods for deposit and withdrawal. Implement default values for the balance and test the class by depositing and withdrawing money.**

# ```python
# class BankAccount:
#     def __init__(self, name, balance=1000):
#         self.name = name
#         self.balance = balance
    
#     def deposit(self, amount):
#         self.balance += amount
    
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("Insufficient funds")
    
#     def display_balance(self):
#         print(f"Account balance: {self.balance}")

# # Creating an object and performing deposit and withdrawal
# account1 = BankAccount("Alice")
# account1.deposit(500)
# account1.withdraw(200)
# account1.display_balance()
# ```

# **Output:**
# ```
# Account balance: 1300
# ```


# ### **Hard Questions**

# 7. **Implement a Library class that holds a list of books, each represented by a dictionary containing the title, author, and year. Write a method to display all books. Use default values for the library's name and location, and test the method by adding and displaying books.**

# ```python
# class Library:
#     def __init__(self, name="Central Library", location="Downtown"):
#         self.name = name
#         self.location = location
#         self.books = []
    
#     def add_book(self, title, author, year):
#         self.books.append({"title": title, "author": author, "year": year})
    
#     def display_books(self):
#         for book in self.books:
#             print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

# # Creating an object, adding books, and displaying them
# library = Library()
# library.add_book("1984", "George Orwell", 1949)
# library.add_book("To Kill a Mockingbird", "Harper Lee", 1960)
# library.display_books()
# ```

# **Output:**
# ```
# Title: 1984, Author: George Orwell, Year: 1949
# Title: To Kill a Mockingbird, Author: Harper Lee, Year: 1960
# ```

# 8. **Create a House class with attributes like address, number of rooms, and square footage. Implement a method that calculates the price based on square footage (price = square footage * rate). Set a default value for the rate and test the class by calculating the price with and without specifying the rate.**

# ```python
# class House:
#     def __init__(self, address, rooms, square_footage, rate=200):
#         self.address = address
#         self.rooms = rooms
#         self.square_footage = square_footage
#         self.rate = rate
    
#     def calculate_price(self):
#         return self.square_footage * self.rate

# # Creating objects and calling the method
# house1 = House("123 Main St", 4, 1500)
# print(f"Price: {house1.calculate_price()}")

# house2 = House("456 Oak St", 3, 1200, rate=250)
# print(f"Price: {house2.calculate_price()}")
# ```

# **Output:**
# ```
# Price: 300000
# Price: 300000
# ```

# 9. **Build an Employee class that stores an employee’s name, position, and salary. Write a method to calculate the annual salary. Provide a default salary value and test the method by calculating the annual salary for an employee with and without a custom salary.**

# ```python
# class Employee:
#     def __init__(self, name, position, salary=50000):
#         self.name = name
#         self.position = position
#         self.salary = salary
    
#     def calculate_annual_salary(self):
#         return self.salary * 12

# # Creating objects and calling the method
# employee1 = Employee("John Doe", "Developer")
# print(f"Annual Salary: {employee1.calculate_annual_salary()}")

# employee2 = Employee("Jane Smith", "Manager", 60000)
# print(f"Annual Salary: {employee2.calculate_annual_salary()}")
# ```

# **Output:**
# ```
# Annual Salary: 600000
# Annual Salary: 720000
# ```

# 10. **Design a Store class that stores a list of products, each represented by a dictionary with name, price, and quantity. Write a method that displays the total value of all products in the store (sum of price * quantity). Use default values for the store’s name and location, and test the method by adding products and displaying the total value.**

# ```python
# class Store:
#     def __init__(self, name="Tech Store", location="Main Street"):
#         self.name = name
#         self.location = location
#         self.products = []
    
#     def add_product(self, name, price, quantity):
#         self.products.append({"name": name, "price": price, "quantity": quantity})
    
#     def total_value(self):
#         total = 0
#         for product in self.products:
#             total += product['price'] * product['quantity']
#         return total

# # Creating an object, adding products, and calculating total value
# store = Store()
# store.add_product("Laptop", 1000, 5)
# store.add_product("Phone", 500, 10)
# print(f"Total Value: {store.total_value()}")
# ```

# **Output:**
# ```
# Total Value: 15000
# ```

# Inheritance


# ---

# ### **1. Basic Inheritance and Method Overriding**
# **Question**:  
# Define a base class named `Animal` with a method `speak()`. Create a derived class `Dog` that overrides the `speak()` method. How should the code be implemented?  

# **Solution**:  
# ```python
# class Animal:
#     def speak(self):
#         return "I make a sound."

# class Dog(Animal):
#     def speak(self):
#         return "Woof! Woof!"

# # Example usage
# animal = Animal()
# dog = Dog()

# print(animal.speak())  # Output: I make a sound.
# print(dog.speak())     # Output: Woof! Woof!
# ```

# ---

# ### **2. Extending Attributes in Derived Classes**
# **Question**:  
# Create a base class `Book` with attributes for `title` and `author`. Write a derived class `EBook` that adds an attribute for `file_size`. How would you extend the functionality of the `Book` class in the `EBook` class?  

# **Solution**:  
# ```python
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

# class EBook(Book):
#     def __init__(self, title, author, file_size):
#         super().__init__(title, author)
#         self.file_size = file_size

# # Example usage
# ebook = EBook("Python Basics", "John Doe", "2MB")
# print(f"{ebook.title} by {ebook.author}, File Size: {ebook.file_size}")
# # Output: Python Basics by John Doe, File Size: 2MB
# ```



# ### **4. Class Hierarchies with Unique Methods**
# **Question**:  
# Design a class hierarchy where `Animal` is the base class, and `Mammal` and `Bird` are derived classes. Each derived class should include a unique method that describes a distinctive feature.  

# **Solution**:  
# ```python
# class Animal:
#     def description(self):
#         return "I am an animal."

# class Mammal(Animal):
#     def nurse(self):
#         return "I nurse my young."

# class Bird(Animal):
#     def fly(self):
#         return "I can fly."

# # Example usage
# mammal = Mammal()
# bird = Bird()

# print(mammal.description())  # Output: I am an animal.
# print(mammal.nurse())        # Output: I nurse my young.
# print(bird.description())    # Output: I am an animal.
# print(bird.fly())            # Output: I can fly.
# ```

# ---

# ### **5. Calling Parent Class Methods from Derived Classes**
# **Question**:  
# How would you implement a method in the base class that is explicitly called from a derived class? Provide an example.  

# **Solution**:  
# ```python
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def description(self):
#         return f"I am an animal named {self.name}."

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def description(self):
#         parent_desc = super().description()
#         return f"{parent_desc} I am a {self.breed}."

# # Example usage
# dog = Dog("Buddy", "Golden Retriever")
# print(dog.description())
# # Output: I am an animal named Buddy. I am a Golden Retriever.
# ```

# ---

