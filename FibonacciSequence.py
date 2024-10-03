# Task: Write a function to return the nth Fibonacci number.
# Constraints: 0 <= n <= 30.
# Example: 5 -> 5, 10 -> 55

def fibonacci_sequence(term_limit):
    if not 0 <= term_limit <= 30:
        return "That's not in the correct range"
    
    previous = 0
    current = 1
    result = 0
    for i in range(term_limit - 1):
        result = previous + current
        previous = current
        current = result
    
    return result

term_limit_1 = 5
term_limit_2 = 10
print(fibonacci_sequence(term_limit_1))
print(fibonacci_sequence(term_limit_2))