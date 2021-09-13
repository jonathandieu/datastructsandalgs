import sys
# # Takes in a sorted list and returns the value we're looking for
# def binary_search(some_list: list, value: int) -> int:
#     # Low is set to zero, while high is the length of the list
#     high = len(some_list) - 1
#     low = 0

#     while high > low:
#         mid = (high + low)
#         guess = some_list[mid]

#         if (guess == value):
#             return mid
#         # If the guess is too high or too low, update the high and low
#         if guess > value:
#             high = mid - 1

#         else:
#             low = mid + 1

#     return None

def binary_search(list, val):
    high = len(list) - 1
    low = 0

    while high > low:
        mid = high + low
        guess = list[mid]
        if (guess == val):
            return mid
        if (guess > val):
            high = mid - 1
        elif (guess < val):
            low = mid + 1

        else:
            return None

if __name__ == "__main__":
    listy_list = [-1, 0, 5]
    print("You're looking for: ", sys.argv[1])
    print("This element is found in index: ", binary_search(listy_list, int(sys.argv[1])))