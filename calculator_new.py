

import sys


def addition(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    sub = num1 - num2
    return sub

def mul(num1, num2):
    mul = num1 * num2
    return mul

print(addition(5, 10)) #
print(sub(10, 5)) #
print(mul(10, 5)) #

if len(sys.argv) < 4:
    print("Usage: python calculator_new.py num1 operation num2")
else:
    num1 = int(sys.argv[1])
    operation = sys.argv[2]
    num2 = int(sys.argv[3])
    if operation == 'add':
        result = addition(num1, num2)
    elif operation == 'sub':
        result = sub(num1, num2)
    elif operation == 'mul':
        result = mul(num1, num2)
    else:
        result = "Invalid operation"
    print(f"Result: {result}")
