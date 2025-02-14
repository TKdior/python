# Function basics arithmetics operations
def basic_arithmetic_operations():
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
basic_arithmetic_operations()


def basic_bitwise_operations():
    print("Select an operation:")
    print("1. AND")
    print("2. OR")
    print("3. XOR")
    print("4. LEFT SHIFT ")
    print("5. RIGHT SHIFT ")
    print("6. NOT")
    print("7. Exit ")

    # Choose a number from 1 to 5
    choice = int(input("Enter your choice: "))
    if choice == 7:
        print("BYE")
        return

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if choice == 1:
        result = num1 & num2
        print(f"AND: {result}")
    elif choice == 2:
        result = num1 |  num2
        print(f"OR: {result}")
    elif choice == 3:
        result = num1 ^ num2
        print(f"XOR: {result}")
    elif choice == 4:
        result = num1 << num2
        print(f"LEFT SHIFT: {result}")
    elif choice == 5:
        result = num1 >> num2
        print(f"RIGHT SHIFT: {result}")
    elif choice == 6:
        result = ~num1
        print(f"NOT: {result}")
    else:
        print("Invalid choice!")

# Call the function to execute
basic_bitwise_operations()
