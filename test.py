# class Dog:
#     def __init__(self, name,age):  # __init__ method initializes the object
#         self.name = name  # Assigns the name argument to the instance's name attribute

# dog1 = Dog("Buddy")  # Create an object (instance) of Dog and pass the name "Buddy"
# print(dog1.name)  # Output: Buddy

# class Dog:
#     def __init__(self, name,age,color):  # __init__ method initializes the object
#         self.name = name 


# dog1 = Dog("buddy",26,"white")  # No __init__ method to set attributes


# print(dog1.name)  # Output: Buddy
# print("hi u")
class Person:
  pass
p = Person()
print(p)

#### **Code Example: Dog Class**  
#### **Code Example: Car Class**  


# class Car:
#     def __init__(self, brand, year, color):
#         self.brand = brand
#         self.year = year
#         self.color = color

#     def describe(self):
#         return f"{self.color} {self.year} {self.brand}"

# # Creating objects
# car1 = Car("Toyota", 2020, "Red")
# print(car1.describe())  # Output: Red 2020 Toyota
 
#creating class called book 
# class Book:
#   def __init__(self,title,author):
#     self.title=title
#     self.author=author
# book=Book("fikir eske mekabr","hadis alemayehu")
# print (f"The author of {book.title} is {book.author}")    

# 7. **Implement a Library class that holds a list of books, each represented by a dictionary containing the title, author, and year. Write a method to display all books. Use default values for the library's name and location, and test the method by adding and displaying books.**
# class Library:
#   def __init__(self, name="Default Library", location="Default Location"):
#     self.name = name
#     self.location = location
#     self.books = []
#   def add_book(self, title, author, year):  
#     self.books.append({"title": title, "author": author, "year": year})
#   def display_books(self):
#     for book in self.books:
#       print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
# # Creating a library object
# library = Library()
# # Adding books to the library
# library.add_book("Book1", "Author1", 2020)
# library.add_book("Book2", "Author2", 2021)
# # Displaying books in the library
# library.display_books()     

### **Practice Example: Student Management System**
# Write a class `Student` with the following:
# 1. An instance method `add_marks(self, subject, marks)` to add marks for a subject.
# 2. A class method `set_school(cls, school_name)` to change the school name.
# 3. A static method `is_passing(marks)` to check if marks are above 50.

# class Student:
#   school_name="DBU"
#   def __init__ (self,name):
#     self.name=name
#     self.marks={}
#   def add_marks(self,subject,marks):
#     self.marks[subject]=marks
#     return f"{subject}:{marks}"
#   @classmethod
#   def set_school(cls,school_name):
#     cls.school_name=school_name
#     return f"{school_name}"
#   @staticmethod
#   def is_passing(passmarks):
#     return passmarks>50
# student=Student("kal")
# print(student.add_marks("english",70) ) 
# print(student.set_school("DMU"))  
# # print(student.is_passing(20))

       
# class Person:
#   def __init__(self,name,age,color):
#     self.name=name
#     self.age=age
#     self.color=color
# p1=Person("tinbite",24,["white","blue","red"])
# print(p1.name,p1.age,p1.color)

# Create a Person class to store a person's name, age, and a list of their favorite colors. Instantiate the class and display the person's name, age, and all the favorite colors.
# class Person:
#   def __init__(self,name,age,favorite_color):
#     self.name=name
#     self.age=age
#     self.favorite_color=favorite_color
# person1=Person("samuel",20,["red","white","blue"])  

# print(f"{person1.name} is {person1.age} years old and his favorite colors are {person1.favorite_color}")  

# ### **Practice Example: Student Management System**
# Write a class `Student` with the following:
# 1. An instance method `add_marks(self, subject, marks)` to add marks for a subject.
# 2. A class method `set_school(cls, school_name)` to change the school name.
# 3. A static method `is_passing(marks)` to check if marks are above 50.
# class Student:
#   school_name="debere birhan prep"
#   def __init__(self,name):
#     self.name=name
#     self.marks={}
#   def add_marks(self,subject,mark):
#     self.marks[subject]=mark
#     return f"{self.marks}"
#   @classmethod
#   def modify_school_name(cls,school_name):
#      cls.school_name=school_name
#      return f"the school name is changed to{cls.school_name}"
#   @staticmethod
#   def is_passing(my_mark):
#     if my_mark>50:
#         return "pass"  
# student1=Student("tinbite")  
# print(student1.add_marks("english",50) )          
# print(student1.modify_school_name("dmu prep"))
# print(student1.is_passing(90))
# class Animal:
#     def sound(self):
#         return "Some sound"

# class Dog(Animal):
#     breed = "Labrador"
#     @classmethod
#     def breed(cls):
#          return cls.breed

# class Cat(Animal):
#     color = "Black"

# # Example Usage
# dog = Dog()
# cat = Cat()

# print(dog.sound())  # Output: Some sound
# print(dog.breed())  
# print(cat.sound())  # Output: Some sound



# Create a Student class that inherits from the Person class.
# The Person class should have attributes name and age, and a method introduce() that introduces the person by stating their name and age.
# The Student class should inherit from Person and add an additional attribute course to represent the course the student is studying.
# Modify the introduce() method in the Student class to include the student's course, so the introduction should include: "Hi, I'm [name], I'm [age] years old, and I study [course]."
# Ensure that the Student class uses the super() function to call the constructor of the Person class to initialize the name and age attributes.

class Person():
  def __init__(self, name, age):
    self.name=name
    self.age=age
  def introduce(self):
    return f"Hi, I'm {self.name}, I'm {self.age} years old"
class Student(Person):
  def __init__(self, name, age, course):
    super().__init__(name,age)
    self.course=course
  def introduce(self):
    return f"Hi, I'm {self.name}, I'm {self.age} years old,I learn{self.course}"
p1=Person("tinbite",22)
print(p1.introduce())
s1=Student("tinbite",23,"english")
print(s1.introduce())









# The Person class should have attributes name and age, and a method introduce() that introduces the person by stating their name and age.
# The Student class should inherit from Person and add an additional attribute course to represent the course the student is studying.
# Modify the introduce() method in the Student class to include the student's course, so the introduction should include: "Hi, I'm [name], I'm [age] years old, and I study [course]."
# Ensure that the Student class uses the super() function to call the constructor of the Person class to initialize the name and age attributes.


