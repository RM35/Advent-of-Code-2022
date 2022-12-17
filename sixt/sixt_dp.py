from copy import deepcopy
from collections import deque
import heapq

def parse():
    data = []
    with open("sixt\sixt_input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().replace(",", " ")
            line = line.split()
            valve = line[1]
            rate = int(line[4].split("=")[1].replace(";", ""))
            connected_valves = line[9:]
            data.append((valve, rate, connected_valves))
    return data

def make_graph(data):
    graph = {}
    for valve, rate, connected_valves in data:
        graph[valve] = [rate, connected_valves]
    return graph

data = parse()
graph = make_graph(data)

