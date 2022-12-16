
from collections import deque
import heapq

def parse():
    data = []
    with open("sixt\sixt_test.txt", "r") as f:
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


# try depth first greeeedy. gets stuck.

def bfs(graph, start):
    q = deque()
    q.append([graph[start], 0])
    depths = {"AA": 0}
    while q:
        node, traversals = q.popleft()
        for neighbour in node[1]:
            if neighbour in depths: continue
            q.append([graph[neighbour], traversals + 1]) 
            depths[neighbour] = traversals + 1
    return depths
        
a = bfs(graph, "AA")
pass        
    







