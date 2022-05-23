def say_hello_decreasing(n: int):
    if n == 0:
        return
    else:
        print("hello", n)
        say_hello_decreasing(n - 1)

# Print "hello" n times
def say_hello_increasing(n: int):
    # base case
    if n == 0:
        return
    else:
        say_hello_increasing(n - 1)
        print("hello", n)

# Return 1 + 2 + 3 + 4 + ... + n
def sum_n(n: int) -> int:
    # TRUST THIS FUNCTION
    if n == 0:
        return 0
    left_part = sum_n(n - 1)
    return n + left_part

# Given 1214: returns 1+2+1 + 4 = 8 or sd(121) + 4
def sum_digits(n: int) -> int:
    if n == 0:
        return 0

    remaining = n // 10 # Leaves us the remaining ones
    last_digit = n % 10 # Gets us the last digit
    print(f"{remaining =} {last_digit =}")
    return sum_digits(remaining) + last_digit

# WHERE YOU CALL THE RECURSIVE FUNCTION M A T T E R S
def pattern_print(n: int):
    if n == 0:
        return
    # PUT IT HERE AND WE GET 1, 12, 123, 1234...
    # pattern_print(n - 1)
    for i in range(1, n):
        print(i, end="")
    print()

    # PUT IT HERE AND WE GET 1234, 123, 12, 1...
    pattern_print(n - 1)

def pattern_print_advanced(n: int):
    # base case
    if n == 1:
        print("1")
        return

    # for i in range(1, n):
    #     print(i, " ", end="")
    # print()
    i = 1
    while i <= n:
        print(i, end="")
        i += 1
    print()

    # Recurse.
    pattern_print_advanced(n - 1) # Trust that it will print everything in the middle

    # for i in range(1, n):
    #     print(i," ", end="")
    # print()

    j = 1
    while j <= n:
        print(j, end="")
        j += 1
    print()

# TRUSS that it returns the nth fib number
def fib(n: int) -> int:

    if n == 1:
        return 0
    elif n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    say_hello_decreasing(10)
    say_hello_increasing(10)
    print(sum_n(100))
    print(sum_digits(1111))
    pattern_print_advanced(9)
    print(fib(10))