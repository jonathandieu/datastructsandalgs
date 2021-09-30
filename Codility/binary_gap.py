# Given an integer, return the maximal sequence of consecutive zeros surrounded by 1s at both ends of the binary representation

def binary_gap(n: int) -> int:
    # Convert from decimal to binary
    bin_representation = bin(n).strip("0b")
    print(bin_representation)

    # Strip the trailing 0s
    bin_representation = bin_representation.strip("0")
    print(bin_representation)

    # Split up the remaining 0s by separating by 1
    bin_representation = bin_representation.split("1")
    print(bin_representation)

    # Return length of the longest string of zeros
    return len(max(bin_representation))


print(binary_gap(45))