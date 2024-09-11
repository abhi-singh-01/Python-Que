def print_primes_and_evens(n):
    """
    Print all prime numbers and even numbers up to n
    """
    for num in range(2, n + 1):
        if num % 2 == 0:
            print(f"{num} is even")
        isPrime = True
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                isPrime = False
                break
        if isPrime:
            print(f"{num} is prime")

# Test the function
print_primes_and_evens(100)