class Employee:
    """Employee class to manage employee information and salary operations."""
    
    def __init__(self, name: str, salary: float):
        """Initialize an Employee instance."""
        self.name = name
        self._salary = salary
    
    def increase_salary(self, percentage: float) -> None:
        """Increase employee salary by given percentage."""
        self._salary += self._salary * percentage / 100
    
    def display_info(self) -> None:
        """Display employee information in formatted output."""
        print(f"Employee: {self.name}, Salary: ${self._salary:,.2f}")


if __name__ == "__main__":
    name = input("Enter employee name: ")
    try:
        salary = float(input("Enter initial salary: "))
        emp = Employee(name, salary)
        print("\n--- Employee Information ---")
        emp.display_info()
        increase = input("\nEnter salary increase percentage (or press Enter to skip): ")
        if increase:
            emp.increase_salary(float(increase))
            print("\n--- Updated Information ---")
            emp.display_info()
    except ValueError as e:
        print(f"Error: {e}")