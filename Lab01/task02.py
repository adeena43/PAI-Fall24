operand1 = float(input("Enter first number: "))
operand2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if(operator == '+'):
    print('SUM: ', abs(-operand1-operand2))

elif(operator == '-'):
    print('DIFFERENCE: ',operand1-operand2)

elif(operator == '*'):
    print('PRODUCT: ',operand1 * operand2)

elif(operator == '/'):
    print('QUOTIENT: ',operand1 / operand2)

else:
    print("Invalid operator")
