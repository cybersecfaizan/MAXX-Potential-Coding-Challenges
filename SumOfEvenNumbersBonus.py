# Task: Calculate the sum of even-indexed even numbers in the array.
# Constraints: 1 <= len(arr) <= 1000, -10^6 <= arr[i] <= 10^6
# Example: [1, 2, 3, 4, 5, 6] -> 0
# Example: [-2, -4, 5, 7] -> -2

def sum_evens(x):
    total_evens = 0
    if not 1 <= len(x) <= 1000:
        return 'The array size is not in the correct range'
    if any(i > 1000000 for i in x):
        return 'Some element(s) are above the allowed maximum of 1,000,000'
    for (index, value) in enumerate(x):
        if index % 2 == 0 and value % 2 == 0:
            total_evens += value
    return total_evens
    
    
x = [1, 2, 3, 4, 5, 6]
y = [-2, -4, 5, 7]
print(sum_evens(x))
print(sum_evens(y))