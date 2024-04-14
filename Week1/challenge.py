# asks for two integers and the operator
num_1 = int(input("Please input an integer: "))
num_2 = int(input("Please input another integer: "))
operator = input("Please input your desired operation (+,-,/,*,**,//,%): ")


# passes two numbers and an operator and does the associated arithmetic
def operation(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '/':
        return num1 / num2
    elif op == '*':
        return num1 * num2
    elif op == '**':
        return num1 ** num2
    elif op == '//':
        return num1 // num2
    elif op == '%':
        return num1 % num2
    else:
        return "Please input a valid mathematical operator."

# prints the result of calling the function
print(operation(num_1, num_2, operator))
