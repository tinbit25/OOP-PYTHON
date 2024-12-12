![My Image](image.png)
# **Day 2: Intermediate OOP Concepts**  
### **Session Duration**: 2 Hours  

---

## **Session Objectives**  
By the end of this session, participants will:  
1. Understand inheritance and polymorphism with their real-life and programming analogies.  
2. Write Python code that effectively uses inheritance and polymorphism.  
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
        return "Can move."

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

In this example, `Car` and `Boat` inherit the `move` method from `Vehicle`.

---

#### **Code Example 2: Inheritance with Specific Attributes**  

```python
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    breed = "Labrador"
    @classmethod
    def breed(cls.breed)
         return cls.breed

class Cat(Animal):
    color = "Black"

# Example Usage
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Some sound
print(dog.breed())  
print(cat.sound())  # Output: Some sound
```

In this example, both `Dog` and `Cat` inherit the `sound` method from `Animal`.

---

### **Part 2: Super and Method Overriding**  

#### **Method Overriding**  
Method overriding occurs when a child class defines a method that has the same name and signature as a method in its parent class. This allows the child class to provide its specific implementation while still inheriting the parent class's method. Method overriding is a key feature of polymorphism in object-oriented programming.

- **Overriding** occurs when a child class provides a specific implementation of a method that is already defined in the parent class. The child class method "overrides" the parent class method.

##### **Key Points on Overriding**  
- The method in the child class must have the same name and parameters as the method in the parent class.
- Overriding allows the child class to change or extend the functionality of the inherited method.
- You can still access the parent class method using `super()`.

##### **Code Example 3: Method Overriding**  

```python
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):  # Overriding the speak method
        return "Dog barks"

class Cat(Animal):
    def speak(self):  # Overriding the speak method
        return "Cat meows"

# Example Usage
animals = [Animal(), Dog(), Cat()]
for animal in animals:
    print(animal.speak())

# Output:
# Animal speaks
# Dog barks
# Cat meows
```

In this example, the `Dog` and `Cat` classes override the `speak` method from the `Animal` class, providing their specific implementation.

---

#### **Using `super()`**  
The `super()` function is used to call a method from the parent class within the child class. It allows the child class to invoke the parent class's methods, especially when those methods are overridden or need to be extended.

- **Syntax**: `super().method()`
- **Use Case**: If you want to call a method from the parent class within an overridden method of the child class.

##### **Code Example 4: Using `super()`**  

```python
class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        return "Can move."
    
class Car(Vehicle):
    def __init__(self, name, brand):
        self.brand = brand
    
    def move(self):
        parent_move = super().move()  # Calling the parent's move method
        return f"{parent_move} I move on roads."

# Example Usage
car = Car("Car1", "Toyota")
print(car.move())  # Output: Can move. I move on roads.
```

In this example, the `Car` class uses `super()` to first call the `__init__` method of the parent class `Vehicle`, then calls `super().move()` within its overridden `move` method. This way, we preserve the parent class behavior and extend it.

---

#### **Additional Notes on Inheritance**  

- **Single Inheritance**: A child class inherits from one parent class.
- **Multiple Inheritance**: A child class can inherit from more than one parent class.

  ```python
  class A:
      def method_a(self):
          return "Method A"
  
  class B:
      def method_b(self):
          return "Method B"
  
  class C(A, B):
      pass
  
  # Example Usage
  c = C()
  print(c.method_a())  # Output: Method A
  print(c.method_b())  # Output: Method B
  ```

---

### **Summary of Key Concepts in Inheritance**  
- **Inheritance**: Allows one class (child) to inherit attributes and methods from another class (parent).
- **Overriding**: When a child class defines a method with the same name and parameters as the parent class method, providing its own version of that method.
- **Super**: Allows calling a method from the parent class within the child class, useful for extending or modifying the inherited behavior.
- **Multiple Inheritance**: A child class can inherit from more than one parent class.

---

### **Exercise 1: Practice Inheritance (15 minutes)**  

1. Create a Student class that inherits from the Person class.

The Person class should have attributes name and age, and a method introduce() that introduces the person by stating their name and age.
The Student class should inherit from Person and add an additional attribute course to represent the course the student is studying.
Modify the introduce() method in the Student class to include the student's course, so the introduction should include: "Hi, I'm [name], I'm [age] years old, and I study [course]."
Ensure that the Student class uses the super() function to call the constructor of the Person class to initialize the name and age attributes.
   
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

Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common base class. The term means "many forms," and it enables a single interface to represent different underlying data types or behaviors.

In simple terms, polymorphism allows the same method or operation to behave differently based on the object that invokes it.

#### **Real-Life Analogy**  
Think of the word **"drive":**  
- A **car driver** drives on roads.  
- A **train driver** operates a train on tracks.  
- A **ship captain** drives (or navigates) a ship on water.  
The action is called "drive," but its implementation varies depending on the context.

---

### **Code Example 5: Basic Polymorphism**  

```python
# Base class
class Animal:
    def make_sound(self):
        return "Grrr"

# Derived class - Dog
class Dog(Animal):
   def make_sound(self):
       return "Woof!"

# Derived class - Cat
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Polymorphism in action
def animal_sound(animal):
    print(animal.make_sound())

# Create instances
dog = Dog()
cat = Cat()

# Use polymorphism
animal_sound(dog)  # Outputs: Woof!
animal_sound(cat)  # Outputs: Meow!
```  

---
### **Questions: Polymorphism**  

1. Write a program with a Animal class and two subclasses Dog and Cat, each with a speak() method. Call the speak() method on each subclass object.

2. Create a Vehicle class and subclasses Car and Bike. Each subclass should implement a move() method differently. Write a function that accepts any Vehicle object and calls its move() method.

3. Implement a Shape class and subclasses Circle and Square, each with a calculate_area() method. Use polymorphism to compute the area of multiple shapes.

4. Create a Bird class and two subclasses Sparrow and Penguin, each with a fly() method. Write a program that demonstrates their unique implementations.

5. Write a Worker class and subclasses Engineer and Doctor, each with a work() method. Use polymorphism to call the work() method for different worker objects.

6. Create a Payment class and subclasses CreditCardPayment and PayPalPayment, each with a process() method. Demonstrate how polymorphism works with these classes.

7. Write a program with a Device class and subclasses Laptop and Smartphone. Each subclass should have a start() method. Call the start() method on different objects using a loop.

8. Create a Student class and two subclasses PrimaryStudent and HighSchoolStudent. Each subclass should have an introduce() method. Use polymorphism to introduce different types of students.

9. Implement a Printer class and subclasses InkjetPrinter and LaserPrinter, each with a print() method. Demonstrate polymorphism by calling the print() method on various printer objects.

10. Write a program with a GameCharacter class and two subclasses Warrior and Mage. Each subclass should implement an attack() method. Use a loop to call the attack() method for different character objects.

---


#### **Summary of Key Concepts**  
- **Inheritance** allows for code reuse and extending behavior.
- **Polymorphism** enables the same method to work with different data types.
- **Method overriding** allows for child classes to redefine inherited methods.
- **Using `super()`** is a way to call parent class methods within child classes.

---

