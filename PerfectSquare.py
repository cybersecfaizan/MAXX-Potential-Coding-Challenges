# Task: Determine if a given number is a perfect square.
# Constraints: 1 <= n <= 10^9.
# Output: Return true if the number is a perfect square, otherwise false.
# Example: 16 -> true, 5 -> false

import math

def check_perfect_square(number):
    if not 1 <= number <= 10**9:
        return "Number out of range"
    return True if math.isqrt(number) ** 2 == number else False

print(check_perfect_square(16))
print(check_perfect_square(5))