# Challenge: Check if a string of parentheses is balanced.
# The goal is to determine whether every opening parenthesis "(" has a corresponding closing parenthesis ")".
# Constraints: The input string length ranges from 1 to 10^4.
# Output: Return True if the string is balanced, otherwise return False.
# Example 1: Input: "((Bal(a)nce))" -> Output: True
# Example 2: Input: "((())" -> Output: False

def balance_checker(x):
    y = 0
    z = 0
    if len(x) < 1 or len(x) > 10000:
        return "The size is not in the correct range"
    for i in x:
        if i == "(":
            y += 1
        elif i == ")":
            z += 1

    if y == z:
        return True
    else:
        return False

x = "((Bal(a)nce))"
y = "((())"
print(balance_checker(x))
print(balance_checker(y))