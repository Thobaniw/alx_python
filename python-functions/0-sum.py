def add(a, b):
    # Handle negative numbers correctly
    if b >= 0:
        while b:
            a, b = a ^ b, (a & b) << 1
    else:
        while b:
            a, b = a ^ b, ((~a) & b) << 1
    return a

