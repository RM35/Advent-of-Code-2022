from collections import defaultdict
from collections import heapq

data = open("twentyfour/t").read().split("\n")

grid = []

for y, row in enumerate(data):
    grid.append([])
    for x, col in enumerate(row):
        grid[y].append(col)