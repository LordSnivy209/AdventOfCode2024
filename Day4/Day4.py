def search_word(x, y, dx, dy, word):
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if not (0 <= nx < rows and 0 <= ny < columns) or grid[nx][ny] != word[i]:
            return False
    return True

with open("input_day4", "r") as inputs:
    word = "XMAS"
    grid = [list(line.strip()) for line in inputs]
    directions = [
        (-1, 0), # up
        (1, 0), # down
        (0, -1), # left
        (0, 1), # right
        (1, 1), # diag down right
        (-1, 1), # diag up right
        (1, -1), # diag down left
        (-1, -1) # diag up left
    ]

    rows = len(grid)
    columns = len(grid[0])

count = 0

for x in range(rows):
    for y in range(columns):
        for dx, dy in directions:
            if search_word(x, y, dx, dy, word):
                count += 1

print(count)