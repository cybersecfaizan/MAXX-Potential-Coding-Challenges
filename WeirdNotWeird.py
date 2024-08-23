#!/usr/bin/python
# Given an integer n, print "Weird" if n is odd or if n is even and falls within the inclusive range of 6 to 20. If n is even and falls within the inclusive range of 2 to 5, or if n is even and greater than 20, print "Not Weird". The integer n is constrained to be between 1 and 100, inclusive.

x = int(input("Enter a Whole Number Between 1 and 100 "))
if x < 1 or x > 100:
    print("That's out of range")
elif x % 2 == 1 or (x % 2 == 0 and x in range(6, 21)):
    print("Weird", x)
elif x % 2 == 0 and x in range(2, 6) or (x > 20 and x % 2 == 0):
    print("Not Weird", x)