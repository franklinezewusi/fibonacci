def generating_fibonacci(n):
    fibonacci_sequence = []
    
    a, b = 0, 1 

    while a <= n:
        fibonacci_sequence.append(a)
        a, b = b, a + b  
    
    return fibonacci_sequence
answer = generating_fibonacci(50)
print(answer)
