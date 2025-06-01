Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> number1 = 10
number2 = 5

sum_result = number1 + number2
difference = number1 - number2
product = number1 * number2

print(f"Addition of {number1} and {number2} is {sum_result}")
print(f"Subtraction of {number1} and {number2} is {difference}")
print(f"Multiplication of {number1} and {number2} is {product}")
>>> number1 = 10
>>> number2 = 5
>>> sum_result = number1 + number2
>>> difference = number1 - number2
>>> product = number1 * number2
>>> print(f"Addition of {number1} and {number2} is {sum_result}")
SyntaxError: invalid syntax
>>> print Addition of {number1} and {number2} is {sum_result}
SyntaxError: invalid syntax
>>> print sum_result = number1 + number2
SyntaxError: invalid syntax
>>> print sum_result
15
>>> print difference
5
>>> print product
50
>>> 
