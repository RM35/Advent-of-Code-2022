data = open("ninet/test.txt").readlines()
bps = []

for bluep in data:
    ore = [int(bluep.split()[6]), 0, 0]
    clay = [int(bluep.split()[12]), 0, 0]
    obby = [0, int(bluep.split()[18]), int(bluep.split()[21])]
    geo = [int(bluep.split()[27]), 0, int(bluep.split()[30]),]
    bps.append([ore, clay, obby, geo])