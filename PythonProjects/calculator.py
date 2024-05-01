def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

while True:
    try:
        # Get user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Display menu for operations
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        # Get user choice for operation
        choice = input("Enter choice (1/2/3/4): ")
        
        # Perform calculation based on user choice
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        else:
            print("Invalid input. Please enter a valid choice.")
            continue  # Go back to the beginning of the loop
        
        # Display the result
        print(f"\nResult: {result}")

        # Ask the user if they want to perform another calculation
        another_calculation = input("\nDo you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            break  # Exit the loop if the user does not want to perform another calculation

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")
