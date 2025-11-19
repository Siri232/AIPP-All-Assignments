class Student:
    def __init__(self, name, age, marks):
        self.name, self.age, self.marks = name, age, marks
    def total(self):
        return sum(self.marks)
    def report(self):
        print(f"{self.name}, {self.age} | {self.marks} | Total: {self.total()} | Avg: {self.total()/len(self.marks):.2f}")

[Student(input("Name: "), int(input("Age: ")), [float(input(f"M{i+1}: ")) for i in range(3)]).report()]