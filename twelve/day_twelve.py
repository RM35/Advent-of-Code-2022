import heapq
from copy import deepcopy

grid = []
with open("twelve/day_twelve_test.txt") as f:
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
        if grid[y][x] == 69:
            end = (x, y)

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
        if grid[y-1][x] == 69:
            up_cost = 0
        else:
            up_cost = abs(grid[y-1][x] - grid[y][x])

    if y == len(grid)-1: 
        down_cost = 100000
    else:
        if grid[y+1][x] == 69:
            down_cost = 0
        else:
            down_cost = abs(grid[y+1][x] - grid[y][x])
    
    if x == 0: 
        left_cost = 100000
    else:
        if grid[y][x-1] == 69:
            left_cost = 0
        else:
            left_cost = abs(grid[y][x-1] - grid[y][x])

    if x == len(grid[y])-1: 
        right_cost = 100000
    else:
        if grid[y][x+1] == 69:
            right_cost = 0
        else:
            right_cost = abs(grid[y][x+1] - grid[y][x])
    
    return {"up": up_cost, "down": down_cost, "left": left_cost, "right": right_cost}

def calc_dist(current, end):
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


def a_star(start, end):
    global path_debug
    open_list = []
    closed_list = []
    heapq.heappush(open_list, (0, start))
    while len(open_list) > 0:
        current = heapq.heappop(open_list)[1]
        if current == end:
            return closed_list
        closed_list.append(current)
        path_debug[current[1]][current[0]] = "#"
        cost = cost_function(current[0], current[1])
        to_add = []

        if cost["up"] < 2:
            to_add.append([(current[0], current[1] - 1), cost["up"]])
        if cost["down"] < 2:
            to_add.append([(current[0], current[1] + 1), cost["down"]])
        if cost["left"] < 2:
            to_add.append([(current[0] - 1, current[1]), cost["left"]])
        if cost["right"] < 2:
            to_add.append([(current[0] + 1, current[1]), cost["right"]])

        for new in to_add:
            if new[0] in closed_list:
                continue
            new_cost = new[1] + calc_dist(new[0], end)
            heapq.heappush(open_list, (new_cost, new[0]))
        print(f"open count: {len(open_list)} closed count: {len(closed_list)}")
    return None

path_debug = deepcopy(grid)

path = a_star(start, end)
#print(path)
print(len(path)-2)
