import math

def is_prime(n):
    # Handle edge cases
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

# Example usage:
n = int(input("Enter a number: "))
print(is_prime(n))