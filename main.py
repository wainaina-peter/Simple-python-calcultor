#Simple python Calculator:
def sum(a,b):
    addition = a + b
    return addition

def minus(a,b):
    subtraction = a - b
    return subtraction

def multiplication(a,b):
    times = a * b
    return times

def division(a,b):
    divide = a // b
    return divide

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

calculation = input('''
Choose the calculation to be performed:
1.Addition(A)
2.Subtraction(S)
3.Multiplication(M)
4.Division(D)
: ''')

if calculation == 'A':
    my_sum = sum(x, y)
    print("The sum of the two numbers is : ", my_sum)
elif calculation == 'S':
    my_minus = minus(x,y)
    print("The difference of the two numbers is: ", my_minus)
elif calculation == 'M':
    my_times = multiplication(x,y)
    print("The product of the two numbers is: ", my_times)
elif calculation == 'D':
    my_div = division(x,y)
    print("The result of dividing the two numbers is: ",my_div)
else:
    print("Wrong input, please try again!")
