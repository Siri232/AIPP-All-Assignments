# Manual inline comments (Human-written):
class sru_student:  # Define class for SRU student
    def __init__(self, name, roll_no, hostel_status):  # Constructor to initialize attributes
        self.name = name  # Store student name
        self.roll_no = roll_no  # Store roll number
        self.hostel_status = hostel_status  # Store hostel status
        self.fee = 0  # Initialize fee to zero
    def fee_update(self, amount):  # Method to update fee
        self.fee += amount  # Add amount to current fee
    def display_details(self):  # Method to show student info
        print(f"Name: {self.name}, Roll: {self.roll_no}, Hostel: {self.hostel_status}, Fee: {self.fee}")  # Print all details
# AI-generated inline comments (Cursor AI):
class sru_student_ai:
    def __init__(self, name, roll_no, hostel_status):  # Initialize student object with name, roll number, and hostel status
        self.name = name  # Assign the student's name as an instance attribute
        self.roll_no = roll_no  # Assign the student's roll number as an instance attribute
        self.hostel_status = hostel_status  # Assign the student's hostel status (e.g., 'Yes' or 'No') as an instance attribute
        self.fee = 0  # Initialize the fee balance to zero for new students
    def fee_update(self, amount):  # Update the student's fee by adding the specified amount
        self.fee += amount  # Increment the current fee balance by the provided amount
    def display_details(self):  # Display all student information in a formatted string
        print(f"Name: {self.name}, Roll: {self.roll_no}, Hostel: {self.hostel_status}, Fee: {self.fee}")  
        # Print formatted string containing name, roll number, hostel status, and current fee
print("MANUAL COMMENTS:\nclass sru_student:  # Define class for SRU student")
print("AI COMMENTS:\nclass sru_student_ai:  # Initialize student object with name, roll number, and hostel status")
print("="*60, "\nCOMPARISON:\nManual: Short, direct comments\nAI: More detailed, explains purpose with examples\n")
# User input to test
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
hostel = input("Enter hostel status (Yes/No): ")
s = sru_student(name, roll_no, hostel)
s.display_details()
fee = int(input("Enter fee amount to add: "))
s.fee_update(fee)
s.display_details()

