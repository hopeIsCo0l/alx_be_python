# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
    """
    Calculate a future date by adding a specified number of days to the current date.
    
    Parameters:
    - days (int): Number of days to add to the current date.
    
    Returns:
    - str: The future date in the format YYYY-MM-DD.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")

def main():
    # Display the current date and time
    display_current_datetime()
    
    # Prompt the user to enter the number of days
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future_date = calculate_future_date(days)
        print(f"Future date: {future_date}")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()
