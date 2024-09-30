# Task: Write a function to reverse a string without using built-in reverse methods.
# Constraints: 1 <= string length <= 1000.
# Example: 'hello' -> 'olleh', 'Python' -> 'nohtyP'

def reverse_text(text):
    if not 1 <= len(text) <= 1000:
        return "You didn't enter the correct number of letters"
    else:
        return text[::-1]

reverse_input_1 = "hello"
reverse_input_2 = "Python"
print(reverse_text(reverse_input_1))
print(reverse_text(reverse_input_2))