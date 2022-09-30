def number_of_islands(grid: list) -> int:
    # initilize return variable and dimensions
    num_islands = 0

    ROWS = len(grid)
    COLS = len(grid[1])
    visited = set()

    def dfs(row, col):
        # base case
        if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] != 1 or grid[row][col] in visited:
            return 0
        # recursive case
        visited.add((row,col))
        return 1 + dfs(row + 1, col) + dfs(row -1, col) + dfs(row, col + 1) + dfs(row, col - 1)


    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col]:
                num_islands = dfs(row, col)
    return num_islands
