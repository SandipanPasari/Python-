class Employee:
    language = "Python"  # This is a class attribute
    salary = 1200000
    
    def __init__(self, name, salary, language):  # Dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")

# Creating an instance of Employee
harry = Employee("Harry", 1300000, "JavaScript")
print(harry.name, harry.salary, harry.language)

# This part had an error because 'rohan' is missing arguments in the constructor
rohan = Employee("Rohan", 1200000, "Python")