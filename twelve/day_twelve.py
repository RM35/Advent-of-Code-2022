import heapq
from copy import deepcopy
from pprint import pprint

grid = []
with open("twelve/day_twelve_input.txt") as f:
    grid = f.readlines()
    grid = list(map(lambda x: x.strip(), grid))
    for i, line in enumerate(grid):
        grid[i] = list(map(ord, line))

# S = 83
# E = 69
# Find start and end

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 83:
            start = (x, y)
            grid[y][x] = 97
        if grid[y][x] == 69:
            end = (x, y)
            grid[y][x] = 122

def cost_function(x, y):
    global grid
    up_cost = 0
    down_cost = 0
    left_cost = 0
    right_cost = 0

    our_value = grid[y][x]
    #if start set these costs
    if our_value == 83:
        return {"up": 100000, "down": 1, "left": 100000, "right": 1}

    if y == 0: 
        up_cost = 100000
    else:
        if grid[y-1][x] == 69 and grid[y][x] == 122:
            up_cost = 0
        else:
            up_cost = abs(grid[y-1][x] - grid[y][x])

    if y == len(grid)-1: 
        down_cost = 100000
    else:
        if grid[y+1][x] == 69 and grid[y][x] == 122:
            down_cost = 0
        else:
            down_cost = abs(grid[y+1][x] - grid[y][x])
    
    if x == 0: 
        left_cost = 100000
    else:
        if grid[y][x-1] == 69 and grid[y][x] == 122:
            left_cost = 0
        else:
            left_cost = abs(grid[y][x-1] - grid[y][x])

    if x == len(grid[y])-1: 
        right_cost = 100000
    else:
        if grid[y][x+1] == 69 and grid[y][x] == 122:
            right_cost = 0
        else:
            right_cost = abs(grid[y][x+1] - grid[y][x])
    
    return {"up": up_cost, "down": down_cost, "left": left_cost, "right": right_cost}

def calc_dist(current, end):
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

# Need to return the pruned direct/shortest path still to fix test.
# full input still broken on top
def a_star(start, end):
    global path_debug
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0, start))
    while len(open_list) > 0:
        current = heapq.heappop(open_list)[1]
        if current == end:
            return closed_list
        closed_list.add(current)
        path_debug[current[1]][current[0]] = "#"
        cost = cost_function(current[0], current[1])
        to_add = []

        if cost["up"] < 2:
            to_add.append([cost["up"], (current[0], current[1] - 1)])
        if cost["down"] < 2:
            to_add.append([cost["down"], (current[0], current[1] + 1)])
        if cost["left"] < 2:
            to_add.append([cost["left"], (current[0] - 1, current[1])])
        if cost["right"] < 2:
            to_add.append([cost["right"], (current[0] + 1, current[1])])

        for new in to_add:
            if new[1] in closed_list:
                continue
            new_cost = new[0] + calc_dist(new[1], end)
            new[0] = new_cost
            if new in open_list:
                continue
            heapq.heappush(open_list, new)
        print(f"open count: {len(open_list)} closed count: {len(closed_list)}")
    return closed_list

def db_cells(loc, size, grid):
    local_area = [[x for x in range(size)] for y in range(size)]
    for y in range(size):
        for x in range(size):
            local_area[y][x] = grid[loc[1] - 1 + y][loc[0] - 1 + x]
    print(local_area)

path_debug = deepcopy(grid)

path = list(a_star(start, end))

print(path)
print(len(path))
