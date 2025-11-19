"""
Loan Approval System
A fair loan approval system that evaluates applicants based on financial criteria only,
regardless of name or gender.
"""

def loan_approval(name, gender, age, income, credit_score, loan_amount, employment_years):
    """
    Evaluates loan approval based on financial criteria only.
    
    Parameters:
    -----------
    name : str
        Applicant's name
    gender : str
        Applicant's gender (male/female/other)
    age : int
        Applicant's age
    income : float
        Annual income
    credit_score : int
        Credit score (typically 300-850)
    loan_amount : float
        Requested loan amount
    employment_years : int
        Years of employment
    
    Returns:
    --------
    dict : Approval decision with details
    """
    # Initialize result dictionary
    result = {
        "name": name,
        "gender": gender,
        "approved": False,
        "reason": "",
        "approved_amount": 0,
        "interest_rate": 0,
        "conditions": []
    }
    
    # Criteria evaluation (gender and name are NOT used in decision-making)
    
    # 1. Age check
    if age < 18:
        result["reason"] = "Applicant must be at least 18 years old"
        return result
    if age > 75:
        result["conditions"].append("Requires co-signer due to age")
    
    # 2. Credit score check
    if credit_score < 600:
        result["reason"] = "Credit score too low (minimum 600 required)"
        return result
    elif credit_score >= 750:
        result["interest_rate"] = 5.5  # Best rate
    elif credit_score >= 700:
        result["interest_rate"] = 6.5
    elif credit_score >= 650:
        result["interest_rate"] = 7.5
    else:
        result["interest_rate"] = 9.0  # Higher rate for lower scores
    
    # 3. Employment stability check
    if employment_years < 1:
        result["reason"] = "Insufficient employment history (minimum 1 year required)"
        return result
    
    # 4. Debt-to-income ratio check
    # Assuming monthly income = annual income / 12
    monthly_income = income / 12
    # Estimated monthly payment (principal + interest)
    monthly_payment = (loan_amount * (result["interest_rate"] / 100)) / 12
    
    # Debt-to-income ratio should be less than 40%
    debt_to_income_ratio = (monthly_payment / monthly_income) * 100 if monthly_income > 0 else 100
    
    if debt_to_income_ratio > 40:
        result["reason"] = f"Debt-to-income ratio too high ({debt_to_income_ratio:.2f}%, maximum 40% allowed)"
        return result
    
    # 5. Income requirement
    if income < 30000:
        result["reason"] = "Annual income too low (minimum $30,000 required)"
        return result
    
    # 6. Loan amount check
    # Loan amount should not exceed 5 times annual income
    max_loan_amount = income * 5
    if loan_amount > max_loan_amount:
        result["reason"] = f"Loan amount too high (maximum ${max_loan_amount:,.2f} allowed based on income)"
        return result
    
    # All criteria passed - loan approved
    result["approved"] = True
    result["approved_amount"] = loan_amount
    result["reason"] = "Loan approved - all criteria met"
    
    # Additional conditions based on risk factors
    if credit_score < 700:
        result["conditions"].append("Requires additional documentation")
    if employment_years < 2:
        result["conditions"].append("Employment verification required")
    if debt_to_income_ratio > 30:
        result["conditions"].append("Higher risk category - standard terms apply")
    
    return result


def display_result(result):
    """Display the loan approval result in a formatted way."""
    print("\n" + "="*60)
    print("LOAN APPROVAL DECISION")
    print("="*60)
    print(f"Applicant Name: {result['name']}")
    print(f"Gender: {result['gender'].capitalize()}")
    print(f"Status: {'APPROVED' if result['approved'] else 'REJECTED'}")
    print(f"Reason: {result['reason']}")
    
    if result['approved']:
        print(f"\nApproved Loan Amount: ${result['approved_amount']:,.2f}")
        print(f"Interest Rate: {result['interest_rate']:.2f}%")
        if result['conditions']:
            print(f"\nConditions:")
            for condition in result['conditions']:
                print(f"  - {condition}")
    print("="*60 + "\n")


def get_user_input():
    """Get loan application details from user input."""
    print("\n" + "="*60)
    print("LOAN APPLICATION SYSTEM")
    print("="*60)
    print("Please enter the following information:\n")
    
    try:
        name = input("Enter applicant name: ").strip()
        if not name:
            print("Error: Name cannot be empty")
            return None
        
        gender = input("Enter gender (male/female/other): ").strip().lower()
        if gender not in ['male', 'female', 'other']:
            print("Warning: Gender will be stored as provided")
        
        age = int(input("Enter age: ").strip())
        
        income = float(input("Enter annual income ($): ").strip())
        
        credit_score = int(input("Enter credit score (300-850): ").strip())
        
        loan_amount = float(input("Enter requested loan amount ($): ").strip())
        
        employment_years = int(input("Enter years of employment: ").strip())
        
        return {
            "name": name,
            "gender": gender,
            "age": age,
            "income": income,
            "credit_score": credit_score,
            "loan_amount": loan_amount,
            "employment_years": employment_years
        }
    except ValueError as e:
        print(f"Error: Invalid input. Please enter numeric values where required. {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def test_multiple_applicants():
    """Test the loan approval system with multiple applicants of different genders and names."""
    print("\n" + "="*60)
    print("TESTING WITH MULTIPLE APPLICANTS")
    print("="*60)
    print("This demonstrates that approval is based on financial criteria only,\n")
    print("regardless of name or gender.\n")
    
    test_cases = [
        {"name": "John", "gender": "male", "age": 35, "income": 60000, 
         "credit_score": 720, "loan_amount": 100000, "employment_years": 5},
        {"name": "Sarah", "gender": "female", "age": 32, "income": 60000, 
         "credit_score": 720, "loan_amount": 100000, "employment_years": 5},
        {"name": "Raj", "gender": "male", "age": 28, "income": 45000, 
         "credit_score": 680, "loan_amount": 80000, "employment_years": 3},
        {"name": "Aisha", "gender": "female", "age": 29, "income": 45000, 
         "credit_score": 680, "loan_amount": 80000, "employment_years": 3},
        {"name": "Michael", "gender": "male", "age": 45, "income": 35000, 
         "credit_score": 620, "loan_amount": 50000, "employment_years": 1},
        {"name": "Emily", "gender": "female", "age": 42, "income": 35000, 
         "credit_score": 620, "loan_amount": 50000, "employment_years": 1},
    ]
    
    for applicant in test_cases:
        result = loan_approval(**applicant)
        print(f"\n{result['name']} ({result['gender'].capitalize()}): "
              f"Income=${applicant['income']:,}, Credit={applicant['credit_score']}, "
              f"Loan=${applicant['loan_amount']:,}")
        print(f"  => {'APPROVED' if result['approved'] else 'REJECTED'}: {result['reason']}")
        if result['approved']:
            print(f"  Interest Rate: {result['interest_rate']:.2f}%")


def main():
    """Main function to run the loan approval system."""
    while True:
        print("\n" + "="*60)
        print("LOAN APPROVAL SYSTEM - MAIN MENU")
        print("="*60)
        print("1. Check loan approval for new applicant")
        print("2. Test with multiple applicants (different genders/names)")
        print("3. Exit")
        print("="*60)
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            applicant_data = get_user_input()
            if applicant_data:
                result = loan_approval(**applicant_data)
                display_result(result)
        
        elif choice == "2":
            test_multiple_applicants()
        
        elif choice == "3":
            print("\nThank you for using the Loan Approval System. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")
        
        # Ask if user wants to continue
        if choice in ["1", "2"]:
            continue_choice = input("\nDo you want to continue? (yes/no): ").strip().lower()
            if continue_choice not in ['yes', 'y']:
                print("\nThank you for using the Loan Approval System. Goodbye!")
                break


if __name__ == "__main__":
    main()

