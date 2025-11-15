###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input('podaj cyfre:'))
number2 = int(input('podaj cyfre:'))
operator = input('podaj operator:')

if operator == '+' :
    result = number1 + number2
elif operator == '-' :
    result = number1 - number2
elif operator == '*' :
    result = number1 * number2
elif operator == '/' :
    result = number1 / number2
else:
    print('nie ma takiego operatora')

# print result
print(f'{number1} {operator} {number2} = {result}')