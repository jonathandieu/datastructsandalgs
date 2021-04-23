# Import the library necessary for math functions
import math

# Initial approximation
initial = -200

# This represents our polynomial: x^2 - x^2 + 2
f = lambda x: x**3 - x**2 + 2

# This represents our g(x) function as given by Professor Jahani
g = lambda x: 1 - 2*x**-2

# Set our root initially to a null value as a placeholder
root = None

# Set our number of iterations as 0
iterations = 0
max = 15

# The tolerance for the function
tolerance = 0.01

# Loop that continues as long as our iterations haven't
# exceeded the max or until we get an acceptable answer
while (iterations < max):
    # We use the g(x) function to approximate the root
    root = g(initial)
    # If this approximation is close enough to the root within the given
    # tolerance, we can just return having successfully done so
    if (abs(root - initial) < tolerance):
        # If the method successfuly finds the root
        print("The procedure was succesful.")
        print("The value of the root is :", root)
        break
    # If not, we continue the loop having incremented the iterations
    # and set the initial to the root calculated during the iteration
    iterations += 1
    initial = root

# If the method fails to find the root
if (root == None or iterations > max):
    print("The method failed after", iterations, "iterations")