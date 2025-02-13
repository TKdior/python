def basic_operations():
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit ")

    # Choose a number from 1 to 5
    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("BYE")
        return

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        result = num1 + num2
        print(f"Addition: {result}")
    elif choice == 2:
        result = num1 - num2
        print(f"Subtraction: {result}")
    elif choice == 3:
        result = num1 * num2
        print(f"Multiplication: {result}")
    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
            print(f"Division: {result}")
        else:
            print("The operation is not possible")
    else:
        print("Invalid choice!")

# Call the function to execute
basic_operations()
