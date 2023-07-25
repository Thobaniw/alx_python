def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_numbers = [0, 1]
        for i in range(2, n):
            next_num = fibonacci_numbers[-1] + fibonacci_numbers[-2]
            fibonacci_numbers.append(next_num)
        return fibonacci_numbers
