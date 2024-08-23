# Bonus Challenge:
# Modify the function to handle a list of integers, determining if each is "Weird" or "Not Weird"
# based on the original rules. Print the result for each integer on a new line.
# Additional Requirements:
# - If an integer is outside the range (1 <= n <= 100), print "Invalid."
# - Implement this without using loops.
# Input: A list of integers.
# Output: For each integer, print "Weird," "Not Weird," or "Invalid" on a new line.

def WeirdnotWeird(x):
    if not isinstance(x, int):
        return "Invalid"
    elif x < 1 or x > 100:
        return "Invalid"
    elif x % 2 == 1 or (x % 2 == 0 and x in range(6, 21)):
        return "Weird"
    elif x % 2 == 0 and x in range(2, 6) or (x > 20 and x % 2 == 0):
        return "Not Weird"

nums = [3, 24, 105, 18, 4, "a", 101, 21, 1, 0]
check_nums = map(WeirdnotWeird, nums)

print('\n'.join(map(str, check_nums))) 


