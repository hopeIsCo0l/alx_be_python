# future_age_calculator.py

# Prompt the user for their current age
current_age = input("How old are you? ")

# Convert the input string to an integer
current_age = int(current_age)

# Calculate the age in 2050
future_year = 2050
current_year = 2023
years_to_add = future_year - current_year
age_in_2050 = current_age + years_to_add

# Print the result
print(f"In {future_year}, you will be {age_in_2050} years old.")

