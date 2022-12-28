
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

onlinecount = 0
beacon_set = set(beac)
for sen in sens:
    if sen[1] == LINE:
        onlinecount += 1
for bea in beacon_set:
    if bea[1] == LINE:
        onlinecount += 1

def check_point(point):
    if not (0 < point[0] < 4000000 and 0 < point[1] < 4000000):
        return False
    checked = 0
    for dist, pos in dists:
        if p_t(point, pos) > dist:
            checked += 1
    if checked == len(dists):
        return True
    else:
        return False

def y_mx_b(p1, p2):
    m = (p2[1]-p1[1]) / (p2[0]-p1[0])
    b = p1[1] - (m * p1[0])
    return m, b


# if there is one spot then it must be on the edge of a manhatten diamond
# get the equation of each line representing the diamonds edges. check all
# adjacnet cells. This takes about 2 mins per sensor but the result is found on
# about sensor 3 so not toooo bad. need to multiply and add to get the final answer manually
for dist, pos in dists:
    print(f'Checking {pos} with dist {dist}')

    top_p = (pos[0], pos[1]+dist)
    bot_p = (pos[0], pos[1]-dist)
    left_p = (pos[0]-dist, pos[1])
    right_p = (pos[0]+dist, pos[1])

    # check upright side
    m, b = y_mx_b(right_p, top_p)
    for i in range(dist):
        x = pos[0] + i
        y = int(m * x + b) + 1
        if check_point((x, y)):
            print(x, y)
    
    #check downright side
    m, b = y_mx_b(right_p, bot_p)
    for i in range(dist):
        x = pos[0] + i
        y = int(m * x + b) - 1
        if check_point((x, y)):
            print(x, y)

    #check downleft side
    m, b = y_mx_b(left_p, bot_p)
    for i in range(dist):
        x = pos[0] - i
        y = int(m * x + b) - 1
        if check_point((x, y)):
            print(x, y)
    
    #check upleft side
    m, b = y_mx_b(left_p, top_p)
    for i in range(dist):
        x = pos[0] - i
        y = int(m * x + b) + 1
        if check_point((x, y)):
            print(x, y)