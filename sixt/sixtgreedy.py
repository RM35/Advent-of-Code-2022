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


# gets stuck

q = []
heapq.heapify(q)
heapq.heappush(q, graph["AA"])

mins_left = 30
total_value = 0
while q and mins_left > 0:
    node = heapq.heappop(q)
    max_value_neighbour = 0
    if len(node[1]) == 0: break
    if len(node[1]) == 1:
        heapq.heappush(q, graph[node[1]])
        mins_left -= 1
        continue
    for i, valve in enumerate(node[1]):
        if i == 0: 
            max_value_neighbour = valve
            continue
        if graph[valve][0] > graph[max_value_neighbour][0]:
            max_value_neighbour = valve
    heapq.heappush(q, graph[max_value_neighbour])
    mins_left -= 1
    if graph[max_value_neighbour][0] == 0: continue
    mins_left -= 1
    total_value += graph[max_value_neighbour][0] * mins_left
    graph[max_value_neighbour][0] = 0
    

print(total_value)
    







