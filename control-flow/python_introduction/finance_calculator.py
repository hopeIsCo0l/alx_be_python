# finance_calculator.py

# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Assume an annual interest rate of 5%
annual_interest_rate = 0.05

# Calculate projected annual savings after one year with interest
projected_savings = monthly_savings * 12 * (1 + annual_interest_rate)

# Print the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

