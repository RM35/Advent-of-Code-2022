from collections import defaultdict

data = 0
with open("eightt/eightt_input.txt", "r") as f:
    data = f.readlines()
    data = list(map(lambda x: x.strip(), data))

droplets = set()
face_count = {}

for drop in data:
    drop = tuple(list(map(int, drop.split(","))))
    droplets.add(drop)

for drop in droplets:
    face_count[drop] = 6

def adjacent(p1, p2):
    x_delta = abs(p1[0] - p2[0])
    y_delta = abs(p1[1] - p2[1])
    z_delta = abs(p1[2] - p2[2])
    return ((x_delta + y_delta + z_delta) == 1)

for p in droplets:
    for pp in droplets:
        if adjacent(p, pp):
            face_count[p] -= 1

surface_area = 0
for p, faces in face_count.items():
    surface_area += faces

print(surface_area)
pass