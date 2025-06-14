def add_binary(a,b):
    n = a+b
    return str(decimal_to_binary(n))
def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    elif decimal_number == 1:
        return "1"
    else:
        return decimal_to_binary(decimal_number // 2) + str(decimal_number % 2)
"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
The binary number returned should be a string.
"""