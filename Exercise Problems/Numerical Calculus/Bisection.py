# Import the library necessary for math functions
import math

# This represents our polynomial: x^2 - x^2 + 2
f = lambda x: x**3 - x**2 + 2

# Set our root initially to a null value
root = None

# Set our number of iterations as 0
iterations = 0

# The tolerance for the function
tolerance = 0.01

# First, choose the starting interval where the function at
# the endpoints is less than 0 and they have differing signs
left = -200
right = 300

# Find the upper bound on the number of iterations
# The upper bound is calculated as n >= log((b-a)/tolerance) / log(2)
max = math.ceil(math.log(500/.01, 10) / math.log(2,10))


# Loop that calculates successive approximations
while (abs(right - left) > tolerance and iterations < max):
    # Find the midpoint between them to get arithmetic mean
    iterations += 1
    midpoint = (left + right) / 2

    # When f(midpoint) has the same sign as f(right) we update the right with the midpoint
    if (f(left) < 0 and f(midpoint) > 0) or (f(left) > 0 and f(midpoint) < 0):
        right = midpoint
    # Otherwise, we set the left equal to the current midpoint
    else:
        left = midpoint

# Once we exit the loop, we will have either found the root or failed to
root = "{:.4f}".format(midpoint)

# If the method successfuly finds the root
print("The procedure was succesful.")
print("The value of the root is :", root)

# If the method fails to find the root
if (root == None):
    print("The method failed after", iterations, "iterations")
