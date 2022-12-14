minx = 100000
maxx = 0
miny = 0
maxy = 0

# point in, point origin
def p_t(p1, p2):
    return (p1[1]-p2[1], p1[0]-p2[0])

#Get bounds of cave
with open("fourteen/fourteen_test.txt") as f:
    for line in f.readlines():
        points = line.strip().split(" -> ")
        points = list(map(lambda x: [x.split(",")[0], x.split(",")[1]], points))
        for point in points:
            x = int(point[0])
            y = int(point[1])
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y > maxy:
                maxy = y

# build grid using bounds
grid = [[" " for _ in range(maxx-minx+1)] for _ in range(maxy-miny+3)]
or_p = (minx, 0)

points_of_rock = set()

with open("fourteen/fourteen_test.txt") as f:
    for line in f.readlines():
        points = line.strip().split(" -> ")
        points = list(map(lambda x: (int(x.split(",")[0]), int(x.split(",")[1])), points))
        # Make the rock formation
        for i in range(len(points)-1):
            points_of_rock.add(points[i])
            p_offset = p_t(points[i], points[i+1])

            # Going down
            if p_offset[0] < 0:
                j = 0
                while j < abs(p_offset[0])+1:
                    points_of_rock.add((points[i][0], points[i][1]+j))
                    j+=1

            # Going up
            if p_offset[0] > 0:
                j = 0
                while j < abs(p_offset[0])+1:
                    points_of_rock.add((points[i][0], points[i][1]-j))
                    j+=1
            
            # Going right
            if p_offset[1] < 0:
                j = 0
                while j < abs(p_offset[1])+1:
                    points_of_rock.add((points[i][0]+j, points[i][1]))
                    j+=1

            # Going left
            if p_offset[1] > 0:
                j = 0
                while j < abs(p_offset[1])+1:
                    points_of_rock.add((points[i][0]-j, points[i][1]))
                    j+=1
                
        
            

for point in points_of_rock:
    newp = p_t(point, or_p)
    grid[newp[0]][newp[1]] = "#"

# add the illegal edges
for row in grid:
    for i in range(30):
        row.insert(0, " ")
        row.append(" ")
    row.insert(0, "D")
    row.append("D")
for i, cell in enumerate(grid[-1]):
    grid[-1][i] = "#"
    


def sand_move(p):
    # Move down if possible
    down_cell = grid[p[0]+1][p[1]]
    rightdown_cell = grid[p[0]+1][p[1]+1]
    leftdown_cell = grid[p[0]+1][p[1]-1]

    # Move down
    if down_cell == " " or down_cell == "D":
        if down_cell == "D": return False
        grid[p[0]][p[1]] = " "
        grid[p[0]+1][p[1]] = "O"
        return (p[0]+1, p[1])

    # Move leftdown
    if leftdown_cell == " " or leftdown_cell == "D":
        if leftdown_cell == "D": return False
        grid[p[0]][p[1]] = " "
        grid[p[0]+1][p[1]-1] = "O"
        return (p[0]+1, p[1]-1)

    # Move rightdown
    if rightdown_cell == " " or rightdown_cell == "D":
        if rightdown_cell == "D": return False
        grid[p[0]][p[1]] = " "
        grid[p[0]+1][p[1]+1] = "O"
        return (p[0]+1, p[1]+1)

    return p

# Drop the sand
total_stacked = 0
sandstacked = True
while sandstacked:
    sand_moving = True
    sand = (0, 506-minx)
    while sand_moving:
        new_loc = sand_move(sand)

        if new_loc == False:
            sandstacked = False
            sand_moving = False
            break
        
        if new_loc == (0, 506-minx):
            sand_moving = False
            sandstacked = False
            break

        if new_loc == sand:
            sand_moving = False
            total_stacked += 1
            break
        

        sand = new_loc


        
print(total_stacked)