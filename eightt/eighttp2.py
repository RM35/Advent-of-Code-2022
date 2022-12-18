from collections import defaultdict, deque
from datetime import datetime

droplets = 0
with open("eightt/eightt_input.txt", "r") as f:
    data = f.readlines()
    data = list(map(lambda x: x.strip(), data))
    for i, line in enumerate(data):
        data[i] = tuple(map(int, line.split(",")))
    droplets = set(data)


def adjacent(p1, p2):
    x_delta = abs(p1[0] - p2[0])
    y_delta = abs(p1[1] - p2[1])
    z_delta = abs(p1[2] - p2[2])
    return ((x_delta + y_delta + z_delta) == 1)

face_count = {}

for drop in droplets:
    face_count[drop] = 6

for p in droplets:
    for pp in droplets:
        if adjacent(p, pp):
            face_count[p] -= 1

surface_area = 0
for p, faces in face_count.items():
    surface_area += faces

q = deque()
start = (0, 0, 0)
q.append(start)
explored = set()

bfs_max_bounds = 30
bfs_min_bounds = -2

start_time = datetime.now()
print(f'BFS START: {start_time}')

while q:
    node = q.popleft()
    if node in explored: continue
    explored.add(node)

    # +ve x
    if node[0] < bfs_max_bounds:
        if (node[0]+1, node[1], node[2]) not in droplets:
            q.append((node[0]+1, node[1], node[2]))
    # -ve x
    if node[0] > bfs_min_bounds:
        if (node[0]-1, node[1], node[2]) not in droplets:
            q.append((node[0]-1, node[1], node[2]))
    # +ve y
    if node[1] < bfs_max_bounds:
        if (node[0], node[1]+1, node[2]) not in droplets:
            q.append((node[0], node[1]+1, node[2]))
    # -ve y
    if node[1] > bfs_min_bounds:
        if (node[0], node[1]-1, node[2]) not in droplets:
            q.append((node[0], node[1]-1, node[2]))
    # +ve z
    if node[2] < bfs_max_bounds:
        if (node[0], node[1], node[2]+1) not in droplets:
            q.append((node[0], node[1], node[2]+1))
    # -ve z
    if node[2] > bfs_min_bounds:
        if (node[0], node[1], node[2]-1) not in droplets:
            q.append((node[0], node[1], node[2]-1))

print(f'BFS END: {datetime.now()}')
print(f'BFS TIME: {datetime.now() - start_time}')

for p in droplets:
    for pp in explored:
        if adjacent(p, pp):
            face_count[p] -= 1

surface_area_internal = 0
for p, faces in face_count.items():
    surface_area_internal += faces

print(surface_area - surface_area_internal)
pass
    
