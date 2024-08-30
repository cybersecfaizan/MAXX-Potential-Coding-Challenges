# Function to find and return all duplicate elements in an array.
# Constraints: Array length is between 1 and 1000 (inclusive), and elements are between 0 and 10^6 (inclusive).
# Output: A list of duplicate elements.
# Example:
#   Input: [1, 2, 3, 2, 4, 5, 6, 5]
#   Output: [2, 5]
#   Input: [1, 1, 2, 3, 3]
#   Output: [1, 3]

def check_duplicates(x):
    arr = (x)
    seen = {}
    duplicate_array = []
    if len(arr) < 1 or len(arr) > 1000:
        return "The array size is not in the correct range"
    if any(i > 1000000 for i in arr):
        return "Some element(s) are above the allowed maximum of 1,000,0000"
    for i in arr:
        if i in seen:
            duplicate_array.append(i)
        else:
            seen[i] = 0

    return duplicate_array

x = [1, 2, 3, 2, 4, 5, 6, 5]
y = [1, 1, 2, 3, 3]

print(check_duplicates(x))
print(check_duplicates(y))