def matrix_multiply(a, b):
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
    ]


def matrix_power(matrix, n):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, matrix)
        matrix = matrix_multiply(matrix, matrix)
        n //= 2
    return result


def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(matrix, n - 1)
    fib_n = result_matrix[0][0]

    fib_sequence = [0]
    a, b = 0, 1
    for _ in range(1, n):
        fib_sequence.append(b)
        a, b = b, a + b

    return fib_sequence


# Get user input for the number of terms in the Fibonacci sequence
try:
    n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        result = generate_fibonacci(n)
        print(f"Fibonacci sequence with {n} terms: {result}")
except ValueError:
    print("Invalid input or too large, using default value (e.g., 1000)")
    n = 1000
    result = generate_fibonacci(n)
    print(f"Fibonacci sequence with {n} terms: {result}")
