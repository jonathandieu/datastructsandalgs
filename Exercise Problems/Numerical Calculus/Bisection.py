# Import the library necessary for math functions
import math

f = lambda x: x**3 - x**2 + 2
print(f(1))
iterations = 0
root = "placeholder"
tolerance = 0.01
# First, choose the starting interval where the function at
# the endpoints is less than 0 and they have differing signs
left = -200
right = 300

# Find the upper bound on the number of iterations
max = math.ceil(2 / math.log(2,10))
print(max)
max = 16

# Loop that calculates
while (abs(right - left) > tolerance and iterations < max):
    # Find the midpoint between them
    iterations += 1
    midpoint = (left + right) / 2

    if ((f(left) < 0 and f(midpoint) > 0)) or (f(left) > 0 and f(midpoint) < 0):
        right = midpoint
    else:
        left = midpoint

print(midpoint)




# If the method successfuly finds the root
print("The procedure was succesful.")
print("The value of the root is :", root)
# If the method fails to find the root
print("The method failed after", iterations, "iterations")
