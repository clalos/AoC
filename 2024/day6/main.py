obstacles_positions = {}
current_guard_pos = ()
tot_rows = 0
tot_cols = 0


# Find the next obstacle coord in obstacle_positions.
# obstancle_positions is a dictionary with keys as tuple of (row, col) and values as None.
def next_obstacle(current_guard_pos, obstacles_positions, direction):
    if direction == "up":
        for row in range(current_guard_pos[0] - 1, -1, -1):
            if (row, current_guard_pos[1]) in obstacles_positions:
                return (row, current_guard_pos[1])
    elif direction == "right":
        for col in range(current_guard_pos[1] + 1, tot_cols):
            if (current_guard_pos[0], col) in obstacles_positions:
                return (current_guard_pos[0], col)
    elif direction == "down":
        for row in range(current_guard_pos[0] + 1, tot_rows):
            if (row, current_guard_pos[1]) in obstacles_positions:
                return (row, current_guard_pos[1])
    elif direction == "left":
        for col in range(current_guard_pos[1] - 1, -1, -1):
            if (current_guard_pos[0], col) in obstacles_positions:
                return (current_guard_pos[0], col)
    return None


with open("input.txt", "r", encoding="utf8") as file:
    for line in file:
        for col, char in enumerate(line):
            if char == "#":
                obstacles_positions[tot_rows, col] = None
            if char == "^":
                current_guard_pos = (tot_rows, col)
        tot_cols = len(line)
        tot_rows += 1

if current_guard_pos == ():
    raise ValueError("Guard position '^' not found in the input file.")

total_unique_path_coords = {}
cur_direction = "up"
while True:
    next_obstacle_coord = next_obstacle(
        current_guard_pos, obstacles_positions, cur_direction
    )
    if next_obstacle_coord is None:
        # Add the last path coordinates until the end of the grid.
        if cur_direction == "up":
            for row in range(current_guard_pos[0], -1, -1):
                total_unique_path_coords[row, current_guard_pos[1]] = None
        elif cur_direction == "right":
            for col in range(current_guard_pos[1], tot_cols):
                total_unique_path_coords[current_guard_pos[0], col] = None
        elif cur_direction == "down":
            for row in range(current_guard_pos[0], tot_rows):
                total_unique_path_coords[row, current_guard_pos[1]] = None
        elif cur_direction == "left":
            for col in range(current_guard_pos[1], -1, -1):
                total_unique_path_coords[current_guard_pos[0], col] = None
        break
    if cur_direction == "up":
        for row in range(current_guard_pos[0], next_obstacle_coord[0], -1):
            total_unique_path_coords[row, current_guard_pos[1]] = None
        current_guard_pos = next_obstacle_coord[0] + 1, next_obstacle_coord[1]
        cur_direction = "right"
    elif cur_direction == "right":
        for col in range(current_guard_pos[1], next_obstacle_coord[1]):
            total_unique_path_coords[next_obstacle_coord[0], col] = None
        current_guard_pos = next_obstacle_coord[0], next_obstacle_coord[1] - 1
        cur_direction = "down"
    elif cur_direction == "down":
        for row in range(current_guard_pos[0], next_obstacle_coord[0]):
            total_unique_path_coords[row, next_obstacle_coord[1]] = None
        current_guard_pos = next_obstacle_coord[0] - 1, next_obstacle_coord[1]
        cur_direction = "left"
    elif cur_direction == "left":
        for col in range(current_guard_pos[1], next_obstacle_coord[1], -1):
            total_unique_path_coords[next_obstacle_coord[0], col] = None
        current_guard_pos = next_obstacle_coord[0], next_obstacle_coord[1] + 1
        cur_direction = "up"


print(f"Number of unique path coordinates: {len(total_unique_path_coords)}")
