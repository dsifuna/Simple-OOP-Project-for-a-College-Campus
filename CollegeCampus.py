class Person:

    def  __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
        
def get_info(self):
    return f"{self.role}: {self.name}: Age:{self.age}"

class Student(Person):
    
    def __init__(self, name, age, student_id):
        # Call the superclass (Person)  constructor with the given arguments
        super().__init__(name, age, role="Student")
        self.student_id = student_id
        
    def get_info(self):
        # Override the get_info method for students
        return f"{self.role}: {self.name}, Age: {self.age}, Student ID: {self.student_id}"
    
class Faculty(Person):
    
    def __init__(self, name, age, employee_id, department):
        # Call the superclass (Person) constructor with the given arguments
        super().__init__(name, age,role="Faculty")
        self.employee_id = employee_id
        self.department = department
    
    def get_info(self):
        # Override the get_info method for students
        return f"{self.role}: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Department: {self.department}"
    
class Staff(Person):
    
    def __init__(self, name, age, employee_id, position):
        #Call the Employee's constructor passing in additional parameters
        super().__init__(name, age, role = "Staff")
        self.employee_id =  employee_id
        self.position= position
    def get_info(self):
        #Additional information about staff members
        return f"{self.role}: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Position {self.position}"
    
# Example usage:
student1 = Student("Dennis Sifuna", 29, "DS3030")
faculty1 = Faculty("John Omond", 35, "SD8903", "Computer Science")
staff1 = Staff("ijaza Imani", 28, "ED3030", "Administrator")

# Print information  about each person

print(student1.get_info())
print(faculty1.get_info())
print(staff1.get_info())
        