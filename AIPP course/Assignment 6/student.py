class Student:
    """A class to represent a student with name, age, and course."""
    
    def __init__(self, name, age, course):
        """
        Initialize a Student object.
        
        Args:
            name (str): The name of the student
            age (int): The age of the student
            course (str): The course the student is enrolled in
        """
        self.name = name
        self.age = age
        self.course = course
    
    def display_details(self):
        """Display the student's information."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")


if __name__ == "__main__":
    Student(input("Name: "), int(input("Age: ")), input("Course: ")).display_details()
