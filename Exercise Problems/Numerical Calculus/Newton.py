# Import the library necessary for math functions
import math

# Initial approximation
initial = -200

# This represents our polynomial: x^2 - x^2 + 2
f = lambda x: x**3 - x**2 + 2

# First derivative of f(x):
first_deriv = lambda x: 3*x**2 - 2*x

# Set our root initially to a null value as a placeholder
root = None

# Set our number of iterations as 0
iterations = 0
max = 15
# The tolerance for the function
tolerance = 0.01

# Loop that calculates the root using Netwon's Method as long as the
# iterations have not exceeded their max
while (iterations < max):
    # Check if the derivative is 0, as Newton's method stipulates
    # that f'(P_n-1) cannot be 0 at any point
    if (first_deriv(initial) != 0):
        # We set the next to be equal to the previous minus f(prev) divided by f'(prev)
        next = initial - f(initial) / first_deriv(initial)

        # If the method successfuly finds the root
        if (abs(next - initial) < tolerance):
            # The next approximation will be the root we want
            root = next
            print("The procedure was succesful.")
            print("The value of the root is :", root)
            break

        # If we haven't reached the threshold for success
        iterations += 1
        initial = next



# If the method fails to find the root
if (root == None):
    print("The method failed after", iterations, "iterations")