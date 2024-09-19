
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

operation = input("choose the operation (+,-,*,/): ")

match operation:
    case '+':
        result = num1 + num2
        print(f"the result is {result}")

    case '-':
        result = num1 - num2
        print(f"the result is {result}") 

    case '*':
        result = num1 * num2
        print(f"the result is {result}") 

    case '/':
        result = num1 / num2
        print(f"the result is {result}")
    case _:
        print("invalid operations selected")    

              