# ### **Exercise 1: Practice Inheritance (With Answers)**  

# ---

# #### **1. Create a `Student` class that inherits `Person`.**  
# Add an attribute `course` and modify the `introduce` method to include "I study [course]."  

# ```python
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         return f"My name is {self.name}, and I am {self.age} years old."

# class Student(Person):
#     def __init__(self, name, age, course):
#         super().__init__(name, age)
#         self.course = course

#     def introduce(self):
#         return super().introduce() + f" I study {self.course}."

# # Example
# student = Student("Tinbite", 20, "Computer Science")
# print(student.introduce())
# # Output: My name is Tinbite, and I am 20 years old. I study Computer Science.
# ```

# ---

# #### **2. Add an `id` attribute to `Student`.**

# ```python
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

# # Example
# student = Student("Tinbite", 20, "S12345")
# print(f"Name: {student.name}, Age: {student.age}, ID: {student.student_id}")
# # Output: Name: Tinbite, Age: 20, ID: S12345
# ```

# ---

# #### **3. Override `fuel_efficiency()` in `Car` and `Bike` subclasses.**

# ```python
# class Vehicle:
#     def fuel_efficiency(self):
#         return "Generic fuel efficiency."

# class Car(Vehicle):
#     def fuel_efficiency(self):
#         return "Car fuel efficiency: 15 km/l."

# class Bike(Vehicle):
#     def fuel_efficiency(self):
#         return "Bike fuel efficiency: 40 km/l."

# # Example
# car = Car()
# bike = Bike()
# print(car.fuel_efficiency())  # Output: Car fuel efficiency: 15 km/l.
# print(bike.fuel_efficiency())  # Output: Bike fuel efficiency: 40 km/l.
# ```

# ---

# #### **4. Implement `Shape` and `Square` to calculate the area.**

# ```python
# class Shape:
#     def area(self):
#         return "Area not defined."

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# # Example
# square = Square(5)
# print(square.area())  # Output: 25
# ```

# ---

# #### **5. Use `super()` to call a parent class method.**

# ```python
# class Parent:
#     def greet(self):
#         return "Hello from Parent."

# class Child(Parent):
#     def greet(self):
#         return super().greet() + " And hello from Child."

# # Example
# child = Child()
# print(child.greet())
# # Output: Hello from Parent. And hello from Child.
# ```

# ---

# #### **6. Create a `Teacher` class and inherit in `MathTeacher` and `ScienceTeacher`.**

# ```python
# class Teacher:
#     def teach(self):
#         return "I teach subjects."

# class MathTeacher(Teacher):
#     def teach(self):
#         return "I teach Mathematics."

# class ScienceTeacher(Teacher):
#     def teach(self):
#         return "I teach Science."

# # Example
# math_teacher = MathTeacher()
# science_teacher = ScienceTeacher()
# print(math_teacher.teach())  # Output: I teach Mathematics.
# print(science_teacher.teach())  # Output: I teach Science.
# ```

# ---

# #### **7. Demonstrate single inheritance using `Company` and `Employee`.**

# ```python
# class Company:
#     def __init__(self, name):
#         self.name = name

# class Employee(Company):
#     def __init__(self, name, employee_name):
#         super().__init__(name)
#         self.employee_name = employee_name

# # Example
# employee = Employee("Techtonic", "Tinbite")
# print(f"Company: {employee.name}, Employee: {employee.employee_name}")
# # Output: Company: Techtonic, Employee: Tinbite
# ```

# ---

# #### **8. Override `use()` in `Laptop` and `Smartphone`.**

# ```python
# class Device:
#     def use(self):
#         return "Using device."

# class Laptop(Device):
#     def use(self):
#         return "Using a laptop for work."

# class Smartphone(Device):
#     def use(self):
#         return "Using a smartphone for communication."

# # Example
# laptop = Laptop()
# smartphone = Smartphone()
# print(laptop.use())  # Output: Using a laptop for work.
# print(smartphone.use())  # Output: Using a smartphone for communication.
# ```

# ---

# #### **9. Multiple inheritance with `Teacher` and `Mentor`.**

# ```python
# class Teacher:
#     def teach(self):
#         return "Teaching."

# class Mentor:
#     def guide(self):
#         return "Guiding."

# class TeacherMentor(Teacher, Mentor):
#     pass

# # Example
# teacher_mentor = TeacherMentor()
# print(teacher_mentor.teach())  # Output: Teaching.
# print(teacher_mentor.guide())  # Output: Guiding.
# ```

# ---

# #### **10. Hierarchical inheritance with `Person`, `Student`, and `Teacher`.**

# ```python
# class Person:
#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     def role(self):
#         return f"{self.name} is a student."

# class Teacher(Person):
#     def role(self):
#         return f"{self.name} is a teacher."

# # Example
# student = Student("Tinbite")
# teacher = Teacher("Elias")
# print(student.role())  # Output: Tinbite is a student.
# print(teacher.role())  # Output: Elias is a teacher.
# ```









# ### **10 Simple Polymorphism Coding Questions with Answers**

# ---

# #### **1. Animal Example**
# **Question:** Write a program with an `Animal` class and two subclasses `Dog` and `Cat`, each with a `speak()` method. Call the `speak()` method on each subclass object.  
# **Answer:**

# ```python
# class Animal:
#     def speak(self):
#         return "I make a sound."

# class Dog(Animal):
#     def speak(self):
#         return "Woof! Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# # Creating objects
# dog = Dog()
# cat = Cat()

# print(dog.speak())  # Output: Woof! Woof!
# print(cat.speak())  # Output: Meow!
# ```

# ---

# #### **2. Vehicle Example**
# **Question:** Create a `Vehicle` class and subclasses `Car` and `Bike`. Each subclass should implement a `move()` method differently. Write a function that accepts any `Vehicle` object and calls its `move()` method.  
# **Answer:**

# ```python
# class Vehicle:
#     def move(self):
#         return "I can move."

# class Car(Vehicle):
#     def move(self):
#         return "I move on four wheels."

# class Bike(Vehicle):
#     def move(self):
#         return "I move on two wheels."

# def vehicle_move(vehicle):
#     print(vehicle.move())

# # Example Usage
# car = Car()
# bike = Bike()

# vehicle_move(car)   # Output: I move on four wheels.
# vehicle_move(bike)  # Output: I move on two wheels.
# ```

# ---

# #### **3. Shape Example**
# **Question:** Implement a `Shape` class and subclasses `Circle` and `Square`, each with a `calculate_area()` method. Use polymorphism to compute the area of multiple shapes.  
# **Answer:**

# ```python
# class Shape:
#     def calculate_area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def calculate_area(self):
#         return self.side ** 2

# shapes = [Circle(5), Square(4)]

# for shape in shapes:
#     print(shape.calculate_area())
# # Output:
# # 78.5
# # 16
# ```

# ---

# #### **4. Bird Example**
# **Question:** Create a `Bird` class and two subclasses `Sparrow` and `Penguin`, each with a `fly()` method. Write a program that demonstrates their unique implementations.  
# **Answer:**

# ```python
# class Bird:
#     def fly(self):
#         return "Some birds can fly."

# class Sparrow(Bird):
#     def fly(self):
#         return "I am a Sparrow, I can fly high."

# class Penguin(Bird):
#     def fly(self):
#         return "I am a Penguin, I cannot fly."

# birds = [Sparrow(), Penguin()]

# for bird in birds:
#     print(bird.fly())
# # Output:
# # I am a Sparrow, I can fly high.
# # I am a Penguin, I cannot fly.
# ```

# ---

# #### **5. Worker Example**
# **Question:** Write a `Worker` class and subclasses `Engineer` and `Doctor`, each with a `work()` method. Use polymorphism to call the `work()` method for different worker objects.  
# **Answer:**

# ```python
# class Worker:
#     def work(self):
#         return "I do general work."

# class Engineer(Worker):
#     def work(self):
#         return "I design and build systems."

# class Doctor(Worker):
#     def work(self):
#         return "I diagnose and treat patients."

# workers = [Engineer(), Doctor()]

# for worker in workers:
#     print(worker.work())
# # Output:
# # I design and build systems.
# # I diagnose and treat patients.
# ```

# ---

# #### **6. Payment Example**
# **Question:** Create a `Payment` class and subclasses `CreditCardPayment` and `PayPalPayment`, each with a `process()` method. Demonstrate how polymorphism works with these classes.  
# **Answer:**

# ```python
# class Payment:
#     def process(self):
#         return "Processing payment."

# class CreditCardPayment(Payment):
#     def process(self):
#         return "Processing credit card payment."

# class PayPalPayment(Payment):
#     def process(self):
#         return "Processing PayPal payment."

# payments = [CreditCardPayment(), PayPalPayment()]

# for payment in payments:
#     print(payment.process())
# # Output:
# # Processing credit card payment.
# # Processing PayPal payment.
# ```

# ---

# #### **7. Device Example**
# **Question:** Write a program with a `Device` class and subclasses `Laptop` and `Smartphone`. Each subclass should have a `start()` method. Call the `start()` method on different objects using a loop.  
# **Answer:**

# ```python
# class Device:
#     def start(self):
#         return "Starting device."

# class Laptop(Device):
#     def start(self):
#         return "Laptop is booting up."

# class Smartphone(Device):
#     def start(self):
#         return "Smartphone is turning on."

# devices = [Laptop(), Smartphone()]

# for device in devices:
#     print(device.start())
# # Output:
# # Laptop is booting up.
# # Smartphone is turning on.
# ```

# ---

# #### **8. Student Example**
# **Question:** Create a `Student` class and two subclasses `PrimaryStudent` and `HighSchoolStudent`. Each subclass should have an `introduce()` method. Use polymorphism to introduce different types of students.  
# **Answer:**

# ```python
# class Student:
#     def introduce(self):
#         return "I am a student."

# class PrimaryStudent(Student):
#     def introduce(self):
#         return "I am a primary school student."

# class HighSchoolStudent(Student):
#     def introduce(self):
#         return "I am a high school student."

# students = [PrimaryStudent(), HighSchoolStudent()]

# for student in students:
#     print(student.introduce())
# # Output:
# # I am a primary school student.
# # I am a high school student.
# ```

# ---

# #### **9. Printer Example**
# **Question:** Implement a `Printer` class and subclasses `InkjetPrinter` and `LaserPrinter`, each with a `print()` method. Demonstrate polymorphism by calling the `print()` method on various printer objects.  
# **Answer:**

# ```python
# class Printer:
#     def print(self):
#         return "Printing document."

# class InkjetPrinter(Printer):
#     def print(self):
#         return "Inkjet printer is printing."

# class LaserPrinter(Printer):
#     def print(self):
#         return "Laser printer is printing."

# printers = [InkjetPrinter(), LaserPrinter()]

# for printer in printers:
#     print(printer.print())
# # Output:
# # Inkjet printer is printing.
# # Laser printer is printing.
# ```

# ---

# #### **10. GameCharacter Example**
# **Question:** Write a program with a `GameCharacter` class and two subclasses `Warrior` and `Mage`. Each subclass should implement an `attack()` method. Use a loop to call the `attack()` method for different character objects.  
# **Answer:**

# ```python
# class GameCharacter:
#     def attack(self):
#         return "I attack in my own way."

# class Warrior(GameCharacter):
#     def attack(self):
#         return "Warrior attacks with a sword."

# class Mage(GameCharacter):
#     def attack(self):
#         return "Mage casts a spell."

# characters = [Warrior(), Mage()]

# for character in characters:
#     print(character.attack())
# # Output:
# # Warrior attacks with a sword.
# # Mage casts a spell.
# ```