import math

def calculator():
    print("Calculator")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Sine (sin)")
    print("6. Cosine (cos)")
    print("7. Tan")
    print("8. Cosec")
    print("9. Sec")
    print("10. Cot")
    choice = input("Enter your choice (1-10): ")

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", num1 + num2)
        elif choice == "2":
            print("Result:", num1 - num2)
        elif choice == "3":
            print("Result:", num1 * num2)
        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero")
            else:
                print("Result:", num1 / num2)

    elif choice in ["5", "6","7","8","9","10"]:
        angle = float(input("Enter angle in degrees: "))
        radians = math.radians(angle)

        if choice == "5":
            print("sin(", angle, ") =", math.sin(radians))
        elif choice == "6":
            print("cos(", angle, ") =", math.cos(radians))
        elif choice == "7":
            print("tan(", angle, ") =", math.tan(radians))
        elif choice == "8":
           print("cosec(", angle, ") =", 1 / math.sin(radians))
        elif choice == "9":
            print("sec(", angle, ") =", 1 / math.cos(radians))
        elif choice == "10":
            print("cot(", angle, ") =", 1 / math.tan(radians))
    else:
        print("Invalid choice!")

calculator()

