# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform division with error handling for zero division and non-numeric inputs.
    
    Parameters:
    - numerator (str): The numerator for the division.
    - denominator (str): The denominator for the division.
    
    Returns:
    - str: The result of the division or an error message.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
