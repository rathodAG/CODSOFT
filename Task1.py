def simple_calculator():
    print("Welcome")

    while True:
        # Input: First number
        num1 = float(input("Enter the first number: "))
        
        # Input: Second number
        num2 = float(input("Enter the second number: "))
        
        # Input: Operation choice
        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter the operation (1/2/3/4) or 'e' to exit: ")

        # Perform calculation based on operation choice
        if operation == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Cannot divide by zero.")
        elif operation.lower() == 'e':
            print("Thank you for using the calculator. Goodbye!")
            break
        else:
            print("Invalid operation choice. Please select a valid operation.")

# Run the calculator
simple_calculator()
