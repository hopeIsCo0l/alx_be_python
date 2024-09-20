# Global conversion factors

CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
FREEZING_POINT_DIFFERENCE = 32

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """Converts a given temperature in Fahrenheit to Celsius."""
    try:
        return (fahrenheit - FREEZING_POINT_DIFFERENCE) * FAHRENHEIT_TO_CELSIUS_FACTOR
    except TypeError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """Converts a given temperature in Celsius to Fahrenheit."""
    try:
        return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FREEZING_POINT_DIFFERENCE
    except TypeError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# User interaction for temperature conversion
def main():
    try:
        # Prompting user for temperature input
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
