# write a function that takes in two numbers as arguments and returns their sum
def add(a, b):
    return a + b

# write a function that takes in two numbers as arguments and returns their difference
def difference(a, b):
    return a - b

# write a function that takes in two numbers as arguments and returns their product
def product(a, b):
    return a * b

# write a function that takes in two numbers as arguments and returns their quotient (float if there is a remainder)
def quotient(a, b):
    if a % b == 0:
        return int(a / b)
    else:
        return a * 1.0 / b

# write a function that takes in two numbers as arguments and returns their remainder
def remainder(a, b):
    return a % b

# write a function that takes two numbers and an operator and return the result
# I'm sure this is way more lengthy than need be a could be refactored
def calculator(a, b, op):
    if op.lower() == 'add':
        return add(a, b)
    elif op.lower() == 'subtract':
        return difference(a, b)
    elif op.lower() == 'multiply':
        return product(a, b)
    elif op.lower() == 'divide':
        return quotient(a, b)
    elif op.lower() == 'remainder':
        return remainder(a, b)


print(add(3, 2))
print(difference(5, 4))
print(product(7, 3))
print(quotient(15.0, -3))
print(quotient(16, -3))
print(remainder(19, 5))
print(calculator(3,5,'multiply'))