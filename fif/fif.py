
import re

sens = []
beac = []
LINE = 10
with open("fif/fif_input.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = re.split(r"[:, =]", line.rstrip())
        sens.append((int(line[3]), int(line[6])))
        beac.append((int(line[13]), int(line[16])))

def p_t(p1, p2):
    return abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])

dists = []

for i, sen in enumerate(sens):
    dist = p_t(sen, beac[i])
    dists.append([dist, sen])

onlinecount = 0
beacon_set = set(beac)
for sen in sens:
    if sen[1] == LINE:
        onlinecount += 1
for bea in beacon_set:
    if bea[1] == LINE:
        onlinecount += 1



discovered = set()
for dist, point in dists:
    if p_t(point, (point[0], LINE)) > dist: continue
    if point[1] == LINE:
        for i in range(dist*2):
            discovered.add(((point[0]-dist)+i, LINE))
    else:
        y_offset = point[1] - LINE
        percent_along_triangle_from_point = 1 - (abs(y_offset) / dist)
        width_on_line = int(dist * 2 * percent_along_triangle_from_point) + 1
        if width_on_line == 1:
            discovered.add((point[0], LINE))
            continue
        for i in range(width_on_line):
            discovered.add(((point[0]-(width_on_line//2)+i), LINE))

print(len(discovered)-onlinecount)