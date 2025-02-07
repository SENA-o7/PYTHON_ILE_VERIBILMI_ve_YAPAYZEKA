def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for fib in fibonacci_generator(10):
    print(fib)
    """
    #bu kullanım generator değildir ve bellekte daha fazla yer kaplar
    def fibonacci_list(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Kullanım
for fib in fibonacci_list(10):
    print(fib)
"""