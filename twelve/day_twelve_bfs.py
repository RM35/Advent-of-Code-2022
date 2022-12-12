from collections import deque
from copy import deepcopy

grid = []
with open("twelve/day_twelve_input.txt") as f:
    grid = f.readlines()
    grid = list(map(lambda x: x.strip(), grid))
    for i, line in enumerate(grid):
        grid[i] = list(map(ord, line))

H = len(grid) # HEIGHT
W = len(grid[0]) # WIDTH

start = (0, 0)
end = (0, 0)

# set the start and end to a -1 ord and z + 1 ord
for y in range(H):
    for x in range(W):
        if grid[y][x] == 83:
            start = (y, x)
            grid[y][x] = 96
        if grid[y][x] == 69:
            end = (y, x)
            grid[y][x] = 123

queue = deque()

# Add start. Counting the traversal moves as 0
# Add all starts for a and shortest will be taken
# queue.append([start, 0])
for y in range(H):
    for x in range(W):
        if grid[y][x] == 97: 
            queue.append([(y, x), 0])

included_locs = set()

debug_grid = deepcopy(grid)
for i in range(H):
    for j in range(W):
        debug_grid[i][j] = " "

last_q = []

while queue:
    loc, traversals = queue.popleft()
    last_q = [loc, traversals]
    if loc in included_locs:
        continue
    included_locs.add(loc)

    current_value = grid[loc[0]][loc[1]]

    # Show on debug the traversals to get to each point
    debug_grid[loc[0]][loc[1]] = (traversals, current_value)

    # Reached end
    print(f'cur value: {current_value}')
    if current_value == 123:
        print(traversals - 2)
        break

    # Check up
    if loc[0] > 0:
        up_value = grid[loc[0]-1][loc[1]]
        if (up_value-current_value) < 2:
            queue.append([(loc[0]-1, loc[1]), traversals+1])
    # Check down
    if loc[0] < H-1:
        down_value = grid[loc[0]+1][loc[1]]
        if down_value-current_value < 2:
            queue.append([(loc[0]+1, loc[1]), traversals+1])
    # Check right
    if loc[1] < W-1:
        right_value = grid[loc[0]][loc[1]+1]
        if right_value-current_value < 2:
            queue.append([(loc[0], loc[1]+1), traversals+1])
    # Check left
    if loc[1] > 0:
        left_value = grid[loc[0]][loc[1]-1]
        if left_value-current_value < 2:
            queue.append([(loc[0], loc[1]-1), traversals+1])    