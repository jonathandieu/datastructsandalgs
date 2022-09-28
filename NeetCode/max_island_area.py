def maxAreaOfIsland(grid) -> int:
    max_area = 0

    ROWS = len(grid)
    COLS = len(grid[0])
    def dfs(row, col):
            # base case:
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] != 1:
                return 0
            grid[row][col] = "nina"
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col]:
                max_area = max(max_area, dfs(row, col))
                print(max_area)
    return max_area
