from copy import deepcopy
from decimal import *

rocks = [[(0, 0), (1, 0), (2, 0), (3, 0)],
         [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
         [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
         [(0, 0), (0, 1), (0, 2), (0, 3)],
         [(0, 0), (1, 0), (0, 1), (1, 1)]]
 
# rock additional height above local origin of rock
rm = [0, 2, 2, 3, 1]

jets = """>>><<<<><<><<<>>>><>>>><<><<<<>>>><<<<>><<>><<<>><<>>>><<<>>>><<<<>>><>><<<<>>><<<<>>>><<<>>>><<<>><<><><<>>><<<<>>>><<<><<<<>>><<<<>>>><><<<<><<<>>>><<<<>>><<><<<<>>>><<<>>>><<<><<<<>>><<<<>>><<<<>><<<<>>>><<><<<>><<<><<<>>>><<<<>><>><<><<<<><<<>>>><<<>><<<>>>><>><<<>>>><<>>><>>>><>>><<<<><<<>>><<<>>><<<<>>>><<<><<<<><>><<<>>>><>><>><>><>><<>><<<>>>><<><>><<<<>><>><<>><<<<>>><<<>><>>><>><<>>><>><<<<>><<<<><<<<>><<<>><<<>><<>><>>><<<<><<<>>><>>><>>>><<>><<<<><<<<>><<<>>>><<<<><<<>>><<<>>><<<>>>><<><<<>>>><>>><>>><<<<>>><<<<>>>><>>><<<<>><<>><<<<><><<<><>>><<<<>>><<><><<<<>>><<>>>><>>><>><<>>>><<>><<>>><>><<<><>>><<>>>><<><><<<>><<<<>><><<<<>><<>>>><<>>><>>><>>><>><<<>>>><<<<>><<><<<>><>>><<<>>><<<>>><<<<>>>><<<>>><<<<>>><<<><<>>>><<<<>>><<<<>><<<>>><<>>>><<<<><<<<>><<><<<<>>><<<<><<<><<<>><>>><<<>>><>><<<><<<<>><<<>>>><>>>><<<><<<>>><>>><<<>>><<<><>>><>><<<<>>><<>>><<>>>><><<<<>>><>><>>>><>>><<<<><<<>>><<>>>><>><<<>>>><<<>><><<<><<<>><<<><>>><><<<<>><<>>>><><<<>>>><>>>><<<>>>><<<<>>>><<<<>>><<<><<<>>>><>>>><<<<>><<<<>>>><<>><>><<<<>><<><<<>><<<<>>>><>><<<<><<<>><>>><<<<>><>>>><>>>><><<><<<<>><<<>><<>>><<<>>><<<<>>>><<<>>>><<<>><<<<>><<<<><>>><><<<<><<><<<><<>>>><<<><<><<>>>><<>>>><>>>><>><<<<>>>><<<<><>><<>>><><<<<>>>><<>><><<>>><<<<>>><<<>>><<<>><>>><<<<>>>><>>>><>>><<<>>>><<>>><>>>><<>>>><<<<><>>>><<>><<<><>>><<<>>><>>>><<<>>>><>><<<>>>><>><><<<<>>><<<<>><<<>>>><>>>><<<<>><<<>>>><<><<<><<<>>><<<<>>>><<<><<>><>>><<<<>>><<<>>>><>>>><<<<>>>><<>>><<<>><>>>><<<<>><<<<><>>><<<<>>><>>>><<<<>>><>>>><<><<>>>><<>>><<<<>>>><<<<>><<<<><<<>>><<<<><<<><>>>><>>><<>><<<<>><><>><<>>><>>>><><<<>>>><<>><<<>>>><<>><<><<>>>><<<<>>>><<<<>>><<<<>>><>><<<>>><<<>>><<<<>><<><>>>><<<>>><<>>>><<>>><<>>><<<<>>>><<<<>>>><>><<<>><<<<>>>><<<>>>><><><<<<>>><<<>>><<<<>>><<<><<<<>><<<>>><<<>><<>>>><<>>><<>>>><<<><<>>>><<><<<><<<>>><<<<>>><>>><<<<>>><>>><<<>>>><>>><<<><<><>>><<>>><<>>>><<<<>><<<<><><<<<>>>><<<<>><<<><<<>><<<>>>><<>><<>>>><<><<>>><<<<><<<>><<<>>><>><<>><<<<>>>><<>>>><<<><>>><<<><<>>><<<<>>>><<<>>><<>>>><<<<>>>><<<>>>><<<>><<<>><<<<><<<<><<>>><<<<>><<<>>><>><>><><<<>>>><<>>><>>><<><>>>><<>>><<>>><<><><<<<>><<<>><<<<>>>><>>>><>>><<<<>><<<><<<>>><<<<><<><>>>><<<>>><<<><<>>>><<<>><<<<>>><>><<<<>><<<>><><<<<><<<<>><>><<<>>>><<<>>><<<>>><>>><<<>><<>>>><<<>>><<<<>><>>><<>>>><>><<<<>>>><>><<<>>>><>>><<<<>>><><<<>><<<>>><>><<<<><<<><<<>>>><>>>><<<<><>>>><<>>>><>>><<>>><>>><<<<>>><<<><>>>><>><<>>><<<<>><<<><<<><>>>><<<<>><<>><<<<>>>><>>>><><<<<>><<<>>>><<<>>>><<<>>>><<>>>><<<><>>>><<<>>>><<<<><<<>><<<<><><<<>><<>><<>><<><<<<><<>><<<<>>>><<<>>><<<><>><<>>>><<>>><>><<><<<><>>><<><>><<<><>><<<><<<>><<>>><<<>>>><<<<>><<<>>><>>><<<<>>><><<<<>>><<<<>>>><>><<>>>><<<<>>><<<>>><><>>><><<<<>>>><<<>>>><<<<>><<><<<<>>>><<><>>><<<>>><<>>><<<><<>>>><<<<>>><<<>>>><<<<>><<<>>>><<<>><<>><><<<>><<<<>>>><>><<<<>><<><<<<>>>><>><<>>>><>>>><><<<<>>>><<>><>>>><<>>>><<><<<<><>>>><>>><<>>><<<><<>>><<>>>><>>>><>>><>>>><<<>><<<<>>><<>>><<<<>>><><<>><<>><<<>><<>><<<>>>><<>>>><<<<>>><<<>>>><<<>>>><><<<<>><<>><<<<><<<>>><<<>><<<<>><<<<>>>><<<<>><<<>><<>>>><<<<>>>><<<<>>><<<<>>>><<>>><<>>>><<>><<<>>><<>><><<<>><>>>><<<>>><>>><<<>>>><<<<><>><<<<>><<>>>><<>><<<<>>>><<<><<><>>>><>>>><<><<<>>>><<>><<<<>>>><<<<><>><<<>><>>><<<<><>>>><<><<>>>><<<<>>>><<<<><<<>><<>><<>><>>><<<><<<<>>>><<>><<>>>><>>>><<<><>>>><<<<>>>><<<<>>>><<>>><<<<>>><<<>><>>>><<<><<>>><<>>>><><<<>><>>>><<<><<>><<>><<<>>><>><>><<>>>><>>><<><<>><<<><>>>><<<<>>><<<>><<<><<<<>><<<><>><<<><<>>><<<>>><>><>><<<>>>><<<><>>>><>>><<>>>><<<>><<<<>>>><<<>><>>>><<><<<>><>>><<<>>><<>>>><><>><<<>>>><<<><>>>><<<>>><<<>><<>>><>><>>>><<<<>>>><<><><<<<>>><>><<<<><>><<<>>>><<<<>>><<<<>>><<>><><<<<>><<<<>>>><<<<>>><<<>>>><<<<>>><<<<>>><<<>><>><<>>><<<>><>>><<><<<>>><>>><<<><<>>><>><<<<><<<>>><>><<<<>>><><>>>><<>>>><<<>><<<>>>><<<<><<>><>><>>>><><<<<><<><<><<<>>><><<<<>><<>><<<>>>><<>>><<<>><>><>>>><<>>>><>>>><>><>>>><>>><>><<<<>><<<<>>>><<<><<<><<<<>><>>><<>><<<<>><<<<>>><<<<>>><<<>>>><<<<>><<<>><<<><<<><<<<>>>><<<><<>>><<<>>><<><<<<>><<>>><><<<<>><><<<>>>><<<>>>><<<<>>>><><<>>><><><<>><>><>><<<>>><>><<<>><<<<><<<<>>>><<<>>><>>><>>>><<><<>>>><>>><><>><<>>>><<<>><<<<>><>>>><>>><<<<>>><<>>>><><<<>>><>>><>>><<<<>>>><<>><<<>>>><<>><>>>><<>><<>>><<<<>>>><>>><>>>><<<<>>><<<<>><>>>><<<>><><<<<>>>><<>>><<><<><><<<>>>><<>>>><<>>><>>><<<>>><>>><<<>>>><<<>><<<<>><<>>>><<><<<><<<>><<<<>>>><<<>><<>>><<<<>>><<<>>><<<<><<><>>>><<<<>><><<><<<>><<<<><<<>><<<>>><<>><<<<>>><<<><<<<>><<<<>>><><<<>>><<<<>>><<>>><>>>><<>>><<>><<<><<<<>><<>>>><<<<>>><<<<>>>><<<>><<<<>>>><<<<>>><<<>>><>><<><<<<><<<<>>>><<<><<><<<<><<<<>><>><<<>><<><<<><<><<<>><<<<><>>>><<<>>>><>><<>>>><>>>><>>>><<<>><<<>><<<<>>>><>>>><<<>>><<>>>><<<>>><<>>>><<<<>>>><><>>><><<>>><<<<>>>><>>>><<<>>>><<>>><<>><<<>>><<<<>><<<<>><<>><<<>><<>>>><>>><><<<<><><>>>><<<>>>><<<<>>><<>><>><<<<><>>><<<<>>>><<<<>><>>><<<>>><>>>><><>><>>><><>>>><><>>><<>><<><<<<>><<<<><<<<><<>><<<<><<<>><<<>>>><><<<<>>><<><<<<>>>><>>>><>>><<<>>><<<>>>><<>>><<><>>><<<><>><<<<><<<<><><<<>><><<>>>><<<>><<><<<<>><<>>><>><<>>><>><<<><>>><<>>>><<<<>><>>>><<<>>><<<>>><<>>>><<<>>><<<><>><<>>>><<>><>><<<<>><<<>>>><><<<<>>><>>><<>>><<<<>><<<>>><<>>>><<<>>>><><<<>><<>>>><<<>>><<<<><<<<>><<<<>><<<<>><<>>><<<>><<<>>>><<<<>>><<>>><<<<>>><<<>><<<<><><>><<>>>><<>>><<<<><<<><<<<><<<><><<<>>><>>>><<<<>>>><<><<<>>>><<><<<><><<>><<<<>>><<<><<<>><<<>>><>>><<<<>>><>><<>>>><<<<><<<>><<><>>><<<<>>>><><<>><>>>><<<>>>><<<<>>>><<<>>>><>>><<<>>><<<<><<<<>>>><<<<>>><<><<<>><<<<>><<<>>>><<<<>><<>>><>>><<<<><><<<>><>><>><<<>><<<<>>>><<>><>><<<>>><><<<<>><<>><<<><<>>>><><<<><<>><>><<>>>><<<<>><>>><<<<><<<><<>><<<<>><<<<>>>><<>>><<<<>>><<<>>>><<>>><<<><>>>><<<<>><<<<>><<>>>><<<>>>><<>><<<>>><>><<<<>>>><>><<<<><<<>><<<<>><>><>>>><<<>>>><><><>>>><<<<>>><<<>>><<<<><<>><<><<>>>><<<><<<<>>>><<>>>><<>>><<>><<<<>><<<<>>><>>><>>>><>><<<>>>><<>><<<><<<<><<<>>><<<>>>><<<><<>><<>>><><<<<>><<><<<<><<<>>>><<<<>><<>><<><<<>>><<<<>><<>>><<<>>><<<>><<<>>>><>>>><<>>><<<<>>><>>>><<<><<<>>><<<>><>>><>><<<>>><>>><<<>>><<<<><<<><<<<>><<<<>><<>>><>>><<<<><<>>>><<<<><<>>>><>>>><>>><<>>>><<>>>><<<<><<>><<>><<><>><><<<<>>><>>><<>><<<<>>>><<<<>><>><<<<>><<<>>><<<<>><<>><<>>><<<>>><<<<>><<<<><>><<<<>>><>>>><>><<>>>><>>>><<<<>><<>>><<>>><<>>>><><<><<<<>><<<<><<>>><>>><<<<><<<<>>><<<<>><<<>><<>>>><<<<><<>>>><<<>>>><<<<>>>><<<<><<<<>><<<<>>>><<<>>>><>><>>><<<<>><<<>><<<>><<>><<<<><>><<>><><<<<><<<<>>><<><<<<>><<<>>>><<<><<<<><<>>>><>>><>>><<<>><<<>>>><>>>><<>>><<<<>>><<>><><<<>>>><<><>>>><>><>>>><<<>>>><>>><<>>><>><>>><<<<><<>><<>><>>><>>><<<>><<><<>><><<>>><<>><<>><<<>><<<>>>><>>>><><<<<>>>><<<><<<>>><>><<<<><<<<>>><>>>><<>>>><<>>><>>>><>>>><<<<>>>><<>>><<<<>>><<<>><>>><<<<>>><>><<>>>><<>><<>><><><<<>>>><><<<>>><<<>><<>>>><<>>>><<>>><<>>><<>>><<<><<<<>><<<<>><<<<>><<><<<<>>>><<><<<<>>>><<<<>><<<>>>><<<>><<<<><<<<>>>><<<>><>>>><><>>>><<<<>><<<>>>><<<><<<>>>><<<<><<<>><><<>>><<<<><<>><<<<>>><<<<><<<<>><<<<><<><<<<>><><<<>>><>>>><<<<>><<<>>><<>><<<><>>>><>>><<<<>><>>>><<<><<>>>><<<<>>><<<>>><<><<<<>>>><<<>>><<>>><>>>><<<>>>><>>><<<<><>>>><<>>><<<><>>>><>>>><<<><<><<>><<<<><>>><><<<>>><<>>>><<<<>>><>><<<>><<<>>><<>>><<>>><<<>><<<<>><<<>>><<<>><<<><<<<>>><>>><<<<><<<><<<>>><>>><<><<<<>><<<<><<>><<>>>><<<><>>>><<>>>><<<><>><><<<<><<<><>>><<<<>><>><<<><<><<<<>>><>>><<<>><<<>><>>><<><<<<>>>><<>>>><><><>>>><<>>><<>>><<<<>><<><<<<>><>>><><<<<>>><<<<><<<<>>><<<>>><<<<>>>><<>>>><<<<>><<<>>>><<>>><<<<>><<><<<<><<<><<<><<<<>>><<<<>>>><<>>><<<<>><>><<>><<>>>><>>><<<<><<<<>>><<<>><<><<>>><>>><<<><>>><>>><><>><<<>>>><<<<>>><>><<<><<<>>>><<><<<<>>><<<>>>><<<><<>>>><<<<>>><<><<>>><<>><<>>>><<>>>><<<>>><<<<>><<>><<<<><<<>>><>>>><<>>><>>><<>>><<<>>>><>>>><>>>><<<><>>><<<<>><<<>>><<<>>>><<<<>>>><>>><<<<>>>><<<>>>><>>><<>><<<>>>><<<>><<<>>>><><><>>><<><>>><>>>><>>>><<<<>>><<<><<>>>><<<>>>><<<><>><>>><<<>>>><>><<>><>><<<>>>><<<<>>><<<<><<<<>>>><<<<>>><<>>>><<<<>>>><<<<>><<<>><><<<>>><<<<>>><>>>><<<<>><<>><>><<>>><>>>><<<<><<<><<>>><<<>><<<<>>><<>>><<<>>><<<<><<<>>>><<<>>>><<<>>><>>>><<>>>><<>><<><<>>><><<>><<<<>>>><<<><>>>><<<>><<<<>>>><>>><<<><>>><<<<>>><><<>>>><<<<><<<<>><>>><<<><>>>><<<<>><>>>><<<><<<>>>><<<>>><<<><<<>><<<<>>>><<<>><<<<><<<><<><<<<>>><<<<>>>><<><<<<>>>><><<<<>>>><<<>>><<<>>><<<<><>><<<<>><<<><<<<>>><<><<<<><<>>><<<><<<<><>>><<<<><<<>>>><<<<>>>><<>>>><>><<<<>>><><<<<>>>><<<<>><<<>><<<><<>>><<>>>><>>><<>><<<>><<>>><>>>><<>>>><>>><<<<>><><>>>><<><<<<>>>><<<<>>>><<>><>>><<<>>><<>>>><>>>><>>>><<<<>><<<<>><<<<><<<>>>><>>>><<<<>>>><>><<>>>><<<<>>><<<>>><>><<><<<>>>><>>><<>><<<><>><<<<>><<><>>><<<<><<<>><>>><<<>>>><<>>>><<<<>>><<>><>>><<<<>><<>><<<<>>><><<>>><<><<<<><<<<>><>>><<><<<><<<<>><>>><<>>>><<<>><<<>><<<>>><<<>>>><>>>><<>>><<<>>><>><>>>><>>>><<<>><>>><<<>><<>><>><<<<>>><>>><<<><<<>>>><<<>><<<>>><>>><<<><>>>><<<<><>><<>><<<<><<<>><<>>><<<><>>><<<><<<<><<<<><>><<>>>><<<<>>><<<<>><<<<>>><<<<><<><<<>>><><<>><<>>>><<>>><><<<<><<<<>>><><<<>>>><<<<>>>><<<<>>>><<>><<>><<>><<<>><>>><>><<<<>><<><<<>>><>>><><>>><<<>>>><<>>><>><<<>>>><<<>><<><><<<><>><<<<>>><<<<>><<<<>><<<>>><<<<>>><<<<>>>><<<>>><<<<>><<<<><><<<>>><<<><<><<><<<>><<>>><<>><<><<>>>><>><<<<>>>><>>>><<<<>>><<<<>>><>><<<><<<>>>><<<<>><<<<><<><<<<>>>><<<<>><<<<>>>><<<<>><<<>><<>><<<<>><>><<>>>><<<<><<<><>>><>><<<>>>><><<<><>>>><<<>>><<<>><<<><<<>><<><>>>><<><>>><>><<<>>><<<<>><<><<>><<<<>><<<<><<<>>>><<<<>><<<>>>><>>><<<>><<>>>><<><><<<<><<<<>>>><<<>><<<<>><>>>><<><><<>>>><<<><<<<>><>><>>><<><<<<>>>><<>><<<<><<>>><<<>>><<<>>><<<>>>><>><<<>>>><<<>>>><><<<<>>>><>><<<<>><<<<>>>><<>>><<<>>>><<>><<><<<>>><<>>>><<<<>><<<<>>><>>>><<<>>><<>>>><<>>><><>><<<<>><<<>>>><<>><<<>><<<>>><<<>><>><><<<<>>><<<><<>>>><<>>>><<>><<<><<<><<<<><<><>>>><<<>>>><<<<>>><>><<>>>><>><<<>>>><<<>><<>>>><<<<>>><<<><><<>>><<>><<<>>><<<<>><<>>>><<<><<<<><<>>>><<>>><<<<><<<<><<<>>><<>>><>><<><<><<>>><><>>>><<<>><<>>>><>>>><<<<>><><<<<>><<<<>>>><<>>>><<<<><<<>>><<>>><<><<<<>><>><<><<><<><<<><<<<><>><<<>>>><<<<>>>><<<><>>>><<>>><><>>><<<>>><<<><<>>><<><><<><<<<><<<<>>>><><><<<<>>><>><<>>>><<<<>>>><<<>>><<<><<><<<<><<<<>>><<<<>>>><<<>><<<<>>>><<><<<>><><>>>><<<>>>><<<>>>><<><<<>><>>>><<<><>><<<<><<<<>>><<<<>>>><<><<<>>>><><><<<<><<<<><>><<><>>>><<<>><<>><"""
jetst = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

print(len(jets))
runs = int(50455*52)
gridsize = int(runs*1.6)
#jets = jetst

# Make the grid 2darray
grid = [[0 for x in range(7)] for y in range (gridsize)]
grid_d = [[" " for x in range(9)] for y in range (7)]

for row in grid:
    row.insert(0, 9)
    row.append(9)
grid.append([9 for x in range(9)])

def check_right(rock, loc):
    for r in rock:
        r = (r[1]*-1 + loc[0], r[0] + loc[1])
        if grid[r[0]][r[1] + 1]:
            return False
    return True

def check_left(rock, loc):
    for r in rock:
        r = (r[1]*-1 + loc[0], r[0] + loc[1])
        if grid[r[0]][r[1] - 1]:
            return False
    return True

def check_down(rock, loc):
    for r in rock:
        r = (r[1]*-1 + loc[0], r[0] + loc[1])
        if grid[r[0] + 1][r[1]]:
            return False
    return True

def solidify_rock(rock, loc):
    for r in rock:
        r = (r[1]*-1 + loc[0], r[0] + loc[1])
        grid[r[0]][r[1]] = 4

def debug_solidify(rock, loc):
    grid_temp = [[" " for x in range(len(grid[0]))] for y in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                grid_temp[i][j] = "#"
            else:
                grid_temp[i][j] = " "
    for r in rock:
        r = (r[1]*-1 + loc[0], r[0] + loc[1])
        grid_temp[r[0]][r[1]] = "#"
    return grid_temp
    

MAX_HEIGHT = gridsize-3
s = 0
rot = len(jets)
for i in range(runs):
    #print(f'Max height {MAX_HEIGHT}')

    rok = rocks[i % 5]
    # for _ in range(rm[i % 5]):
    #     grid.insert(0, [9, 0, 0, 0, 0, 0, 0, 0, 9])
    #     MAX_HEIGHT += 1

    loc = (MAX_HEIGHT, 3)

    while True:
        #grid_d = debug_solidify(rok, loc)

        j = jets[s % rot]

        #print(f"instruction: {jets[s % 40]}")

        if j == ">":
            if check_right(rok, loc):
                loc = (loc[0], loc[1] + 1)
                #print(f"success")
        if j == "<":
            if check_left(rok, loc):
                loc = (loc[0], loc[1] - 1)
                #print(f"success")
        s += 1

        
        #grid_d = debug_solidify(rok, loc)
        # Try to fall
        if check_down(rok, loc):
            loc = (loc[0] + 1, loc[1])
            #print(f"instruction: down")
        else:
            #print(f"instruction: solidify")
            solidify_rock(rok, loc)

            MAX_HEIGHT_THIS = loc[0] - rm[i % 5] - 4
            if MAX_HEIGHT_THIS < MAX_HEIGHT:
                MAX_HEIGHT = MAX_HEIGHT_THIS
            break

pass
a = []
for row in grid:
    if row != [9, 0, 0, 0, 0, 0, 0, 0, 9]:
        a.append(row)
print(len(a))
pass

ratio = Decimal(len(a))/Decimal(runs)
print(ratio)
pass

#pattern at 50455 and ratio height/runs
# 0 4 0 0 0 0 0

# at 50455 * 2
# 0 0 0 4 0 0 0

# * 3
# 0 0 4 0 0 0 0
# 1.535249231988901

# * 100 (5million stacks) (took around 5-10mins not exactly sure)
# 0 0 0 0 4 4 0
# 1.5354799326132198
# 
# 1535479932613 # 5 Million sim * runs
# 1535249231988 #  150k sim * runs
# 1000000000000

# rerun 250k runs but use decimal for ratio for more precision
# 1.535324546625706074720047567
# Chop it down
# 1535324546625
# 1000000000000

# Check 2.5 ~ million to get all permutations took 1-2min
# 1.535472965247021336606115122
# 1535472965247
# 1000000000000

# Still very different so can't really make conclusions