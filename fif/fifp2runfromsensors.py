
import re

sens = []
beac = []
LINE = 2000000
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

# onlinecount = 0
# beacon_set = set(beac)
# for sen in sens:
#     if sen[1] == LINE:
#         onlinecount += 1
# for bea in beacon_set:
#     if bea[1] == LINE:
#         onlinecount += 1



# discovered = set()
# for dist, point in dists:
#     if p_t(point, (point[0], LINE)) > dist: continue
#     if point[1] == LINE:
#         for i in range(dist*2):
#             discovered.add(((point[0]-dist)+i, LINE))
#     else:
#         y_offset = point[1] - LINE
#         percent_along_triangle_from_point = 1 - (abs(y_offset) / dist)
#         width_on_line = int(dist * 2 * percent_along_triangle_from_point) + 1
#         if width_on_line == 1:
#             discovered.add((point[0], LINE))
#             continue
#         for i in range(width_on_line):
#             discovered.add(((point[0]-(width_on_line//2)+i), LINE))

# print(len(discovered)-onlinecount)


import random

rand_point = [random.randint(0, 4000000), random.randint(0, 4000000)]

def p_t2(p1, p2):
    return (p2[0]-p1[0], p2[1]-p1[1])

resolution_of_steps = 10000
steps_at_res = 0
notfound = True

total_count = 0
while notfound:
    total_count += 1
    if total_count % 100000 == 0:
        print(f'total_count: {total_count}')
    if total_count % 1000000 == 0:
        rand_point == [random.randint(0, 4000000), random.randint(0, 4000000)]
        steps_at_res = 0
        resolution_of_steps = 10000
    if steps_at_res > 100:
        steps_at_res = 0
        resolution_of_steps = resolution_of_steps // 2
        if resolution_of_steps < 0: resolution_of_steps = 0
    
    cont_count = 0
    for dist, point in dists:
        dist_to_sensor = p_t(rand_point, point)
        if dist_to_sensor > dist: 
            cont_count += 1
            if cont_count == len(dists):
                notfound = False
                print((rand_point[0]* 4000000) + rand_point[1])
                break
            continue
        disp_to_sens = p_t2(rand_point, point)

        if disp_to_sens[0] > 0:
            rand_point = [rand_point[0]-resolution_of_steps, rand_point[1]]
        if disp_to_sens[0] < 0:
            rand_point = [rand_point[0]+resolution_of_steps, rand_point[1]]
        if disp_to_sens[1] > 0:
            rand_point = [rand_point[0], rand_point[1]-resolution_of_steps]
        if disp_to_sens[1] < 0:
            rand_point = [rand_point[0], rand_point[1]+resolution_of_steps]
        
        steps_at_res += 1

        if disp_to_sens == (0, 0):
            notfound = False
            print(rand_point)
            break