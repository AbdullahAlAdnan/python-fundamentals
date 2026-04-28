# Module 3 Assignment — Object Oriented Programming
# Course: Data Science Program

# Q1 — Student class with constructors and methods
class Student:
    """Represents a student with name and ID."""

    def __init__(self, name="Unknown", ID=0):
        self.name = name
        self.ID = ID

    def student_details(self):
        """Displays student name and ID."""
        print(f"Student name: {self.name}, Student ID: {self.ID}")

    def placeholder(self):
        pass  # reserved for future functionality


student1 = Student("Adnan", 12)
student2 = Student("Abdullah", 15)
student1.student_details()
student2.student_details()


# Q2 — Single, multilevel, and hierarchical inheritance with method overriding
class Person:
    """Base class representing a person."""

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def detail_info(self):
        print(self.name, self.id)


class Student(Person):
    """Single inheritance — Student extends Person."""

    def __init__(self, name, id, email):
        super().__init__(name, id)
        self.email = email

    def detail_info(self):  # method overriding
        print(f"Name: {self.name}, ID: {self.id}, Email: {self.email}")


class GraduateStudent(Student):
    """Multilevel inheritance — GraduateStudent extends Student extends Person."""

    def __init__(self, name, id, email, research_area):
        super().__init__(name, id, email)
        self.research_area = research_area

    def detail_info(self):  # method overriding
        print(f"Name: {self.name}, ID: {self.id}, "
              f"Email: {self.email}, Research: {self.research_area}")


class Teacher(Person):
    """Hierarchical inheritance — Teacher also extends Person."""

    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def detail_info(self):  # method overriding
        print(f"Name: {self.name}, Department: {self.department}")


student1 = Student("Adnan", 12, "adnan@gmail.com")
grad_student = GraduateStudent("Rahim", 200, "rahim@gmail.com", "AI")
teacher1 = Teacher("Abdullah", 130, "Science")

student1.detail_info()
grad_student.detail_info()
teacher1.detail_info()


# Q3 — Encapsulation, method overloading (default args), multiple inheritance
class Account:
    """Demonstrates encapsulation using private attributes."""

    def __init__(self, name, balance):
        self.__name = name      # private attribute
        self.__balance = balance  # private attribute

    def get_name(self):
        """Getter for name."""
        return self.__name

    def get_balance(self):
        """Getter for balance."""
        return self.__balance

    def set_balance(self, amount):
        """Setter for balance with validation."""
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance")

    def deposit(self, amount, bonus=0):
        """Simulates method overloading using default argument."""
        self.__balance += amount + bonus
        print(f"Updated balance: {self.__balance}")


class Person:
    """Simple class representing a person's location."""

    def __init__(self, city):
        self.city = city

    def show_city(self):
        print(f"City: {self.city}")


class Employee(Account, Person):
    """Multiple inheritance — Employee extends both Account and Person."""

    def __init__(self, name, balance, city, emp_id):
        Account.__init__(self, name, balance)
        Person.__init__(self, city)
        self.emp_id = emp_id

    def display(self):
        """Displays all employee details."""
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.get_name()}")
        print(f"Balance: {self.get_balance()}")
        print(f"City: {self.city}")


emp = Employee("Adnan", 1000, "Karachi", 501)
print(emp.get_name())
print(emp.get_balance())
emp.deposit(500)
emp.deposit(500, 100)
emp.display()
emp.show_city()
