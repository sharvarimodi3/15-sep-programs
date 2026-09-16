while True:
    user_choice = input("Enter your choice (+, -, *, /, ! or exit): ")

    if user_choice == "exit":
        break

    match user_choice:
        case '+':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")

        case '-':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        case "*":
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        case "/":
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Division by zero cannot be performed")
        case "!":
            num1 = int(input("Enter the number to calculate factorial: "))
            if num1 < 0:
                print("Factorial is not defined for negative numbers")
            else:
                factorial = 1
                for i in range(1, num1 + 1):
                    factorial *= i
                print(f" factorial of {num1} is: {factorial}")
        case _:
            print("Invalid choice, please try again!")
        