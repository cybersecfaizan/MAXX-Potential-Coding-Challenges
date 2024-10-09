# Task: Write a function to check if a given string is a palindrome.
# Constraints: 1 <= string length <= 1000.
# Output: Return 'Yes' if the string is a palindrome, otherwise 'No'.
# Example: 'racecar' -> 'Yes', 'hello' -> 'No'

def is_palindrome(input_string):
    string_length = len(input_string)
    reversed_string = input_string[::-1]
    if not 1 <= string_length <= 1000:
        return "That's not in the correct range"
    if input_string == reversed_string:
        return "Yes"
    else:
        return "No"

input_string_1 = "racecar"
input_string_2 = "hello"

print(is_palindrome(input_string_1))
print(is_palindrome(input_string_2))