# Errors can be handled by "Try and Except" 
def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid Argument')
print(spam(1))
print(spam(10))
print(spam(0))
print(spam(21)) 

# Once an except clause is triggered it does not return to the try clause
def spam(divideBy):
    return 42/divideBy
try:
    print(spam(12))
    print(spam(212))
    print(spam(0))
    print(spam(21))
except ZeroDivisionError:
    print('Error: Invalid Argument')

