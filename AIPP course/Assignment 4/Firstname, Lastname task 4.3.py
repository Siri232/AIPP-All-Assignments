def format_name(first_name, last_name):
    """
    Format a full name as 'Last, First'
    
    Args:
        first_name (str): The person's first name
        last_name (str): The person's last name
        
    Returns:
        str: Formatted name as 'Last, First'
    """
    return f"{last_name}, {first_name}"

# Examples
def example_name_formatting():
    # Example 1
    print(format_name("John", "Smith"))  # Output: Smith, John
    
    # Example 2
    print(format_name("Mary", "Johnson"))  # Output: Johnson, Mary
    
    # Example 3
    print(format_name("Robert", "Brown"))  # Output: Brown, Robert

# Run examples
if __name__ == "__main__":
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    print(format_name(first_name, last_name))