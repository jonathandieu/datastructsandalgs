
def binary_search(nums, target) -> int:
    hi, lo = len(nums) - 1, 0
    mid = (hi + lo) // 2

    while hi >= lo:
        guess = nums[mid]
        if guess > target: # GUESS IS TOO HIGH. LOOK LEFT!
            hi = mid - 1
            mid = (hi + lo) // 2
        elif guess < target:
            lo = mid + 1
            mid = (hi + lo) // 2
        elif guess == target:
            # print(f"Ayo {target} is at index: {mid}")
            return mid
    # print("It ain't here, chief")
    return -1

testy = [1,5,7,8,12,15,67,75,78,100]

# user_input = int(input("gimme a number, dummy: "))
print(binary_search(testy, 100))
