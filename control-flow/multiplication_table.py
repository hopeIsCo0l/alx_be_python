# multiplication_table.py

def main():
    # Prompt the user for a number
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Use a for loop to print the multiplication table from 1 to 10
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

if __name__ == "__main__":
    main()
