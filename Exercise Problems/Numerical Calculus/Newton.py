global x0 = 
iterations = 0
tolerance = 0.01
root = "placeholder"

difference =
# Loop that calculates the root using the Bisection Method
while ( difference >= tolerance):
    iterations += 1
    y = x
# If the method successfuly finds the root
print("The procedure was succesful.")
print("The value of the root is :", root)
# If the method fails to find the root
print("The method failed after", iterations, "iterations")