def is_out_of_bounds(grid, row, col):
    return row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0])


grid = []
with open("input.txt", "r", encoding="utf8") as file:
    for line in file:
        row = []
        for char in line.strip():
            row.append(char)
        grid.append(row)

count = 0
for row_id in range(len(grid)):
    for col_id in range(len(grid[0])):
        if grid[row_id][col_id] != "A":
            continue
        if is_out_of_bounds(grid, row_id - 1, col_id - 1):
            continue
        if is_out_of_bounds(grid, row_id - 1, col_id + 1):
            continue
        if is_out_of_bounds(grid, row_id + 1, col_id - 1):
            continue
        if is_out_of_bounds(grid, row_id + 1, col_id + 1):
            continue
        mas_count = 0
        if grid[row_id - 1][col_id - 1] == "M" and grid[row_id + 1][col_id + 1] == "S":
            mas_count += 1
        if grid[row_id - 1][col_id + 1] == "M" and grid[row_id + 1][col_id - 1] == "S":
            mas_count += 1
        if grid[row_id + 1][col_id - 1] == "M" and grid[row_id - 1][col_id + 1] == "S":
            mas_count += 1
        if grid[row_id + 1][col_id + 1] == "M" and grid[row_id - 1][col_id - 1] == "S":
            mas_count += 1
        if mas_count == 2:
            count += 1
print(count)
