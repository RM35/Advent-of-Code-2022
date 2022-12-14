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
grid = [[" " for _ in range(maxx-minx+1)] for _ in range(maxy-miny+2)]
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

# add 1 cell buffer to left and right

for row in grid:
    row.insert(0, " ")
    row.append(" ")

def sand_move(p):
    pass
