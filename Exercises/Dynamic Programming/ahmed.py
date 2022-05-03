def best_candidates(row1: list, row2: list):

    candidates = [row1, row2]
    print("Candidates: ", candidates)
    num_students = len(row1)
    for row in candidates:
        for candidate in row:
            print(str(candidate) + " ", end="")
        print()

    memo_dp = [[0 for student in range(num_students)] for row in range(2)]
    print (memo_dp)

    for i in range(num_students):
        if i == 0:
            memo_dp[0][i] = candidates[0][0]
            memo_dp[1][i] = candidates[1][0]
        else:
            # Get the max for the last row and then add current index
            memo_dp[0][i] = max(memo_dp[0][i - 1], memo_dp[1][i - 1] + candidates[0][i])
            memo_dp[1][i] = max(memo_dp[1][i - 1], memo_dp[0][i - 1] + candidates[1][i])

    return max(memo_dp[0][num_students - 1], memo_dp[1][num_students - 1])


if __name__ == "__main__":
    row1 = [1, 2, 9]
    row2 = [10, 1, 1]
    print(best_candidates(row1, row2))
