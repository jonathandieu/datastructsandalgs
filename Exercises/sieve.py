def sieve(num: int):
    pass

def prime_comprehension(num: int):
    return [i for i in range(num) if is_prime(i)]


def is_prime(num: int):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True
