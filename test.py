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
class Library:
  def __init__(self, name="Default Library", location="Default Location"):
    self.name = name
    self.location = location
    self.books = []
  def add_book(self, title, author, year):  
    self.books.append({"title": title, "author": author, "year": year})
  def display_books(self):
    for book in self.books:
      print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
# Creating a library object
library = Library()
# Adding books to the library
library.add_book("Book1", "Author1", 2020)
library.add_book("Book2", "Author2", 2021)
# Displaying books in the library
library.display_books()     




