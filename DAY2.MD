Here’s the updated and extended version of the session plan on **Inheritance** and **Polymorphism** for a **2-hour session**, with detailed explanations, real-life examples, exercises, and structured sections.  

---

# **Day 2: Intermediate OOP Concepts**  
### **Session Duration**: 2 Hours  

---

## **Session Objectives**  
By the end of this session, participants will:  
1. Understand inheritance and polymorphism with their real-life and programming analogies.  
2. Write Python code that uses inheritance and polymorphism effectively.  
3. Practice solving practical problems using these OOP concepts.  

---

## **Session Plan**  

### **Part 1: Understanding Inheritance**  

#### **Definition**  
Inheritance allows one class (child) to inherit attributes and methods from another class (parent).  
- **Parent Class**: Represents a general entity (e.g., `Vehicle`).  
- **Child Class**: Represents a specific type of the parent (e.g., `Car` inherits from `Vehicle`).  

#### **Real-Life Analogy**  
Think of a **family hierarchy**:  
- A parent might have specific attributes (e.g., "brown eyes") and behaviors (e.g., "cooking skills").  
- A child inherits these traits but may also add unique traits (e.g., "plays guitar") or modify behaviors (e.g., "different cooking style").  

---

### **Code Example 1: Basic Inheritance**  

```python
class Vehicle:
    def move(self):
        return "I can move."

class Car(Vehicle):
    pass

class Boat(Vehicle):
    pass

# Example Usage
vehicle = Vehicle()
car = Car()
boat = Boat()

print(vehicle.move())  # Output: I can move.
print(car.move())      # Output: I can move.
print(boat.move())     # Output: I can move.
```  

Here, `Car` and `Boat` inherit the `move` method from `Vehicle`.

---

### **Code Example 2: Overriding Methods**  

```python
class Vehicle:
    def move(self):
        return "I can move."

class Car(Vehicle):
    def move(self):
        return "I move on roads."

class Boat(Vehicle):
    def move(self):
        return "I move on water."

vehicles = [Vehicle(), Car(), Boat()]
for v in vehicles:
    print(v.move())
# Output:
# I can move.
# I move on roads.
# I move on water.
```  

---

### **Exercise 1: Practice Inheritance (15 minutes)**  
---
1. Create a `Student` class that inherits `Person`.  
   - Add an attribute `course` and modify the `introduce` method to include "I study [course]." 
   
2. Create a `Person` class and a `Student` class that inherits it. Add an `id` attribute to `Student`.
3. Create a `Vehicle` class with a method `fuel_efficiency()` and override it in `Car` and `Bike` subclasses.

4. Implement a `Shape` class and a `Square` subclass that calculates the area.

5. Use `super()` to call a parent class's method from a child class.

6. Create a `Teacher` class and inherit it in `MathTeacher` and `ScienceTeacher`.

7. Demonstrate single inheritance using `Company` and `Employee`.

8. Write a program with a `Device` class and its subclasses `Laptop` and `Smartphone`, overriding the `use` method.

9. Create an example of multiple inheritance using `Teacher` and `Mentor`.

10. Write a program to demonstrate hierarchical inheritance with a `Person` class and `Student` and `Teacher` subclasses.
 


---

### **Part 2: Understanding Polymorphism**  

#### **Definition**  
Polymorphism means “many forms.” It allows methods in different classes to have the same name but behave differently.  

#### **Real-Life Analogy**  
Think of the word **"drive":**  
- A **car driver** drives on roads.  
- A **train driver** operates a train on tracks.  
- A **ship captain** drives (or navigates) a ship on water.  
The action is called "drive," but its implementation varies depending on the context.

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
# Output:
# I make a sound.
# Woof! Woof!
# Meow!
```  

---

### **Exercise 2: Practice Polymorphism (15 minutes)**  
1. Create a `Shape` class with a method `area`.  
   - Create two subclasses:  
     - `Circle` that calculates the area of a circle (π × r²).  
     - `Rectangle` that calculates the area of a rectangle (length × width).  
2. Write a loop to calculate and print the areas of multiple shapes.  

---

### **Part 3: Advanced Inheritance and Polymorphism**  

#### **Using `super()` in Inheritance**  

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
```
---

### **Questions: Polymorphism**  

1. Write a program with a `Animal` class and two subclasses `Dog` and `Cat`, each with a `speak()` method. Call the `speak()` method on each subclass object.

2. Create a `Vehicle` class and subclasses `Car` and `Bike`. Each subclass should implement a `move()` method differently. Write a function that accepts any `Vehicle` object and calls its `move()` method.

3. Implement a `Shape` class and subclasses `Circle` and `Square`, each with a `calculate_area()` method. Use polymorphism to compute the area of multiple shapes.

4. Create a `Bird` class and two subclasses `Sparrow` and `Penguin`, each with a `fly()` method. Write a program that demonstrates their unique implementations.

5. Write a `Worker` class and subclasses `Engineer` and `Doctor`, each with a `work()` method. Use polymorphism to call the `work()` method for different worker objects.

6. Create a `Payment` class and subclasses `CreditCardPayment` and `PayPalPayment`, each with a `process()` method. Demonstrate how polymorphism works with these classes.

7. Write a program with a `Device` class and subclasses `Laptop` and `Smartphone`. Each subclass should have a `start()` method. Call the `start()` method on different objects using a loop.

8. Create a `Student` class and two subclasses `PrimaryStudent` and `HighSchoolStudent`. Each subclass should have an `introduce()` method. Use polymorphism to introduce different types of students.

9. Implement a `Printer` class and subclasses `InkjetPrinter` and `LaserPrinter`, each with a `print()` method. Demonstrate polymorphism by calling the `print()` method on various printer objects.

10. Write a program with a `GameCharacter` class and two subclasses `Warrior` and `Mage`. Each subclass should implement an `attack()` method. Use a loop to call the `attack()` method for different character objects.

---

### **Summary**  
- **Inheritance** is used to reuse code and model hierarchies.  
- **Polymorphism** is used to define methods that behave differently based on the object calling them.  
- Together, these concepts make OOP flexible, reusable, and scalable.  

