def pow(a, b):
    # Handle negative exponent correctly
    if b < 0:
        a = 1 / a
        b = -b

    result = 1
    while b:
        if b & 1:
            result *= a
        a *= a
        b >>= 1

    return result
pow = __import__('1-power').pow

result = pow(2, 2)
print(result) 

result = pow(98, 2)
print(result) 

result = pow(98, 0)
print(result) 

result = pow(100, -2)
print(result)  

result = pow(-4, 5)
print(result)  

