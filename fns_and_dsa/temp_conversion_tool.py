# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        # Prompt the user to enter a temperature
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        # Inform the user about the invalid input and exit
        print("Invalid temperature. Please enter a numeric value.")
        return

    # Prompt the user to specify the unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Based on the unit, perform the appropriate conversion
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
